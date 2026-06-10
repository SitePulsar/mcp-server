# Publishing `@sitepulsar/mcp-server` to npm

Founder checklist. Run these from inside the `c2-npm/` package directory
(or wherever this package has been copied into the public repo).

## 0. Before you start

- [ ] Confirm the npm org **`@sitepulsar`** exists and you are a member with
      publish rights (https://www.npmjs.com/org/sitepulsar). Create the org if
      it doesn't exist (Settings → Add Organization → `sitepulsar`).
- [ ] Confirm `bin/sitepulsar-mcp.mjs` is executable in the published tarball
      (npm preserves the shebang; the `bin` field handles the exec bit on install).
- [ ] **Pin the `mcp-remote` dependency.** `package.json` currently uses
      `"mcp-remote": "^0.1.0"` as a placeholder. Check the latest version
      (`npm view mcp-remote version`) and set a sensible caret range against it
      before publishing.

## 1. Sanity-check the package contents

```bash
npm install            # installs mcp-remote
npm pack --dry-run     # lists exactly what will be published
```

Confirm the tarball contains `package.json`, `bin/sitepulsar-mcp.mjs`, and
`README.md` — and nothing else (the `files` array gates this).

## 2. Local smoke test (before publishing)

```bash
node bin/sitepulsar-mcp.mjs --help    # should hand off to mcp-remote
```

Or link it and exercise the bin name:

```bash
npm link
sitepulsar-mcp --version || true      # confirms the bin resolves + spawns mcp-remote
npm unlink -g @sitepulsar/mcp-server
```

## 3. Log in and publish

```bash
npm login                              # auth under an account in the @sitepulsar org
# (complete 2FA in your authenticator if enabled — recommended for a public org)

npm publish --access public            # scoped packages default to private; --access public is required
```

> First publish of a brand-new scoped name will fail if the `@sitepulsar` org
> doesn't exist yet — create it first (step 0).

## 4. Verify the published package

```bash
npm view @sitepulsar/mcp-server        # confirm version 0.1.0 is live
npx @sitepulsar/mcp-server --help      # pulls from the registry and runs the launcher
```

## 5. Smoke test in a real stdio client (Claude Desktop)

Add to `claude_desktop_config.json` → `mcpServers`:

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

- [ ] Restart Claude Desktop.
- [ ] Complete the OAuth flow when prompted (browser window from `mcp-remote`).
- [ ] Confirm SitePulsar tools appear and a tool call (e.g. `run_audit` /
      `get_audit`) succeeds.
- [ ] (Optional) Repeat with the Bearer-key variant for a Pro/Business key.

## 6. Post-publish

- [ ] Tag the release in the public repo (`github.com/SitePulsar/mcp-server`).
- [ ] Update https://www.sitepulsar.ai/llms.txt and install docs to reference
      `npx @sitepulsar/mcp-server`.
