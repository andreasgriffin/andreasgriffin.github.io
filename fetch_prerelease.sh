#!/usr/bin/env bash

set -euo pipefail

REPO="andreasgriffin/bitcoin-safe"
STABLE_API_URL="https://api.github.com/repos/$REPO/releases/latest"
PRE_RELEASES_API_URL="https://api.github.com/repos/$REPO/releases"
PRERELEASE_OUTPUT_FILE="data/latest_prerelease.json"

mkdir -p data

python3 ./fetch_release_data.py \
  --stable-url "$STABLE_API_URL" \
  --releases-url "$PRE_RELEASES_API_URL" \
  --prerelease-output "$PRERELEASE_OUTPUT_FILE"
