#!/usr/bin/env python3

# use it as python ../../../make_translated_md.py --input translations.txt  --outdir . --basename index   --overwrite





import argparse
from pathlib import Path
from typing import Dict, List
import re
import os

LANG_MAP = {
    # --- English ---
    "en": "en",
    "en-us": "en", "en-gb": "en", "en-au": "en", "en-ca": "en", "en-nz": "en",
    "en-ie": "en", "en-sg": "en", "en-in": "en", "en-hk": "en", "en-za": "en",

    # --- Germanic ---
    "de": "de",
    "de-de": "de", "de-at": "de", "de-ch": "de", "de-li": "de", "de-lu": "de",

    "nl": "nl",
    "nl-nl": "nl", "nl-be": "nl",

    "da": "da", "da-dk": "da",
    "sv": "sv", "sv-se": "sv",
    "no": "no", "nb": "no", "nn": "no", "no-no": "no",
    "is": "is", "is-is": "is",
    "fo": "fo", "fo-fo": "fo",

    # --- Romance ---
    "fr": "fr",
    "fr-fr": "fr", "fr-ca": "fr", "fr-ch": "fr", "fr-be": "fr", "fr-lu": "fr",

    "it": "it", "it-it": "it", "it-ch": "it",

    "es": "es",
    "es-es": "es", "es-mx": "es", "es-ar": "es", "es-co": "es", "es-pe": "es",
    "es-cl": "es", "es-uy": "es", "es-ec": "es", "es-gt": "es", "es-ve": "es",
    "es-us": "es", "es-bo": "es", "es-cr": "es", "es-do": "es", "es-ni": "es",
    "es-pa": "es", "es-pr": "es", "es-sv": "es", "es-hn": "es", "es-py": "es",

    "pt": "pt",
    "pt-pt": "pt", "pt-ao": "pt", "pt-mz": "pt", "pt-gw": "pt",
    # keep Brazilian distinct
    "pt-br": "pt-br",

    "ro": "ro", "ro-ro": "ro",
    "ca": "ca", "ca-es": "ca",
    "gl": "gl", "gl-es": "gl",
    "eu": "eu", "eu-es": "eu",
    "oc": "oc", "oc-fr": "oc",

    # --- Slavic / Baltic ---
    "ru": "ru", "ru-ru": "ru",
    "uk": "uk", "uk-ua": "uk",
    "be": "be", "be-by": "be",
    "bg": "bg", "bg-bg": "bg",
    "sr": "sr", "sr-rs": "sr", "sr-ba": "sr",
    "hr": "hr", "hr-hr": "hr",
    "bs": "bs", "bs-ba": "bs",
    "sl": "sl", "sl-si": "sl",
    "sk": "sk", "sk-sk": "sk",
    "cs": "cs", "cs-cz": "cs",
    "mk": "mk", "mk-mk": "mk",
    "pl": "pl", "pl-pl": "pl",
    "lt": "lt", "lt-lt": "lt",
    "lv": "lv", "lv-lv": "lv",
    "et": "et", "et-ee": "et",

    # --- Greek & Cyrillic others ---
    "el": "el", "el-gr": "el",
    "hy": "hy", "hy-am": "hy",
    "ka": "ka", "ka-ge": "ka",
    "kk": "kk", "kk-kz": "kk",
    "az": "az", "az-az": "az",

    # --- Uralic / Turkic ---
    "hu": "hu", "hu-hu": "hu",
    "fi": "fi", "fi-fi": "fi",
    "et": "et",
    "tr": "tr", "tr-tr": "tr",
    "tk": "tk", "tk-tm": "tk",
    "uz": "uz", "uz-uz": "uz",
    "kk-kz": "kk",
    "ky": "ky", "ky-kg": "ky",

    # --- Semitic / RTL ---
    "ar": "ar",
    "ar-sa": "ar", "ar-eg": "ar", "ar-ae": "ar", "ar-kw": "ar", "ar-qa": "ar",
    "ar-bh": "ar", "ar-om": "ar", "ar-jo": "ar", "ar-lb": "ar", "ar-ly": "ar",
    "ar-ma": "ar", "ar-dz": "ar", "ar-tn": "ar", "ar-iq": "ar", "ar-sy": "ar",
    "ar-ye": "ar", "ar-ps": "ar",

    "he": "he", "he-il": "he",  # Hebrew
    "fa": "fa", "fa-ir": "fa",  # Persian
    "ur": "ur", "ur-pk": "ur", "ur-in": "ur",
    "ps": "ps", "ps-af": "ps",

    # --- Indo-Aryan / Dravidian (India etc.) ---
    "hi": "hi", "hi-in": "hi",
    "bn": "bn", "bn-bd": "bn", "bn-in": "bn",
    "pa": "pa", "pa-in": "pa",
    "gu": "gu", "gu-in": "gu",
    "mr": "mr", "mr-in": "mr",
    "ne": "ne", "ne-np": "ne",
    "si": "si", "si-lk": "si",
    "ta": "ta", "ta-in": "ta", "ta-lk": "ta", "ta-sg": "ta", "ta-my": "ta",
    "te": "te", "te-in": "te",
    "kn": "kn", "kn-in": "kn",
    "ml": "ml", "ml-in": "ml",
    "or": "or", "or-in": "or",
    "as": "as", "as-in": "as",

    # --- East / Southeast Asia ---
    "zh": "zh",
    # Simplified Chinese → collapse to 'zh'
    "zh-cn": "zh", "zh-sg": "zh", "zh-hans": "zh",
    # Traditional variants kept distinct
    "zh-tw": "zh-tw", "zh-hk": "zh-hk", "zh-mo": "zh-hk", "zh-hant": "zh-tw",

    "ja": "ja", "ja-jp": "ja",
    "ko": "ko", "ko-kr": "ko",

    "th": "th", "th-th": "th",
    "lo": "lo", "lo-la": "lo",
    "km": "km", "km-kh": "km",
    "my": "my", "my-mm": "my",  # Burmese
    "vi": "vi", "vi-vn": "vi",
    "id": "id", "id-id": "id",
    "ms": "ms", "ms-my": "ms", "ms-bn": "ms",
    "tl": "fil", "tl-ph": "fil", "fil": "fil", "fil-ph": "fil",

    # --- Africa ---
    "sw": "sw", "sw-ke": "sw", "sw-tz": "sw",
    "am": "am", "am-et": "am",
    "om": "om", "om-et": "om",
    "ti": "ti", "ti-er": "ti", "ti-et": "ti",
    "ha": "ha", "ha-ng": "ha", "ha-gh": "ha",
    "yo": "yo", "yo-ng": "yo",
    "ig": "ig", "ig-ng": "ig",
    "af": "af", "af-za": "af",
    "zu": "zu", "zu-za": "zu",
    "xh": "xh", "xh-za": "xh",
    "st": "st", "st-za": "st",
    "tn": "tn", "tn-za": "tn",
    "ts": "ts", "ts-za": "ts",
    "rw": "rw", "rw-rw": "rw",

    # --- Other European ---
    "sq": "sq", "sq-al": "sq",
    "al": "sq",  # sometimes seen
    "mt": "mt", "mt-mt": "mt",
    "ga": "ga", "ga-ie": "ga",
    "cy": "cy", "cy-gb": "cy",
    "br": "br", "br-fr": "br",  # Breton
    "kv": "ru",  # Komi (rare) -> fallback to ru if desired
    "rm": "rm", "rm-ch": "rm",  # Romansh

    # --- Others commonly seen ---
    "kk-kz": "kk",
    "mn": "mn", "mn-mn": "mn",
    "ta-in": "ta", "ta-lk": "ta",
    "ka-ge": "ka",
    "az-az": "az",
    "kk": "kk",
    "uz-uz": "uz",
}


# Support both formats:
#   # LANG:de_DE
#   //de_DE
HEADER_PATTERNS = [
    re.compile(r'^\s*#\s*LANG\s*:\s*([A-Za-z]{2,3}(?:[_-][A-Za-z]{2,3})?)\s*$',
               re.IGNORECASE),
    re.compile(r'^\s*//\s*([A-Za-z]{2,3}(?:[_-][A-Za-z]{2,3})?)\s*$'),
]

def normalize_lang(code: str) -> str:
    key = code.strip().lower().replace("_", "-")
    if key in LANG_MAP:
        return LANG_MAP[key]
    if "-" in key:
        return key
    return key[:2]

def parse_llm_output(text: str) -> Dict[str, str]:
    sections: Dict[str, List[str]] = {}
    current_lang = ""

    def match_header(line: str):
        for pat in HEADER_PATTERNS:
            m = pat.match(line)
            if m:
                return m.group(1)
        return None

    for line in text.splitlines(keepends=True):
        hdr = match_header(line)
        if hdr:
            current_lang = normalize_lang(hdr)
            sections[current_lang] = []
        else:
            if current_lang:
                sections[current_lang].append(line)

    return {lang: "".join(lines).lstrip("\n").rstrip() + "\n"
            for lang, lines in sections.items()}

def main():
    ap = argparse.ArgumentParser(
        description="Create Hugo i18n Markdown files from LLM output (# LANG:xx_XX blocks)."
    )
    ap.add_argument("-i", "--input", required=True, help="LLM output text file")
    ap.add_argument("-o", "--outdir", required=True, help="Target bundle dir (e.g., content/features/usps)")
    ap.add_argument("-b", "--basename", default="index", help='Base filename (default: "index")')
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    ap.add_argument("--llminstructions", action="store_true", help="Show llm instructions")
    args = ap.parse_args()
    
    if args.llminstructions:
        print("""
The task is to translate a hugo md file into the languages [es_ES, it_IT].

Do not translate:  header tags, header images, hugo syntax like {{< page-title >}} , filenames or links

Do translate: 
 - header aliases
 - header title
 - header description
 - header keywords
 - the visible page content  (that includes the code signing policy)

Please return a single downloadable txt file (named translations.txt )  with the content:

# LANG:de_DE    
...de md content...

# LANG:it_IT     
...it md content...



The hugo file to be translated is:

              
              """)
        return

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    text = Path(args.input).read_text(encoding="utf-8")
    blocks = parse_llm_output(text)
    if not blocks:
        raise SystemExit("No language blocks found. Expected lines like: # LANG:de_DE")

    created, skipped = [], []
    for lang, content in blocks.items():
        target = outdir / f"{args.basename}.{lang}.md"
        if target.exists() and not args.overwrite:
            skipped.append(str(target))
            continue
        target.write_text(content, encoding="utf-8")
        created.append(str(target))

    print(f"Created: {len(created)}")
    for p in created: print("  +", p)
    if skipped:
        print(f"Skipped (exists): {len(skipped)}")
        for p in skipped: print("  -", p)

if __name__ == "__main__":
    main()