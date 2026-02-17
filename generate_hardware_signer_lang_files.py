#!/usr/bin/env python3
"""Generate per-language stub pages for hardware signer detail routes.

The script reads the default English `index.md` in each signer folder under
`content/knowledge/supported-hardware-signers/` and emits `index.<lang>.md`
for every language defined in `config/_default/languages.toml` (excluding the
default language set in `config/_default/config.toml`).

Only minimal front matter is written (title, signer, aliases). Page body is
copied from the base file so you can add real content later if desired.

Usage:
  python generate_hardware_signer_lang_files.py [--force] [--dry-run] [--verbose]

Options:
  --force    Overwrite existing language files.
  --dry-run  Show actions without writing files.
  --verbose  Print per-file actions.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import tomllib
import yaml


ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content" / "knowledge" / "supported-hardware-signers"
LANGS_FILE = ROOT / "config" / "_default" / "languages.toml"
CONFIG_FILE = ROOT / "config" / "_default" / "config.toml"


def load_languages() -> list[str]:
    data = tomllib.loads(LANGS_FILE.read_text(encoding="utf-8"))
    return list(data.keys())


def load_default_lang() -> str:
    cfg = tomllib.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    return cfg.get("defaultContentLanguage", "en")


def parse_front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} missing YAML front matter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{path} front matter not terminated")
    fm_text = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    meta = yaml.safe_load(fm_text) or {}
    return meta, body


def build_front_matter(meta: dict) -> str:
    yaml_text = yaml.safe_dump(meta, sort_keys=False, allow_unicode=False)
    return f"---\n{yaml_text}---\n\n"


def generate_for_signer(folder: Path, languages: list[str], default_lang: str, force: bool, dry_run: bool, verbose: bool) -> tuple[int, int]:
    base_file = folder / "index.md"
    if not base_file.exists():
        if verbose:
            print(f"[skip] {folder.name}: missing index.md")
        return 0, 0

    base_meta, body = parse_front_matter(base_file)
    created = updated = 0

    for lang in languages:
        if lang == default_lang:
            continue
        target = folder / f"index.{lang}.md"
        if target.exists() and not force:
            if verbose:
                print(f"[keep] {target}")
            continue

        meta = dict(base_meta)
        meta.setdefault("title", base_meta.get("title", folder.name))
        meta.setdefault("signer", base_meta.get("signer", folder.name))
        meta["aliases"] = [f"/{lang}/knowledge/supported-hardware-signers/{folder.name}/"]

        content = build_front_matter(meta) + body

        if dry_run:
            action = "would overwrite" if target.exists() else "would create"
            print(f"[{action}] {target}")
        else:
            target.write_text(content, encoding="utf-8")
            if target.exists() and force:
                updated += 1
            else:
                created += 1
            if verbose:
                verb = "updated" if target.exists() and force else "created"
                print(f"[{verb}] {target}")

    return created, updated


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate per-language signer stub pages")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    parser.add_argument("--verbose", action="store_true", help="Print per-file actions")
    args = parser.parse_args()

    languages = load_languages()
    default_lang = load_default_lang()

    total_created = total_updated = 0

    for entry in sorted(CONTENT_DIR.iterdir()):
        if not entry.is_dir() or entry.name.startswith("_"):
            continue
        created, updated = generate_for_signer(
            entry, languages, default_lang, args.force, args.dry_run, args.verbose
        )
        total_created += created
        total_updated += updated

    if args.dry_run:
        print("Dry run complete.")
    print(f"Created: {total_created}, Updated: {total_updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
