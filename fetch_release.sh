#!/usr/bin/env bash

set -euo pipefail

REPO="andreasgriffin/bitcoin-safe"
STABLE_API_URL="https://api.github.com/repos/$REPO/releases/latest"
RELEASES_API_URL="https://api.github.com/repos/$REPO/releases?per_page=20"
OUTPUT_FILE="data/latest_release.json"
PRERELEASE_OUTPUT_FILE="data/latest_prerelease.json"

mkdir -p "data"

tmp_release_file="$(mktemp)"
tmp_prerelease_file="$(mktemp)"
trap 'rm -f "$tmp_release_file" "$tmp_prerelease_file"' EXIT

python3 ./fetch_release_data.py \
  --stable-url "$STABLE_API_URL" \
  --releases-url "$RELEASES_API_URL" \
  --stable-output "$tmp_release_file" \
  --prerelease-output "$tmp_prerelease_file"

stable_tag() {
  python3 - "$1" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
if not path.exists():
    print("")
else:
    data = json.loads(path.read_text())
    print(data.get("tag_name", ""))
PY
}

prerelease_state() {
  python3 - "$1" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
if not path.exists():
    print("")
else:
    data = json.loads(path.read_text())
    print("|".join([
        data.get("tag_name", ""),
        str(bool(data.get("newer_than_latest_stable"))).lower(),
    ]))
PY
}

stable_changed=0
prerelease_changed=0

if [[ "$(stable_tag "$tmp_release_file")" != "$(stable_tag "$OUTPUT_FILE")" ]]; then
  mv "$tmp_release_file" "$OUTPUT_FILE"
  stable_changed=1
fi

if [[ "$(prerelease_state "$tmp_prerelease_file")" != "$(prerelease_state "$PRERELEASE_OUTPUT_FILE")" ]]; then
  mv "$tmp_prerelease_file" "$PRERELEASE_OUTPUT_FILE"
  prerelease_changed=1
fi

if [[ "$stable_changed" -eq 0 && "$prerelease_changed" -eq 0 ]]; then
  echo "Release data unchanged; skipping update."
  exit 2
fi

if [[ "$stable_changed" -eq 1 ]]; then
  ./update_readme.sh
fi

exit 0
