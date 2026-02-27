#!/usr/bin/env bash

set -euo pipefail

# Replace with your GitHub repository, e.g., "username/repository"
REPO="andreasgriffin/bitcoin-safe"
API_URL="https://api.github.com/repos/$REPO/releases/latest"
OUTPUT_FILE="data/latest_release.json"
APT_REPO_ROOT="${APT_REPO_ROOT:-static/apt}"
APT_SUITE="${APT_SUITE:-stable}"
APT_RELEASE_FILE="$APT_REPO_ROOT/dists/$APT_SUITE/Release"

mkdir -p "data"

tmp_file="$(mktemp)"
trap 'rm -f "$tmp_file"' EXIT

curl -fsSL "$API_URL" | jq '.' > "$tmp_file"

new_tag="$(jq -r '.tag_name // empty' "$tmp_file")"
if [[ -f "$OUTPUT_FILE" ]]; then
  old_tag="$(jq -r '.tag_name // empty' "$OUTPUT_FILE")"
else
  old_tag=""
fi

if [[ -n "$new_tag" && "$new_tag" == "$old_tag" ]]; then
  if [[ ! -s "$APT_RELEASE_FILE" ]]; then
    echo "Release tag unchanged ($new_tag), but APT repo is missing. Generating APT repo."
    ./update_apt_repo.sh
    exit 0
  fi

  echo "Release tag unchanged ($new_tag); skipping update."
  exit 2
fi

mv "$tmp_file" "$OUTPUT_FILE"

./update_readme.sh
./update_apt_repo.sh

exit 0
