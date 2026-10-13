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

ChatGPT takes a ZIP upload, and its MCP review needs a walkthrough video URL in `extensions.com.openai.review.demo_recording_url`. That URL stays out of this public repository: put it in `.chatgpt-review.local.json`, which git ignores:

```json
{"demo_recording_url": "https://..."}
```

Then build the ZIP from a committed ref:

```sh
python3 scripts/package-chatgpt.py
```

The script packages `HEAD` (or `--ref <branch or commit>`) and writes the URL only into the `plugin.json` inside `dist/transgull-<version>.zip`. `dist/` is ignored by git.
