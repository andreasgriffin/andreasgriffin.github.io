#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import time
import json
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple, Callable, Any, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

# ----------- Instruction templates -----------

DEFAULT_INSTRUCTION_MD = """You are a professional localization assistant for Hugo websites.

Goal: Translate the following Hugo Markdown file into the target language ({language_code}).
Output a complete Hugo Markdown file suitable to be saved as "index.{short_code}.md".

Do NOT translate:
- Header tags/keys (the YAML/TOML front matter field names like `title`, `description`, `aliases`, `tags`, `images`, etc.)
- Header images or filenames
- Hugo shortcodes and templating (e.g., {{< ... >}}, {{% ... %}}, {{ ref "..." }})
- URLs, filenames, or fragment anchors inside links

DO translate:
- The values of these front matter fields: aliases, title, description, keywords (values only, keep the keys and structure)
- All visible page content (headings, paragraphs, lists, callouts, notes)
- Any UI strings within the content

Strictly follow:
- Preserve original structure, spacing, and Hugo shortcodes as-is.
- Keep the same front matter format and keys; only translate the values where appropriate.
- Return ONLY the full translated Markdown file content. No explanations, no code fences, no extra commentary.

Remember the target language is {language_code}
"""

DEFAULT_INSTRUCTION_HTML = """You are a professional localization assistant for websites.

Goal: Translate the following HTML file into the target language ({language_code}).

VERY IMPORTANT — Do NOT modify:
- HTML tags, tags, tag names, structure, attributes, classes, ids, data-* attributes
- Embedded code, inline scripts, or event handlers
- URLs, link targets (href/src), filenames, anchors, image paths
- Hugo shortcodes or template braces if present

Translate ONLY visible human-readable text nodes.
Preserve whitespace and indentation as much as possible.
Return ONLY the full translated HTML. No explanations, no code fences, no extra commentary.

Remember the target language is {language_code}
"""

DEFAULT_INSTRUCTION_TOML = """You are a professional localization assistant for Hugo configuration files written in TOML.

Goal: Translate the following TOML into the target language ({language_code}).

Do NOT modify:
- Keys, table names, or arrays-of-tables structure ([[...]]) 
- Numbers, booleans, dates
- Routing/identifier fields: url, pageRef, rel, identifier, parent, weight, slug, target, href, path, icon
- Inline HTML, shortcodes, or code
- Quoting style and escaping

Translate ONLY human-visible string values for common UI keys when present:
- name, title, label, description, ariaLabel, tooltip, placeholder
- Inside [params] tables, translate ONLY: name, title, label, description, ariaLabel, placeholder

Preserve whitespace/indentation/order. 
Return ONLY the full TOML content. No explanations, no code fences, no extra commentary.

Remember the target language is {language_code}
"""

DEFAULT_INSTRUCTION_TOML_MENUS = """You are a professional localization assistant for Hugo MENU files (TOML).

Goal: Translate the following Hugo menus TOML into the target language ({language_code}). 
Typical sections are [[main]], [[footer]], etc.

STRICTLY do NOT modify:
- Keys, table names, arrays-of-tables ([[main]], [[footer]], etc.)
- Non-string values (numbers, booleans)
- Routing/identifier fields: url, pageRef, rel, identifier, parent, weight, slug, target, href, path, icon, pre, post
- Quoting style, escaping, indentation, or ordering

Translate ONLY these string values when present:
- name, title, label, description, ariaLabel
- Inside params tables, only: name, title, label, description, ariaLabel

Leave url/identifier/weight/parent/pageRef/target/slug/href/icon/pre/post unchanged.

Return ONLY the full TOML. No explanations, no code fences, no extra commentary.

Remember the target language is {language_code}
"""



# ----------- Utilities -----------

CODE_FENCE_RE = re.compile(r"^\s*```(?:\w+)?\s*|\s*```\s*$", re.MULTILINE)

def is_menus_toml(path: Path) -> bool:
    p = str(path).replace("\\", "/").lower()
    name = path.name.lower()
    return ("/config/_default/menus/" in p) or (name.startswith("menus.") and name.endswith(".toml"))


def strip_code_fences(text: str) -> str:
    return CODE_FENCE_RE.sub("", text).strip()

def clean_translation(text: str) -> str:
    """
    Post-process model output:
      - remove helper markers
      - remove entire aliases: section (the 'aliases:' line and all following '  - ' lines)
    """
    # Helper markers added in prompt
    for m in ("===== ORIGINAL MARKDOWN START =====", "===== ORIGINAL MARKDOWN END ====="):
        text = text.replace(m, "")

    lines = text.splitlines()
    cleaned_lines = []
    skip_alias_block = False

    for line in lines:
        if line.strip().startswith("aliases:"):
            # Keep your current behavior of stripping aliases entirely.
            skip_alias_block = True
            continue
        if skip_alias_block:
            if line.startswith("  - "):
                continue
            else:
                skip_alias_block = False
        cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()

def openai_chat_completion(api_base: str, api_key: Optional[str], model: str,
                           system_prompt: str, user_prompt: str,
                           temperature: float = 0.2, max_tokens: Optional[int] = None,
                           timeout: int = 10000) -> str:
    url = api_base.rstrip("/") + "/chat/completions"
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    payload: Dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
    }
    if max_tokens:
        payload["max_tokens"] = max_tokens

    resp = requests.post(url, headers=headers, data=json.dumps(payload), timeout=timeout)
    if resp.status_code != 200:
        raise RuntimeError(f"API error {resp.status_code}: {resp.text}")

    data = resp.json()
    return data["choices"][0]["message"]["content"]

def build_prompt(language_code: str, short_code: str, content: str, instruction_template: str) -> str:
    return instruction_template.format(
        language_code=language_code,
        short_code=short_code,
    ) + "\n\n===== ORIGINAL MARKDOWN START =====\n" + content + "\n===== ORIGINAL MARKDOWN END =====\n"

def find_index_md_files(base_dir: Path) -> List[Path]:
    return [p for p in base_dir.rglob("index.md") if p.is_file()]

def normalize_languages(raw_tokens: List[str]) -> List[str]:
    """
    Accepts:
      - ["fr_FR", "ko_KR", "de_DE"]
      - ["'fr_FR',", "'ko_KR',", "'de_DE'"]
      - ["'fr_FR',", "'ko_KR',", "de_DE"]
      - ["'fr_FR',", "'ko_KR',", "'de_DE',", ""]
      - ["'fr_FR', 'ko_KR', 'de_DE'"]
    Returns clean list like ["fr_FR", "ko_KR", "de_DE"]
    """
    joined = " ".join(raw_tokens)
    parts = [p.strip().strip("\"'") for p in joined.split(",")]
    out = []
    for p in parts:
        if not p:
            continue
        p = re.sub(r"\s+", "", p)
        if "_" in p:
            out.append(p)
        else:
            out.append(p)
    return out

# ----------- Filename helpers for additional files -----------

_LANG_DOT_RE = re.compile(r"\.([a-z]{2})\.(?=[^.]+$)", re.IGNORECASE)
def compute_translated_filename(src: Path, short_code: str) -> Path:
    """
    For 'features.en.html' -> replace '.en.' with '.<short_code>.'.
    If no '.xx.' segment exists, insert before extension: 'features.html' -> 'features.<short_code>.html'
    """
    name = src.name
    match = _LANG_DOT_RE.search(name)
    if match:
        new_name = name[:match.start()+1] + short_code + name[match.end()-1:]
    else:
        stem = src.stem
        suffix = "".join(src.suffixes)
        if len(src.suffixes) >= 1:
            base = name[: -len(suffix)]
            new_name = f"{base}{short_code}{suffix}"
            if not base.endswith("."):
                new_name = f"{base.rstrip('.')}.{short_code}{suffix}"
        else:
            new_name = f"{stem}.{short_code}"
    return src.with_name(new_name)

# ----------- Translation workers -----------

def translate_markdown_index(index_md_path: Path, lang_code: str, api_base: str, api_key: Optional[str],
                             model: str, sleep_seconds: float, overwrite: bool, instruction_template: str,
                             retries: int, retry_backoff: float) -> None:
    folder = index_md_path.parent
    short_code = lang_code.split("_")[0].lower()
    out_path = folder / f"index.{short_code}.md"

    if out_path.exists() and not overwrite:
        print(f"↷  Skip existing {out_path}")
        return

    text = index_md_path.read_text(encoding="utf-8")
    user_prompt = build_prompt(lang_code, short_code, text, instruction_template)

    print(f"→ Translating {index_md_path} -> {out_path.name} [{lang_code}] ...")
    attempt = 0
    while True:
        attempt += 1
        try:
            raw = openai_chat_completion(
                api_base=api_base,
                api_key=api_key,
                model=model,
                system_prompt="You are a careful, precise localization assistant for Hugo static sites.",
                user_prompt=user_prompt,
            )
            translated = strip_code_fences(raw)
            translated = clean_translation(translated)

            if not translated or len(translated) < 10:
                raise RuntimeError("Model returned too little content")

            out_path.write_text(translated, encoding="utf-8")
            print(f"✓ Wrote {out_path}")
            break
        except Exception as e:
            if attempt <= retries:
                wait = retry_backoff * attempt
                print(f"⚠️  Attempt {attempt}/{retries} failed: {e}, retrying in {wait}s ...")
                time.sleep(wait)
            else:
                print(f"❌ Failed after {retries} retries for {lang_code}: {e}", file=sys.stderr)
                break

    # Optional pacing (consider --sleep 0 when using --workers > 1)
    time.sleep(sleep_seconds)

def translate_additional_file(src_path: Path, lang_code: str, api_base: str, api_key: Optional[str],
                              model: str, sleep_seconds: float, overwrite: bool,
                              instruction_template: str, retries: int, retry_backoff: float) -> None:
    short_code = lang_code.split("_")[0].lower()
    out_path = compute_translated_filename(src_path, short_code)

    if not src_path.exists():
        print(f"!! Additional file not found: {src_path}", file=sys.stderr)
        return

    if out_path.exists() and not overwrite:
        print(f"↷  Skip existing {out_path}")
        return

    text = src_path.read_text(encoding="utf-8")
    user_prompt = build_prompt(lang_code, short_code, text, instruction_template)

    print(f"→ Translating {src_path} -> {out_path.name} [{lang_code}] ...")
    attempt = 0
    while True:
        attempt += 1
        try:
            raw = openai_chat_completion(
                api_base=api_base,
                api_key=api_key,
                model=model,
                system_prompt="You are a careful, precise localization assistant for websites.",
                user_prompt=user_prompt,
            )
            translated = strip_code_fences(raw)
            translated = clean_translation(translated)

            if not translated or len(translated) < 5:
                raise RuntimeError("Model returned too little content")

            out_path.write_text(translated, encoding="utf-8")
            print(f"✓ Wrote {out_path}")
            break
        except Exception as e:
            if attempt <= retries:
                wait = retry_backoff * attempt
                print(f"⚠️  Attempt {attempt}/{retries} failed: {e}, retrying in {wait}s ...")
                time.sleep(wait)
            else:
                print(f"❌ Failed after {retries} retries for {lang_code}: {e}", file=sys.stderr)
                break

    time.sleep(sleep_seconds)

# ----------- Task runner -----------

Task = Tuple[Callable[..., Any], tuple, dict]

def run_tasks(tasks: List[Task], workers: int) -> None:
    """
    Execute tasks sequentially (workers=1) or in parallel with a thread pool (workers>1).
    Each task is a tuple: (callable, args_tuple, kwargs_dict)
    """
    if not tasks:
        return

    if workers <= 1:
        for fn, args, kwargs in tasks:
            fn(*args, **kwargs)
        return

    # Parallel
    print(f"\nRunning {len(tasks)} tasks with {workers} workers...\n")
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(fn, *args, **kwargs) for fn, args, kwargs in tasks]
        # Iterate as they complete (optional: could show progress)
        for _ in as_completed(futures):
            pass

# ----------- Main -----------
def main():
    parser = argparse.ArgumentParser(description="Recursive Hugo translator (sequential or parallel).")
    parser.add_argument("--base-dir", type=str, default=None,
                        help="Root content directory to scan for content/**/index.md. If omitted, no directory scan is done.")
    parser.add_argument("--languages", nargs="+", required=True,
                        help="Languages as space-separated tokens or one comma-separated string. "
                             "Examples: --languages fr_FR de_DE  OR  --languages \"'fr_FR', 'de_DE'\"")
    parser.add_argument("--api-base", type=str, default=os.environ.get("OPENAI_API_BASE", "http://localhost:3000/v1"))
    parser.add_argument("--api-key", type=str, default=os.environ.get("OPENAI_API_KEY"))
    parser.add_argument("--model", type=str, default=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"))
    parser.add_argument("--sleep", type=float, default=0,
                        help="Seconds to sleep after each task (use 0 when parallelizing heavily).")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--retry-backoff", type=float, default=2.0)
    parser.add_argument("--instruction-file-md", type=str, default=None)
    parser.add_argument("--instruction-file-html", type=str, default=None)
    parser.add_argument("--additional-files", nargs="*", default=[],
                        help="Specific files to translate (one comma-separated string).")
    parser.add_argument("--workers", type=int, default=1,
                        help="Parallel worker threads. 1 = sequential (default). >1 enables parallel HTTP calls.")
    parser.add_argument("--instruction-file-toml", type=str, default=None)
    parser.add_argument("--instruction-file-toml-menus", type=str, default=None)

    args = parser.parse_args()

    # Load instruction templates
    if args.instruction_file_md:
        try:
            instruction_md = Path(args.instruction_file_md).read_text(encoding="utf-8")
        except Exception as e:
            print(f"Failed to read Markdown instruction template, fallback to default: {e}", file=sys.stderr)
            instruction_md = DEFAULT_INSTRUCTION_MD
    else:
        instruction_md = DEFAULT_INSTRUCTION_MD

    if args.instruction_file_html:
        try:
            instruction_html = Path(args.instruction_file_html).read_text(encoding="utf-8")
        except Exception as e:
            print(f"Failed to read HTML instruction template, fallback to default: {e}", file=sys.stderr)
            instruction_html = DEFAULT_INSTRUCTION_HTML
    else:
        instruction_html = DEFAULT_INSTRUCTION_HTML

    if args.instruction_file_toml:
        try:
            instruction_toml = Path(args.instruction_file_toml).read_text(encoding="utf-8")
        except Exception as e:
            print(f"Failed to read TOML instruction template, fallback to default: {e}", file=sys.stderr)
            instruction_toml = DEFAULT_INSTRUCTION_TOML
    else:
        instruction_toml = DEFAULT_INSTRUCTION_TOML

    if args.instruction_file_toml_menus:
        try:
            instruction_toml_menus = Path(args.instruction_file_toml_menus).read_text(encoding="utf-8")
        except Exception as e:
            print(f"Failed to read TOML MENUS instruction template, fallback to default: {e}", file=sys.stderr)
            instruction_toml_menus = DEFAULT_INSTRUCTION_TOML_MENUS
    else:
        instruction_toml_menus = DEFAULT_INSTRUCTION_TOML_MENUS


    # Normalize inputs
    languages = normalize_languages(args.languages)
    if not languages:
        print("No languages parsed from --languages.", file=sys.stderr)
        sys.exit(2)

    additional_files = normalize_languages(args.additional_files) if args.additional_files else []
    additional_paths = [Path(p).resolve() for p in additional_files]

    print(f"Languages: {languages}")
    if additional_paths:
        print(f"Additional files: {additional_paths}")

    tasks: List[Task] = []

    # Only scan base-dir if explicitly given
    if args.base_dir:
        base_dir = Path(args.base_dir).resolve()
        if base_dir.exists():
            index_files = find_index_md_files(base_dir)
            print(f"Found {len(index_files)} index.md files under {base_dir}")
            for idx, md in enumerate(sorted(index_files), 1):
                print(f"[{idx}/{len(index_files)}] queueing {md.relative_to(base_dir)}")
                for lang_code in languages:
                    tasks.append((
                        translate_markdown_index,
                        (md, lang_code, args.api_base, args.api_key, args.model,
                         args.sleep, args.overwrite, instruction_md, args.retries, args.retry_backoff),
                        {}
                    ))
        else:
            print(f"(Info) Base directory not found: {base_dir} — skipping content tree scan.")

    # Process additional files
    if additional_paths:
        print("\nQueueing additional files...")
        for src in additional_paths:
            ext = "".join(src.suffixes).lower()
            if ext.endswith(".html") or ext.endswith(".htm"):
                instr = instruction_html
            elif ext.endswith(".toml"):
                instr = instruction_toml_menus if is_menus_toml(src) else instruction_toml
            else:
                instr = instruction_md
            for lang_code in languages:
                tasks.append((
                    translate_additional_file,
                    (src, lang_code, args.api_base, args.api_key, args.model,
                     args.sleep, args.overwrite, instr, args.retries, args.retry_backoff),
                    {}
                ))

    # Run tasks (sequential by default, parallel if --workers > 1)
    run_tasks(tasks, workers=max(1, args.workers))

    print("\nDone.")

if __name__ == "__main__":
    main()
