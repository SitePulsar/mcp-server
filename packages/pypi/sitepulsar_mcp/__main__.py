"""Console entry point for the SitePulsar MCP stdio launcher.

IMPORTANT — read before extending this file
============================================
The SitePulsar MCP server is REMOTE (streamable-http). Many MCP clients connect
to a remote URL directly and do NOT need any local package. This package is only
useful for clients that require a local stdio command.

Python does not yet have a single, widely-adopted, drop-in stdio->remote MCP
bridge equivalent to the Node `mcp-remote` proxy (which also handles the OAuth
handshake). Rather than ship a half-working proxy we cannot verify end-to-end,
this entry point currently prints clear guidance and points users at the two
supported paths:

  1. Connect the client directly to the remote URL (preferred), or
  2. Use the Node `mcp-remote` proxy via `npx` as the stdio bridge.

See the TODO below for the native-proxy implementation plan.
"""

from __future__ import annotations

import sys

from . import ENDPOINT, __version__


# ---------------------------------------------------------------------------
# TODO (native stdio->remote bridge)
# ---------------------------------------------------------------------------
# Implement a real stdio MCP server that proxies to the hosted streamable-http
# endpoint, so `sitepulsar-mcp` can be used as a `command` by stdio-only clients
# without requiring Node/`mcp-remote`.
#
# Sketch of the intended implementation:
#   * Use the official `mcp` Python SDK (https://github.com/modelcontextprotocol
#     /python-sdk). Add `mcp[cli]` (or `httpx` + the low-level client) to
#     `dependencies` in pyproject.toml when implementing.
#   * Open a streamable-http client session to ENDPOINT.
#   * Run a local stdio server that forwards JSON-RPC messages in both
#     directions (a transparent proxy / passthrough of initialize, tools/list,
#     tools/call, etc.).
#   * Implement OAuth for the streamable-http transport, OR accept a Bearer
#     token via `--header "Authorization: Bearer <mcp_api_key>"` and attach it
#     to outbound requests (Pro/Business keys).
#
# Until that lands, `main()` is intentionally a guidance shim — do NOT fabricate
# a proxy here that hasn't been verified against the live server.
# ---------------------------------------------------------------------------


GUIDANCE = f"""\
SitePulsar MCP (v{__version__})
================================

The SitePulsar MCP server is REMOTE (streamable-http):

    {ENDPOINT}

A native Python stdio->remote bridge is not implemented yet (see the TODO in
sitepulsar_mcp/__main__.py). Use one of the supported paths instead:

1) Remote-capable clients (preferred) — connect directly to the URL above.
   Authenticate with OAuth (connector flow) or a Bearer API key
   (Pro/Business: header `Authorization: Bearer <mcp_api_key>`).

   Example client config:

     {{
       "mcpServers": {{
         "sitepulsar": {{
           "url": "{ENDPOINT}"
         }}
       }}
     }}

2) Stdio-only clients — use the Node `mcp-remote` proxy as the bridge:

     npx mcp-remote {ENDPOINT}

   Or the SitePulsar npm launcher (same effect):

     npx @sitepulsar/mcp-server

   Example stdio client config:

     {{
       "mcpServers": {{
         "sitepulsar": {{
           "command": "npx",
           "args": ["-y", "mcp-remote", "{ENDPOINT}"]
         }}
       }}
     }}

Docs: https://www.sitepulsar.ai/llms.txt
Site: https://www.sitepulsar.ai   ·   Contact: info@sitepulsar.ai
"""


def main() -> int:
    """Entry point for the ``sitepulsar-mcp`` console script.

    Prints connection guidance. Returns a non-zero exit code because no stdio
    MCP transport is actually served yet — a stdio client launching this as its
    ``command`` should treat the absence of a transport as a failure rather than
    silently hang. Guidance goes to stderr so it never corrupts a stdio
    JSON-RPC stream if a client does wire this up as a server.
    """
    if any(arg in ("-V", "--version") for arg in sys.argv[1:]):
        print(__version__)
        return 0

    sys.stderr.write(GUIDANCE)
    sys.stderr.flush()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
