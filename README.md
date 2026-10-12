# TransGull Plugin

**Translate online meetings**

Arrange real-time translation for Zoom, Google Meet, and Microsoft Teams with GullBot. TransGull supports 47 languages: tell your AI assistant which two or more languages you need and share your meeting link. GullBot can join now or at a scheduled time.

This repository is the official plugin package for Claude, ChatGPT, Cursor, Gemini CLI, and VS Code. Each client connects to the same hosted TransGull MCP server.

## What it does

After you sign in to TransGull, your assistant can use these tools:

| Tool | What it does |
| --- | --- |
| `create_meeting_translation` | Sends GullBot to a meeting now or at a scheduled time, with two-language or multilingual translation |
| `list_meeting_translations` | Lists your meeting translations for a date range |
| `get_meeting_translation` | Shows the status and viewing link of one translation |
| `update_meeting_translation` | Changes a scheduled translation, such as its start time |
| `cancel_meeting_translation` | Cancels a scheduled translation |

Example prompts:

- "Have GullBot join the Zoom meeting above now and translate between Japanese and Chinese."
- "Schedule GullBot for my Google Meet tomorrow at 3 PM Tokyo time, translating into Chinese, English, and Japanese."
- "Show my meeting translations for tomorrow and give me the viewing link for Review Teams."

The tools can't read or summarize transcript text, stop a translation that is already running (end it in the TransGull app), or take payments.

## Account and billing

A TransGull account with sufficient personal or workspace balance is required. Each translation consumes that balance. You add balance on the [TransGull website](https://transgull.com); the plugin never handles payment details.

## Data and privacy

- **Where data goes:** all requests go to `https://us2.transgull.com/mcp`, operated by Say Wow, Inc. The plugin doesn't contact any other service.
- **What is sent:** the meeting link (including any passcode in it), the languages you choose, the scheduled time, and the IDs of translations you manage.
- **In the meeting:** GullBot joins as **TransGull Interpreter**, transcribes the conversation to produce the translation, and posts a viewing link in the meeting chat. Meeting audio recordings are not retained. Tell participants that the meeting will be transcribed.
- **Sign-in:** OAuth through TransGull. No API keys or passwords are stored in this repository or in your client configuration.

See the [privacy policy](https://transgull.com/about/privacy) for collection, use, and retention details.

## Install

### Claude Code

```sh
claude plugin marketplace add TransGull/transgull-plugin
claude plugin install transgull@transgull
```

Then run `/mcp` in a session and sign in to TransGull.

### Claude (web and desktop)

Open **Customize → Plugins → Add marketplace**, enter `https://github.com/TransGull/transgull-plugin`, install **TransGull**, and connect it on the plugin's **Connectors** tab.

### ChatGPT

Once TransGull is listed in the ChatGPT apps directory, install it there and sign in when prompted.

### Gemini CLI

```sh
gemini extensions install https://github.com/TransGull/transgull-plugin
```

Then run `/mcp auth transgull` to sign in.

### Cursor

Install the TransGull plugin, or add the server to Cursor's `mcp.json` yourself. Cursor must send the TransGull client ID shown below:

```json
{
  "mcpServers": {
    "transgull": {
      "url": "https://us2.transgull.com/mcp",
      "auth": { "CLIENT_ID": "transgull-cursor" }
    }
  }
}
```

Then complete the TransGull OAuth sign-in when Cursor prompts you.

### VS Code and GitHub Copilot

```sh
code --add-mcp '{"name":"transgull","type":"http","url":"https://us2.transgull.com/mcp"}'
```

Then complete the TransGull OAuth sign-in when VS Code prompts you.

## Support and policies

- [Website](https://transgull.com)
- [Support](https://transgull.com/about/contactus)
- [Privacy policy](https://transgull.com/about/privacy)
- [Terms of service](https://transgull.com/about/terms)
- [Security policy](SECURITY.md)

## License

Plugin configuration and documentation are licensed under [Apache-2.0](LICENSE). Logo artwork and trademarks have separate terms in [TRADEMARKS.md](TRADEMARKS.md). This license does not cover the hosted TransGull service or its backend implementation.
