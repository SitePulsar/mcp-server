---
name: aeo-audit
description: Run SitePulsar AEO agent-readiness audits and explain FIND/READ/USE scores and prioritized fixes via the SitePulsar MCP.
---

When the user wants to know how AI agents find, read, or use a website, use the SitePulsar MCP.

1. Prefer `check_agent_readiness` for a fast FIND/READ/USE snapshot of a public URL.
2. Use `run_audit` when they want a fuller audit; keep the returned audit id.
3. Use `get_audit` to fetch scores and findings for an audit the user owns.
4. Use `get_fixes` to list prioritized remediation steps.

Only audit public URLs the user provides or sites they own. Do not attempt payments, account deletion, or access to another customer's audits. If a URL is invalid or unreachable, say so and ask for a valid HTTPS URL.
