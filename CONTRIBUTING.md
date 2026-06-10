# Contributing

Thanks for your interest in SitePulsar's MCP server.

## This server is hosted

SitePulsar runs as a **remote, hosted** MCP server at `https://sitepulsar-mcp.vercel.app/mcp`. There is no local build or runtime in this repository — clients connect to the hosted endpoint. As a result, contributions here are about **documentation, examples, and connection ergonomics**, plus feedback that shapes the hosted tool surface.

<!-- TODO(gijs): if/when server source is open-sourced from the private `sitepulsar-mcp` repo, add a "Local development" section here with build/run/test steps. -->

## Reporting issues

Please open a GitHub issue for:

- Connection problems (OAuth handshake, Bearer auth, transport).
- Incorrect or unclear documentation in this repo.
- Unexpected tool behaviour, errors, or output shape mismatches.

When reporting a tool issue, include the tool name, the input you sent, your client (Claude desktop/web, Claude Code, Cursor, Cline, etc.), and what you expected vs. what you got. Do **not** paste API keys or OAuth tokens into issues.

## Proposing tool changes

The 13 tools are implemented in the private hosted backend, so tool behaviour changes can't be made via pull request here. Instead:

1. Open an issue describing the proposed new tool, parameter, or behaviour change, framed around the agent use case it unlocks (FIND / READ / USE).
2. We'll discuss scope, naming, and pillar fit.
3. Accepted changes ship on the hosted endpoint and are reflected in this repo's docs and in [`llms.txt`](https://www.sitepulsar.ai/llms.txt).

Documentation and example fixes (README, connect configs, curl examples) are very welcome as pull requests.

## Contact

Questions or anything sensitive: <info@sitepulsar.ai>.

## Code of conduct

Be respectful and constructive. We follow the spirit of the [Contributor Covenant](https://www.contributor-covenant.org/). Conduct concerns can be reported privately to <info@sitepulsar.ai>.
