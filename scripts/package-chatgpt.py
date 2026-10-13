#!/usr/bin/env python3
"""Build the ChatGPT plugin ZIP from a committed ref.

The review walkthrough video must reach OpenAI but stay out of this public
repository, so its URL lives in the git-ignored .chatgpt-review.local.json
({"demo_recording_url": "https://..."}) and is written only into the
plugin.json inside the ZIP.

Usage: python3 scripts/package-chatgpt.py [--ref REF]
"""

import argparse
import io
import json
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCAL_REVIEW_FILE = ROOT / ".chatgpt-review.local.json"
PREFIX = "transgull/"
PACKAGE_FILES = [
    "plugin.json",
    "mcp.json",
    "assets/icon.png",
    "LICENSE",
    "NOTICE",
    "TRADEMARKS.md",
    "README.md",
]


def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True).stdout


def demo_recording_url() -> str:
    try:
        url = json.loads(LOCAL_REVIEW_FILE.read_text(encoding="utf-8"))["demo_recording_url"]
    except FileNotFoundError:
        sys.exit(f"missing {LOCAL_REVIEW_FILE.name}: create it with {{\"demo_recording_url\": \"https://...\"}}")
    except (KeyError, ValueError):
        sys.exit(f"{LOCAL_REVIEW_FILE.name} must be a JSON object with a demo_recording_url string")
    if not isinstance(url, str) or not url.startswith("https://"):
        sys.exit("demo_recording_url must be an https:// URL")
    return url


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ref", default="HEAD", help="committed ref to package (default: HEAD)")
    args = parser.parse_args()

    url = demo_recording_url()
    manifest = json.loads(git("show", f"{args.ref}:plugin.json"))
    manifest["extensions"]["com.openai"]["review"]["demo_recording_url"] = url
    version = manifest["version"]

    archive = git("archive", "--format=zip", f"--prefix={PREFIX}", args.ref, *PACKAGE_FILES)
    output = ROOT / "dist" / f"transgull-{version}.zip"
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(archive)) as source, zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as target:
        for item in source.infolist():
            data = source.read(item)
            if item.filename == PREFIX + "plugin.json":
                data = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
            target.writestr(item, data)

    commit = git("rev-parse", "--short", args.ref).decode().strip()
    print(f"OK: {output.relative_to(ROOT)} from {args.ref} ({commit}), version {version}, demo recording included")
    return 0


if __name__ == "__main__":
    sys.exit(main())
