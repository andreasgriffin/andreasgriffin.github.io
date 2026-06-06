#!/usr/bin/env python3

import argparse
import json
import re
import urllib.request
from pathlib import Path


HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "bitcoin-safe-website-release-fetcher",
}


def fetch_json(url: str):
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def parse_base_version(tag: str):
    match = re.match(r"^v?(\d+)\.(\d+)\.(\d+)", tag or "")
    if not match:
        return None
    return tuple(int(part) for part in match.groups())


def build_prerelease_payload(stable_release, all_releases):
    latest_prerelease = next(
        (
            release
            for release in all_releases
            if release.get("prerelease") and not release.get("draft")
        ),
        None,
    )

    stable_base = parse_base_version(stable_release.get("tag_name", ""))
    prerelease_base = (
        parse_base_version(latest_prerelease.get("tag_name", ""))
        if latest_prerelease
        else None
    )

    payload = {
        "newer_than_latest_stable": bool(
            stable_base is not None
            and prerelease_base is not None
            and prerelease_base > stable_base
        ),
    }

    if latest_prerelease:
        payload.update(
            {
                "name": latest_prerelease.get("name"),
                "tag_name": latest_prerelease.get("tag_name"),
                "html_url": latest_prerelease.get("html_url"),
                "published_at": latest_prerelease.get("published_at"),
                "prerelease": latest_prerelease.get("prerelease"),
            }
        )

    return payload


def write_json(path: str, payload):
    Path(path).write_text(json.dumps(payload, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stable-url", required=True)
    parser.add_argument("--releases-url", required=True)
    parser.add_argument("--prerelease-output", required=True)
    parser.add_argument("--stable-output")
    args = parser.parse_args()

    stable_release = fetch_json(args.stable_url)
    all_releases = fetch_json(args.releases_url)

    if args.stable_output:
        write_json(args.stable_output, stable_release)

    write_json(
        args.prerelease_output,
        build_prerelease_payload(stable_release, all_releases),
    )


if __name__ == "__main__":
    main()
