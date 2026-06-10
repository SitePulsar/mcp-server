# @sitepulsar/mcp-server

Stdio launcher for the **SitePulsar** hosted MCP server.

SitePulsar runs **AEO (Agent Experience Optimization)** audits — it measures how
**findable, readable, and usable** a website is to AI answer engines and
autonomous AI agents, and returns one AEO score across three pillars:
**FIND / READ / USE**. It is agent infrastructure, not SEO tooling.

> The SitePulsar MCP server is **remote** (streamable-http). This npm package is
> only needed by MCP clients that require a local `command` (stdio). Clients that
> support remote URLs can skip the package entirely — see below.

---

## Remote clients (no package needed)

If your MCP client supports remote/streamable-http servers directly
(e.g. the Claude Desktop connector UI, Cursor), just point it at:

```
https://mcp.sitepulsar.ai/mcp
```

Authenticate with **OAuth** (the connector flow, no key) or a **Bearer API key**
(Pro/Business — header `Authorization: Bearer <mcp_api_key>`).

---

## Stdio clients (use this package)

For clients that only accept a local stdio command, this package launches a local
bridge (`mcp-remote`) that proxies to the hosted endpoint.

Run it directly with `npx` (no install required):

```bash
npx @sitepulsar/mcp-server
```

This starts a stdio MCP server that proxies to
`https://mcp.sitepulsar.ai/mcp`, with OAuth handled by `mcp-remote`.

### Example client config

```json
{
  "mcpServers": {
    "sitepulsar": {
      "command": "npx",
      "args": ["-y", "@sitepulsar/mcp-server"]
    }
  }
}
```

### Bearer API key (Pro/Business)

Any args you pass are forwarded to `mcp-remote` after the endpoint, so you can
pass an `Authorization` header instead of using OAuth:

```bash
npx @sitepulsar/mcp-server --header "Authorization: Bearer <mcp_api_key>"
```

```json
{
  "mcpServers": {
    "sitepulsar": {
      "command": "npx",
      "args": [
        "-y",
        "@sitepulsar/mcp-server",
        "--header",
        "Authorization: Bearer <mcp_api_key>"
      ]
    }
  }
}
```

---

## Links

- Website: https://www.sitepulsar.ai
- Tool/docs manifest (LLM-readable): https://www.sitepulsar.ai/llms.txt
- Contact: info@sitepulsar.ai

## License

MIT © Gijs van Bueren / SitePulsar
