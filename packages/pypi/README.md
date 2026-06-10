# sitepulsar-mcp

Stdio launcher for the **SitePulsar** hosted MCP server.

SitePulsar runs **AEO (Agent Experience Optimization)** audits — it measures how
**findable, readable, and usable** a website is to AI answer engines and
autonomous AI agents, returning one Agent Readiness Score across three pillars:
**FIND / READ / USE**. It is agent infrastructure, not SEO tooling.

> The SitePulsar MCP server is **remote** (streamable-http). Most MCP clients can
> connect to the URL directly and don't need this package. This package targets
> clients that require a local stdio command bridge.

---

## Install

```bash
pip install sitepulsar-mcp
```

## The remote endpoint

```
https://mcp.sitepulsar.ai/mcp
```

Authenticate with **OAuth** (the connector flow, no key) or a **Bearer API key**
(Pro/Business — header `Authorization: Bearer <mcp_api_key>`).

---

## Usage

### Remote-capable clients (preferred)

Point your client straight at the endpoint — no package required:

```json
{
  "mcpServers": {
    "sitepulsar": {
      "url": "https://mcp.sitepulsar.ai/mcp"
    }
  }
}
```

### Stdio-only clients

> **Status:** a native Python stdio→remote bridge is **not implemented yet**
> (see the TODO in `sitepulsar_mcp/__main__.py`). Running `sitepulsar-mcp` today
> prints connection guidance rather than serving an MCP transport.

Until the native bridge lands, use the Node `mcp-remote` proxy as the stdio
bridge:

```bash
npx mcp-remote https://mcp.sitepulsar.ai/mcp
```

or the SitePulsar npm launcher (same effect):

```bash
npx @sitepulsar/mcp-server
```

Example stdio client config:

```json
{
  "mcpServers": {
    "sitepulsar": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.sitepulsar.ai/mcp"]
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
