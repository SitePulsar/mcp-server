# SitePulsar MCP Server

[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-ai.sitepulsar%2Fmcp-blue)](https://www.sitepulsar.ai/llms.txt)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Transport: streamable-http](https://img.shields.io/badge/transport-streamable--http-purple)](https://sitepulsar-mcp.vercel.app/mcp)

> Agent Experience Optimization (AEO) for AI agents — measure and improve how findable, readable, and usable any website is to AI answer engines and autonomous AI agents, directly from your MCP client.

A **remote, hosted** [Model Context Protocol](https://modelcontextprotocol.io) server. There is nothing to build or run locally — connect your MCP client to the hosted endpoint and the 13 tools below become available.

**Endpoint (streamable-http):** `https://sitepulsar-mcp.vercel.app/mcp`

---

## What is SitePulsar / AEO?

SitePulsar is an **Agent Experience Optimization (AEO)** audit platform. It measures how findable, readable, and usable a website is to AI answer engines and autonomous AI agents, and returns one AEO score across three pillars:

- **FIND** — discoverability across ChatGPT, Claude, Gemini, Perplexity, and Grok.
- **READ** — comprehension, structured data, and trust signals.
- **USE** — agent-actionability (can an autonomous AI agent actually take action on the site?).

AEO is the agent-native successor to what used to be split as GEO + AIO. SitePulsar is agent infrastructure, not an SEO tool.

---

## Quick start

The server supports two auth modes. Pick whichever fits your client.

### Option A — OAuth (recommended for Claude; no API key)

Add SitePulsar as a **custom connector** in Claude using the endpoint. Claude walks you through the OAuth handshake; no API key needs to be stored.

- **Endpoint:** `https://sitepulsar-mcp.vercel.app/mcp`
- **OAuth protected-resource metadata:** `https://sitepulsar-mcp.vercel.app/.well-known/oauth-protected-resource`

### Option B — Bearer API key (for headless / non-interactive clients)

Mint an MCP API key in the [SitePulsar dashboard](https://www.sitepulsar.ai) (Pro/Business plan), then send it on every request:

```
Authorization: Bearer <mcp_api_key>
```

See [`examples/headless-curl.md`](./examples/headless-curl.md) for raw HTTP usage.

---

## Connect matrix

| Client | How to connect |
| --- | --- |
| **Claude (desktop / web)** | Settings → Connectors → Add custom connector → paste `https://sitepulsar-mcp.vercel.app/mcp`, then complete OAuth. |
| **Claude Code (CLI)** | `claude mcp add --transport http sitepulsar https://sitepulsar-mcp.vercel.app/mcp` |
| **Cursor / Cline (JSON config)** | Add to your MCP config: see below. |

Cursor / Cline JSON config:

```json
{
  "mcpServers": {
    "sitepulsar": {
      "url": "https://sitepulsar-mcp.vercel.app/mcp"
    }
  }
}
```

A ready-to-paste config is in [`examples/claude_desktop_config.json`](./examples/claude_desktop_config.json).

> For headless clients that cannot do interactive OAuth, add an `Authorization: Bearer <mcp_api_key>` header (see Option B above).

---

## Tools

13 tools, grouped by pillar coverage. "Metered" tools run a billed audit/scan and require a Pro/Business plan; "Free" tools are read-only or lightweight probes.

| Tool | What it does | Cost |
| --- | --- | --- |
| `check_agent_readiness` | Fast synchronous agent-readiness check for a URL (no full run, no charge). Immediate signals on machine readability, structured data, and agent-accessibility. | Free |
| `run_audit` | Start a full async AEO audit for a URL. Returns an `audit_id`; poll with `get_audit`. | Metered (Pro/Business) |
| `get_audit` | Poll status and, when complete, a decision-ready summary: AEO score (overall + FIND/READ/USE), weakest pillar, headline takeaways, and top fixes. | Free |
| `get_audit_detail` | Full per-section breakdown of a completed audit — per-dimension sub-scores, reputation across engines, competitor cluster, crawl/schema/robots, agentic + USE probes, rendered-DOM. | Free |
| `get_audit_full` | One call returning summary + full detail + fixes (use `expand` to trim). | Free |
| `compare_aeo` | Compare AEO posture across multiple URLs on the same pillar scale. | Free |
| `get_fixes` | Prioritised, pillar-tagged action plan for a completed audit, ordered by estimated impact. | Free |
| `search_companies` | Samples major AI engines for which companies they name for a query; returns a consensus shortlist (≤5). | Free |
| `probe_agent_discovery` | Checks the official MCP registry, PyPI, and GitHub for servers/packages tied to a domain or brand. | Free |
| `probe_mcp_functional` | Discovers a site's advertised MCP endpoint and reports its declared OAuth/transport posture + declared tool names. | Free |
| `probe_ucp_readiness` | Inspects `/.well-known/ucp` for AI-shopping-agent transactability (presence + advertised capabilities). | Free |
| `scan_visibility` | Live AI-visibility scan for any brand (crawl + reputation across engines): where a brand is mentioned. | Metered (Pro/Business) |
| `scan_product_page` | Product-page readability scan for AI agents; structured product/offer extraction. | Free or metered — see dashboard |

Full machine-readable tool reference: [`llms.txt`](https://www.sitepulsar.ai/llms.txt).

---

## Authentication

SitePulsar accepts either of the following on the hosted endpoint.

### OAuth

Used by interactive clients (e.g. Claude custom connectors). The server advertises its OAuth posture via RFC 9728 protected-resource metadata:

```
https://sitepulsar-mcp.vercel.app/.well-known/oauth-protected-resource
```

Your client discovers the authorization server from that document and completes the handshake — no API key is stored on your side.

### Bearer API key

Used by headless clients. Mint a key in the [SitePulsar dashboard](https://www.sitepulsar.ai) (Pro/Business plan) and send it on every request:

```
Authorization: Bearer <mcp_api_key>
```

Metered tools (`run_audit`, `scan_visibility`, and the metered path of `scan_product_page`) require a Pro/Business plan regardless of auth mode.

---

## Links

- Website: <https://www.sitepulsar.ai>
- Tool reference (llms.txt): <https://www.sitepulsar.ai/llms.txt>
- Hosted MCP endpoint: `https://sitepulsar-mcp.vercel.app/mcp`
- OAuth metadata: `https://sitepulsar-mcp.vercel.app/.well-known/oauth-protected-resource`
- Listed in the official MCP registry as `ai.sitepulsar/mcp` (v1.0.0).

---

## License

MIT — see [`LICENSE`](./LICENSE).

## Built by

[SitePulsar](https://www.sitepulsar.ai) — EU-based (Netherlands). Founder & CEO: [Gijs van Bueren](https://www.linkedin.com/in/gijs-van-bueren-51b8263b2/). Questions: <info@sitepulsar.ai>.
