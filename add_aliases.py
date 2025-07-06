#!/usr/bin/env python3
import os

CONTENT_DIR = "content"

def has_alias_block(frontmatter_lines):
    for line in frontmatter_lines:
        if line.strip().startswith("aliases:"):
            return True
    return False

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) < 2 or lines[0].strip() != "---":
        # no YAML front-matter
        return False

    # find the closing '---'
    end_idx = None
    for i, ln in enumerate(lines[1:], start=1):
        if ln.strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        # malformed front-matter
        return False

    # if front-matter already has aliases, skip
    if has_alias_block(lines[1:end_idx]):
        return False

    # Compute the URL path:
    rel = os.path.relpath(path, CONTENT_DIR).replace(os.sep, "/")
    # strip .md
    rel_no_ext = rel.rsplit(".md", 1)[0]

    # if it's an index.md, drop the trailing '/index'
    if rel_no_ext.endswith("/index"):
        rel_no_ext = rel_no_ext[: -len("/index")]

    # ensure trailing slash
    alias_url = "/" + rel_no_ext.strip("/") + "/"

    # rebuild file with alias block just under the first ---
    new_lines = []
    new_lines.append(lines[0])  # '---\n'
    new_lines.append("aliases:\n")
    new_lines.append(f'  - "{alias_url}"\n')
    new_lines.extend(lines[1:])

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"  ↪ added alias {alias_url} to {path}")
    return True

def main():
    any_changed = False
    for root, _, files in os.walk(CONTENT_DIR):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            name = fn[:-3]
            # skip language‐tagged files
            if "." in name:
                continue
            full = os.path.join(root, fn)
            if process_file(full):
                any_changed = True

    if any_changed:
        print("Run `git add` on the modified files to include their new aliases.")
        exit(1)  # abort commit so you can review

if __name__ == "__main__":
    main()
