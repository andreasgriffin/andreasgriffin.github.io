#!/bin/bash
# URL for the raw README content from the GitHub repo
RAW_URL="https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/README.md"

# Target file to update
TARGET_FILE="content/features/readme/index.md"

# Marker after which the fetched content will replace the old content
MARKER="<!-- header-end -->"

# Fetch the content from the remote file using curl
remote_content=$(curl -sSL "$RAW_URL")
if [ -z "$remote_content" ]; then
  echo "Error: Failed to fetch content from $RAW_URL"
  exit 1
fi

# Convert relative markdown links to absolute links that point to raw GitHub images.
# This sed command finds markdown links starting with "docs/" and converts them to:
# (https://raw.githubusercontent.com/andreasgriffin/bitcoin-safe/main/docs/...)
remote_content=$(echo "$remote_content" | sed -E 's/\((docs\/[^)]+)\)/\(https:\/\/raw.githubusercontent.com\/andreasgriffin\/bitcoin-safe\/main\/\1\)/g')

# Ensure the target file exists
if [ ! -f "$TARGET_FILE" ]; then
  echo "Warning: Target file $TARGET_FILE does not exist. Creating it..."
  touch "$TARGET_FILE"
fi

# Check that the target file contains the marker
if ! grep -q "$MARKER" "$TARGET_FILE"; then
  echo "Error: Marker '$MARKER' not found in $TARGET_FILE."
  exit 1
fi

# Create a temporary file to build the updated content
temp_file=$(mktemp)

# Copy all lines up to and including the marker, discarding any content after the marker.
awk -v marker="$MARKER" '{
    print
    if($0 ~ marker) { exit }
}' "$TARGET_FILE" > "$temp_file"

# Append the fetched (and modified) content after the marker.
echo "$remote_content" >> "$temp_file"

# Replace the original target file with the updated content
mv "$temp_file" "$TARGET_FILE"

echo "Content from $RAW_URL has replaced the content after '$MARKER' in $TARGET_FILE."
