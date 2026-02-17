#!/usr/bin/env bash

# The repository in the form "owner/repo"
REPO="andreasgriffin/bitcoin-safe"

# Endpoint to list all releases
PRE_RELEASES_API_URL="https://api.github.com/repos/$REPO/releases"

# Output file for the latest prerelease
PRERELEASE_OUTPUT_FILE="data/latest_release.json"

mkdir -p data

# Fetch all releases, select only those with "prerelease": true, pick the first (latest), and save to file
curl -s "$PRE_RELEASES_API_URL" \
  | jq '[ .[] | select(.prerelease == true) ] | first' \
  > "$PRERELEASE_OUTPUT_FILE"




./update_readme.sh