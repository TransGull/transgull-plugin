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

The tools can't read or summarize transcript text, stop a translation that is already running (end the meeting, or use the TransGull app), or take payments.

## Before you start

You need three things:

1. **A TransGull account.** Sign up at [transgull.com](https://transgull.com) if you don't have one.
2. **Enough balance.** Each translation uses your personal or workspace balance. You add balance on the TransGull website; the plugin never takes payments or handles payment details.
3. **A meeting link** for Zoom, Google Meet, or Microsoft Teams. For Zoom, copy the full invite link and keep the passcode part (`?pwd=`), or GullBot can't join.

## Install

### Claude (web and desktop)

1. Open **Settings → Connectors** and select **Add custom connector**.
2. Enter the name `TransGull` and the URL `https://us2.transgull.com/mcp`.
3. Keep the default options and select **Add**.
4. Sign in to TransGull, choose your personal or workspace space, and approve.

To install the full plugin instead, open **Customize → Plugins → Add marketplace**, enter `https://github.com/TransGull/transgull-plugin`, install **TransGull**, and connect it on the plugin's **Connectors** tab.

### ChatGPT

Open [TransGull in ChatGPT](https://chatgpt.com/plugins/plugin_asdk_app_6accba52d3f88191a65ae16ad6c2d95e), add it, and sign in to TransGull when prompted.

### Claude Code

```sh
claude plugin marketplace add TransGull/transgull-plugin
claude plugin install transgull@transgull
```

Then run `/mcp` in a session and sign in to TransGull.

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

## Your first translation

For example, to translate a Zoom meeting that's already underway between Japanese and English:

1. **Ask your assistant.** Type "Have GullBot join this meeting now and translate between Japanese and English", then paste the meeting link.
2. **Approve the action** if your assistant asks for permission.
3. **Admit GullBot.** It asks to join as **TransGull Interpreter**. If the meeting has a waiting room, the host needs to admit it.
4. **Open the viewing link.** GullBot posts a link in the meeting chat where participants follow the live translation. Your assistant shares the same link with you.

GullBot leaves on its own when the meeting ends. To book ahead, replace "now" with a time, such as "tomorrow at 3 PM".

## Things you can say

| To | Say something like |
| --- | --- |
| Translate a meeting now | "Have GullBot join this meeting now and translate between Chinese and English: (meeting link)" |
| Book ahead | "Schedule GullBot to join this Google Meet tomorrow at 3 PM Tokyo time, translating into Chinese, English, and Japanese: (meeting link)" |
| Handle several languages | "Detect each speaker's language automatically and translate into Chinese and English" |
| Check your bookings | "Which meeting translations do I have tomorrow?" |
| Get the viewing link | "Send me the viewing link for the weekly meeting translation" |
| Change the time | "Move the weekly meeting translation to 4 PM and keep everything else" |
| Cancel | "Cancel the weekly meeting translation; GullBot doesn't need to join" |

## Tips

- **Say the time zone** when you book, such as "Tokyo time", so GullBot joins at the right moment.
- **Admit GullBot** from the waiting room, or translation can't start.
- **Tell participants** that the meeting will be transcribed for translation. Meeting audio recordings are not retained.
- **Only bookings that haven't started** can be changed or cancelled.
- **To end a translation early,** end the meeting in Zoom, Google Meet, or Microsoft Teams; the translation ends with it. You can also stop it in the TransGull app. Your assistant can't remove GullBot once it has joined.
- **If your balance runs low,** your assistant tells you and shares a link to add balance on the TransGull website.

## Data and privacy

- **Where data goes:** all requests go to `https://us2.transgull.com/mcp`, operated by Say Wow, Inc. The plugin doesn't contact any other service.
- **What is sent:** the meeting link (including any passcode in it), the languages you choose, the scheduled time, and the IDs of translations you manage.
- **In the meeting:** GullBot joins as **TransGull Interpreter**, transcribes the conversation to produce the translation, and posts a viewing link in the meeting chat. Meeting audio recordings are not retained. Tell participants that the meeting will be transcribed.
- **Sign-in:** OAuth through TransGull. No API keys or passwords are stored in this repository or in your client configuration.

See the [privacy policy](https://transgull.com/about/privacy) for collection, use, and retention details.

## Support and policies

- [Website](https://transgull.com)
- [Support](https://transgull.com/about/contactus)
- [Privacy policy](https://transgull.com/about/privacy)
- [Terms of service](https://transgull.com/about/terms)
- [Security policy](SECURITY.md)

## License

Plugin configuration and documentation are licensed under [Apache-2.0](LICENSE). Logo artwork and trademarks have separate terms in [TRADEMARKS.md](TRADEMARKS.md). This license does not cover the hosted TransGull service or its backend implementation.
