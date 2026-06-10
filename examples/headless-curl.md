# Headless usage (Bearer API key)

For non-interactive / headless clients that cannot complete an OAuth handshake, authenticate with a Bearer API key minted in the [SitePulsar dashboard](https://www.sitepulsar.ai) (Pro/Business plan).

- **Endpoint (streamable-http):** `https://mcp.sitepulsar.ai/mcp`
- **Auth header (exact):** `Authorization: Bearer <mcp_api_key>`

> The JSON-RPC request bodies below are **illustrative** of the MCP wire shape (initialize → tools/list → tools/call). Streamable-http servers may also require an MCP session header and may stream responses as SSE.
> <!-- TODO(gijs): confirm exact request/response shapes, required headers (e.g. `Mcp-Session-Id`, `MCP-Protocol-Version`, `Accept: application/json, text/event-stream`), and the protocol version string against the live `sitepulsar-mcp` server before publishing. -->

Replace `$SITEPULSAR_API_KEY` with your key (e.g. `export SITEPULSAR_API_KEY=...`).

## 1. List available tools

```bash
curl -sS https://mcp.sitepulsar.ai/mcp \
  -H "Authorization: Bearer $SITEPULSAR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
  }'
```

## 2. Call a free tool — fast agent-readiness check

```bash
curl -sS https://mcp.sitepulsar.ai/mcp \
  -H "Authorization: Bearer $SITEPULSAR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
      "name": "check_agent_readiness",
      "arguments": {
        "url": "https://example.com"
      }
    }
  }'
```

## 3. Start a metered audit, then poll for the result

Start the audit (returns an `audit_id`):

```bash
curl -sS https://mcp.sitepulsar.ai/mcp \
  -H "Authorization: Bearer $SITEPULSAR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
      "name": "run_audit",
      "arguments": {
        "url": "https://example.com"
      }
    }
  }'
```

Poll for status and the decision-ready summary (substitute the returned `audit_id`):

```bash
curl -sS https://mcp.sitepulsar.ai/mcp \
  -H "Authorization: Bearer $SITEPULSAR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 4,
    "method": "tools/call",
    "params": {
      "name": "get_audit",
      "arguments": {
        "audit_id": "<audit_id_from_run_audit>"
      }
    }
  }'
```

> `run_audit` and `scan_visibility` are metered (Pro/Business). `check_agent_readiness`, `get_audit`, `get_audit_detail`, `get_audit_full`, `compare_aeo`, `get_fixes`, `search_companies`, and the `probe_*` tools are free. `scan_product_page` may be free or metered — see the dashboard.
