#!/usr/bin/env bash

set -euo pipefail

RELEASE_FILE="${RELEASE_FILE:-data/latest_release.json}"
APT_REPO_ROOT="${APT_REPO_ROOT:-static/apt}"
APT_REPO_URL="${APT_REPO_URL:-https://bitcoin-safe.org/apt}"
APT_SUITE="${APT_SUITE:-stable}"
APT_COMPONENT="${APT_COMPONENT:-main}"
APT_DATA_FILE="${APT_DATA_FILE:-data/apt_repo.json}"
APT_GPG_KEY_ID="${APT_GPG_KEY_ID:-}"
APT_KEYRING_PATH="${APT_KEYRING_PATH:-/usr/share/keyrings/bitcoin-safe-archive-keyring.gpg}"
APT_KEYRING_FILE="${APT_KEYRING_FILE:-bitcoin-safe-archive-keyring.gpg}"

APT_REPO_URL="${APT_REPO_URL%/}"
APT_KEYRING_URL="${APT_REPO_URL}/${APT_KEYRING_FILE}"

require_cmd() {
  local cmd="$1"
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "Error: missing required command '$cmd'" >&2
    exit 1
  fi
}

for cmd in curl jq dpkg-deb dpkg-scanpackages gzip md5sum sha256sum stat sort base64; do
  require_cmd "$cmd"
done

if [[ ! -f "$RELEASE_FILE" ]]; then
  echo "Error: release file not found: $RELEASE_FILE" >&2
  exit 1
fi

mapfile -t deb_assets < <(jq -r '.assets[] | select(.name | endswith(".deb")) | @base64' "$RELEASE_FILE")
if [[ ${#deb_assets[@]} -eq 0 ]]; then
  echo "Error: no .deb asset found in $RELEASE_FILE" >&2
  exit 1
fi

pool_dir="$APT_REPO_ROOT/pool/$APT_COMPONENT"
dist_component_dir="$APT_REPO_ROOT/dists/$APT_SUITE/$APT_COMPONENT"

rm -rf "$pool_dir" "$dist_component_dir"
mkdir -p "$pool_dir" "$dist_component_dir"

declare -A seen_arches=()
package_name=""

for asset_b64 in "${deb_assets[@]}"; do
  asset_json="$(echo "$asset_b64" | base64 --decode)"
  asset_name="$(echo "$asset_json" | jq -r '.name')"
  asset_url="$(echo "$asset_json" | jq -r '.browser_download_url')"

  target_deb="$pool_dir/$asset_name"
  echo "Downloading $asset_name"
  curl -fsSL "$asset_url" -o "$target_deb"

  current_arch="$(dpkg-deb -f "$target_deb" Architecture)"
  current_package="$(dpkg-deb -f "$target_deb" Package)"
  seen_arches["$current_arch"]=1

  if [[ -z "$package_name" ]]; then
    package_name="$current_package"
  fi

  asc_url="$(jq -r --arg n "${asset_name}.asc" '.assets[] | select(.name == $n) | .browser_download_url' "$RELEASE_FILE")"
  if [[ -n "$asc_url" ]]; then
    curl -fsSL "$asc_url" -o "${target_deb}.asc"
  fi
done

mapfile -t arches < <(printf "%s\n" "${!seen_arches[@]}" | sort)
if [[ ${#arches[@]} -eq 0 ]]; then
  echo "Error: no package architectures discovered from .deb files" >&2
  exit 1
fi

for arch in "${arches[@]}"; do
  mkdir -p "$dist_component_dir/binary-$arch"
done

all_packages_file="$(mktemp)"
(
  cd "$APT_REPO_ROOT"
  dpkg-scanpackages "pool/$APT_COMPONENT" /dev/null > "$all_packages_file"
)

for arch in "${arches[@]}"; do
  # Keep only entries matching the target arch (plus architecture-independent "all").
  awk -v target_arch="$arch" '
    BEGIN { RS=""; ORS="\n\n" }
    {
      keep = 0
      n = split($0, lines, "\n")
      for (i = 1; i <= n; i++) {
        if (lines[i] ~ /^Architecture:[[:space:]]*/) {
          arch = lines[i]
          sub(/^Architecture:[[:space:]]*/, "", arch)
          if (arch == target_arch || arch == "all") {
            keep = 1
          }
          break
        }
      }
      if (keep) {
        print $0
      }
    }
  ' "$all_packages_file" > "$dist_component_dir/binary-$arch/Packages"
  gzip -9c "$dist_component_dir/binary-$arch/Packages" > "$dist_component_dir/binary-$arch/Packages.gz"
done

rm -f "$all_packages_file"

release_dir="$APT_REPO_ROOT/dists/$APT_SUITE"
release_file="$release_dir/Release"
mapfile -t index_files < <(find "$release_dir/$APT_COMPONENT" -type f \( -name "Packages" -o -name "Packages.gz" \) | sort)

{
  echo "Origin: Bitcoin Safe"
  echo "Label: Bitcoin Safe"
  echo "Suite: $APT_SUITE"
  echo "Codename: $APT_SUITE"
  echo "Date: $(LC_ALL=C date -Ru)"
  echo "Architectures: ${arches[*]}"
  echo "Components: $APT_COMPONENT"
  echo "Description: Bitcoin Safe APT repository"
  echo "MD5Sum:"
  for abs_path in "${index_files[@]}"; do
    rel_path="${abs_path#"$release_dir"/}"
    md5_value="$(md5sum "$abs_path" | awk '{print $1}')"
    file_size="$(stat -c%s "$abs_path")"
    printf " %s %16s %s\n" "$md5_value" "$file_size" "$rel_path"
  done
  echo "SHA256:"
  for abs_path in "${index_files[@]}"; do
    rel_path="${abs_path#"$release_dir"/}"
    sha256_value="$(sha256sum "$abs_path" | awk '{print $1}')"
    file_size="$(stat -c%s "$abs_path")"
    printf " %s %16s %s\n" "$sha256_value" "$file_size" "$rel_path"
  done
} > "$release_file"

mkdir -p "$(dirname "$APT_DATA_FILE")"
signed_repo=false
source_line="deb [trusted=yes] $APT_REPO_URL $APT_SUITE $APT_COMPONENT"

if [[ -n "$APT_GPG_KEY_ID" ]]; then
  require_cmd gpg
  gpg --batch --yes --local-user "$APT_GPG_KEY_ID" --clearsign -o "$release_dir/InRelease" "$release_file"
  gpg --batch --yes --local-user "$APT_GPG_KEY_ID" --detach-sign -o "$release_dir/Release.gpg" "$release_file"
  gpg --batch --yes --output "$APT_REPO_ROOT/$APT_KEYRING_FILE" --export "$APT_GPG_KEY_ID"
  signed_repo=true
  source_line="deb [signed-by=$APT_KEYRING_PATH] $APT_REPO_URL $APT_SUITE $APT_COMPONENT"
else
  rm -f "$release_dir/InRelease" "$release_dir/Release.gpg"
fi

jq -n \
  --arg url "$APT_REPO_URL" \
  --arg suite "$APT_SUITE" \
  --arg component "$APT_COMPONENT" \
  --arg package "$package_name" \
  --arg source_line "$source_line" \
  --arg keyring_path "$APT_KEYRING_PATH" \
  --arg keyring_file "$APT_KEYRING_FILE" \
  --arg keyring_url "$APT_KEYRING_URL" \
  --argjson signed "$signed_repo" \
  '{
    url: $url,
    suite: $suite,
    component: $component,
    package: $package,
    signed: $signed,
    source_line: $source_line,
    keyring_path: $keyring_path,
    keyring_file: $keyring_file,
    keyring_url: $keyring_url
  }' > "$APT_DATA_FILE"

echo "APT repository metadata written to $APT_REPO_ROOT"
