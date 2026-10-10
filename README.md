# TransGull Plugin

**Translate online meetings**

Arrange real-time translation for Zoom, Google Meet, and Microsoft Teams with GullBot. TransGull supports 47 languages: tell ChatGPT which two or more languages you need and share your meeting link. GullBot can join now or at a scheduled time.

A TransGull account with sufficient personal or workspace balance is required. Translation consumes that balance; recharge on the [TransGull website](https://transgull.com). Meeting audio recordings are not retained.

## Connection

- Remote MCP endpoint: `https://us2.transgull.com/mcp`
- Transport: Streamable HTTP
- Authentication: OAuth through the client authorization flow

For clients supporting remote MCP, add the endpoint above and complete the TransGull OAuth sign-in. This repository does not contain credentials or an MCP server implementation. Available tools and their parameter descriptions are provided by the remote server.

## Package contents

- `plugin.json`: plugin metadata, English listing, 13 localized listings, conversation starters, and review scenarios.
- `mcp.json`: remote MCP connection configuration.
- `assets/icon.png`: 1024 × 1024 product icon.
- `LICENSE`, `NOTICE`, `TRADEMARKS.md`: license and brand asset terms.

The existing internal plugin identifier `transgull-test` is preserved. The current `0.2.0` package is a review draft; inclusion of review scenarios does not mean they have passed production testing or marketplace review. This repository is the maintained source for subsequent package changes.

## Create a package

From a committed checkout, create a ZIP containing the plugin files and license notices:

```sh
mkdir -p dist
git archive --format=zip --prefix=transgull-test/ --output=dist/transgull-test-0.2.0.zip HEAD plugin.json mcp.json assets/icon.png LICENSE NOTICE TRADEMARKS.md README.md
```

Before submission, verify the production OAuth connection and meeting workflows, complete review evidence, and check the target marketplace's current packaging requirements. This bundle has not been adapted or validated as a Claude-specific plugin package.

## Support and policies

- [Website](https://transgull.com)
- [Support](https://transgull.com/about/contactus)
- [Privacy policy](https://transgull.com/about/privacy)
- [Terms of service](https://transgull.com/about/terms)

## License

Plugin configuration and documentation are licensed under [Apache-2.0](LICENSE). Logo artwork and trademarks have separate terms in [TRADEMARKS.md](TRADEMARKS.md). This license does not cover the hosted TransGull service or its backend implementation.
