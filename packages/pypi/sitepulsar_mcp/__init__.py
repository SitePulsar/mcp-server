"""SitePulsar MCP — stdio launcher for the hosted SitePulsar MCP server.

SitePulsar runs AEO (Agent Experience Optimization) audits: it measures how
findable, readable, and usable a website is to AI answer engines and autonomous
AI agents, returning one Agent Readiness Score across three pillars
(FIND / READ / USE). This is agent infrastructure, not SEO tooling.

The SitePulsar MCP server is REMOTE (streamable-http) at:

    https://mcp.sitepulsar.ai/mcp

Most MCP clients can connect to that URL directly. This package exists only to
help clients that require a local stdio command bridge to the remote endpoint.
"""

__version__ = "0.1.1"

ENDPOINT = "https://mcp.sitepulsar.ai/mcp"

__all__ = ["__version__", "ENDPOINT"]
