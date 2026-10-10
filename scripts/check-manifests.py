#!/usr/bin/env python3
"""Check that every client manifest uses the same name, version, keywords, and MCP endpoint.

Each host reads its own manifest, so the version and server URL are duplicated
across files. Run this before tagging a release; CI runs it on every push.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NAME = "transgull"

MANIFESTS = [
    "plugin.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".cursor-plugin/plugin.json",
    "gemini-extension.json",
]

# gemini-extension.json has no keywords field; the Gemini gallery uses GitHub topics.
KEYWORD_MANIFESTS = [
    "plugin.json",
    ".claude-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
]

MCP_FILES = {
    # path: (key holding the URL, expected transport type or None)
    "mcp.json": ("url", "streamable-http"),
    ".mcp.json": ("url", "http"),
    "gemini-extension.json": ("httpUrl", None),
}


def load(path):
    with open(ROOT / path, encoding="utf-8") as f:
        return json.load(f)


def main():
    errors = []

    versions = {}
    for path in MANIFESTS:
        data = load(path)
        if path.endswith("marketplace.json"):
            for entry in data["plugins"]:
                versions[f"{path} ({entry['name']})"] = entry.get("version")
                if entry["name"] != NAME:
                    errors.append(f"{path}: plugin name must be {NAME!r}, got {entry['name']!r}")
        else:
            versions[path] = data.get("version")
            if data.get("name") != NAME:
                errors.append(f"{path}: name must be {NAME!r}, got {data.get('name')!r}")

    if len(set(versions.values())) != 1:
        errors.append("version mismatch:")
        errors.extend(f"  {path}: {version}" for path, version in versions.items())

    keywords = {path: load(path).get("keywords") for path in KEYWORD_MANIFESTS}
    if len({tuple(k or ()) for k in keywords.values()}) != 1:
        errors.append("keywords mismatch:")
        errors.extend(f"  {path}: {k}" for path, k in keywords.items())

    urls = {}
    for path, (url_key, expected_type) in MCP_FILES.items():
        servers = load(path)["mcpServers"]
        if len(servers) != 1:
            errors.append(f"{path}: expected exactly one MCP server, found {len(servers)}")
        for name, server in servers.items():
            urls[f"{path} ({name})"] = server.get(url_key)
            if name != NAME:
                errors.append(f"{path}: MCP server key must be {NAME!r}, got {name!r}")
            if expected_type and server.get("type") != expected_type:
                errors.append(f"{path} ({name}): type must be {expected_type!r}, got {server.get('type')!r}")

    if len(set(urls.values())) != 1:
        errors.append("MCP URL mismatch:")
        errors.extend(f"  {path}: {url}" for path, url in urls.items())

    for url in set(urls.values()):
        if not str(url).startswith("https://"):
            errors.append(f"MCP URL must use https: {url}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"OK: version {next(iter(versions.values()))}, MCP URL {next(iter(urls.values()))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
