# Security policy

## Reporting a vulnerability

**Please don't open a public GitHub issue for a security problem.** Public issues are visible to everyone and can put users at risk before a fix is ready.

Report it privately by email to [security@transgull.com](mailto:security@transgull.com). A good report includes:

- What you found and why you think it's a security issue
- Steps to reproduce, or a proof of concept
- The affected component: a file in this repository, a client manifest, or the hosted endpoint
- The impact you think it could have

We will acknowledge your report, investigate it, and keep you informed while we work on a fix. Please give us a reasonable chance to ship that fix before sharing details publicly.

## What this repository covers

This repository holds only the public client pieces of the TransGull integration: documentation and the plugin manifests for Claude, ChatGPT, Cursor, and Gemini CLI (`plugin.json`, `mcp.json`, `.mcp.json`, `.claude-plugin/`, `.cursor-plugin/`, `gemini-extension.json`). It contains no server code and no credentials.

The MCP server is a hosted service at `us2.transgull.com`, operated by Say Wow, Inc. Report problems with the hosted service, its OAuth sign-in, or the TransGull website through the same channel above. There is nothing to patch on your side; clients always connect to the current hosted endpoint.

## Using TransGull safely

- Connect only through the official endpoint `https://us2.transgull.com/mcp` and sign in on the TransGull OAuth page.
- Review what the assistant is about to do before it creates, changes, or cancels a translation, because these actions use your account balance.
