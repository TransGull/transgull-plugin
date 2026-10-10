# Contributing

This repository packages the hosted TransGull MCP server for several AI clients. It contains manifests and documentation only; the server and its OAuth implementation live in the TransGull backend.

## Keep the manifests in sync

Each client reads its own manifest, so the same values appear in several files:

| Value | Files |
| --- | --- |
| `name` (`transgull`) and `version` | `plugin.json`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.cursor-plugin/plugin.json`, `gemini-extension.json` |
| `keywords` | `plugin.json`, `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json` |
| MCP endpoint `https://us2.transgull.com/mcp` | `mcp.json`, `.mcp.json`, `.cursor-plugin/plugin.json`, `gemini-extension.json` |

`scripts/check-manifests.py` fails when any of these drift apart, and CI runs it together with `claude plugin validate` on every push and pull request.

Gemini CLI and Cursor sign in with the OAuth client IDs `transgull-gemini-cli` and `transgull-cursor`. Both are pre-registered in the TransGull backend, so don't rename them here without changing the backend first.

## Release a new version

1. Update `version` in every manifest listed above.
2. Run the checks:

   ```sh
   python3 scripts/check-manifests.py
   claude plugin validate .
   ```

3. Merge to `main`.

## Build the ChatGPT package

ChatGPT takes a ZIP upload. From a committed checkout:

```sh
VERSION=$(python3 -c 'import json; print(json.load(open("plugin.json"))["version"])')
mkdir -p dist
git archive --format=zip --prefix=transgull/ --output="dist/transgull-$VERSION.zip" HEAD plugin.json mcp.json assets/icon.png LICENSE NOTICE TRADEMARKS.md README.md
```

`dist/` is ignored by git.
