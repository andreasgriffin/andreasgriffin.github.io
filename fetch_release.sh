#!/usr/bin/env bash

set -euo pipefail

# Replace with your GitHub repository, e.g., "username/repository"
REPO="andreasgriffin/bitcoin-safe"
API_URL="https://api.github.com/repos/$REPO/releases/latest"
OUTPUT_FILE="data/latest_release.json"

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
  echo "Release tag unchanged ($new_tag); skipping update."
  exit 2
fi

mv "$tmp_file" "$OUTPUT_FILE"

./update_readme.sh

exit 0
