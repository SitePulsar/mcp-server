#!/usr/bin/env node
/**
 * SitePulsar MCP — stdio launcher
 * --------------------------------
 * The SitePulsar MCP server is REMOTE (streamable-http). MCP clients that
 * support remote URLs directly (e.g. Claude Desktop's connector UI, Cursor)
 * do NOT need this package — they can point straight at the endpoint below.
 *
 * This launcher exists for clients that ONLY accept a local `command`/`args`
 * (stdio) MCP server. It is a thin wrapper around the well-known `mcp-remote`
 * proxy: it spawns `mcp-remote <endpoint>` so a stdio client can talk to the
 * hosted server, with OAuth handled by mcp-remote.
 *
 * Auth:
 *   - OAuth (default): mcp-remote performs the browser OAuth handshake.
 *   - Bearer API key (Pro/Business): pass it through, e.g.
 *       npx @sitepulsar/mcp-server --header "Authorization: Bearer <mcp_api_key>"
 *
 * Any extra CLI args are forwarded verbatim to mcp-remote AFTER the endpoint,
 * so `--header`, `--transport`, etc. all work.
 */

import { spawn } from "node:child_process";
import { createRequire } from "node:module";

const ENDPOINT = "https://mcp.sitepulsar.ai/mcp";

// Forward every CLI arg after our own invocation to mcp-remote.
const forwardedArgs = process.argv.slice(2);

/**
 * Resolve the mcp-remote CLI entry point from this package's own
 * node_modules so we don't depend on a globally-installed copy.
 * Falls back to invoking `mcp-remote` via npx-style resolution if the
 * direct require fails (older/newer layouts).
 */
function resolveMcpRemoteBin() {
  const require = createRequire(import.meta.url);
  try {
    // mcp-remote ships a `bin` entry; resolve its package.json then read bin.
    const pkgPath = require.resolve("mcp-remote/package.json");
    const pkg = require(pkgPath);
    const binField = pkg.bin;
    let relBin;
    if (typeof binField === "string") {
      relBin = binField;
    } else if (binField && typeof binField === "object") {
      // Prefer a "mcp-remote" key, otherwise the first bin entry.
      relBin = binField["mcp-remote"] ?? Object.values(binField)[0];
    }
    if (!relBin) return null;
    const { dirname, resolve } = require("node:path");
    return resolve(dirname(pkgPath), relBin);
  } catch {
    return null;
  }
}

function main() {
  const binPath = resolveMcpRemoteBin();

  let child;
  if (binPath) {
    // Run the resolved mcp-remote entry directly with the current Node binary.
    child = spawn(process.execPath, [binPath, ENDPOINT, ...forwardedArgs], {
      stdio: "inherit",
    });
  } else {
    // Fallback: rely on a `mcp-remote` command being on PATH.
    child = spawn("mcp-remote", [ENDPOINT, ...forwardedArgs], {
      stdio: "inherit",
      shell: process.platform === "win32",
    });
  }

  child.on("error", (err) => {
    process.stderr.write(
      `[sitepulsar-mcp] Failed to start mcp-remote: ${err.message}\n` +
        `[sitepulsar-mcp] Ensure dependencies are installed, or connect your client ` +
        `directly to the remote URL: ${ENDPOINT}\n`
    );
    process.exit(1);
  });

  // Mirror the child's exit code/signal.
  child.on("exit", (code, signal) => {
    if (signal) {
      // Re-raise the signal so the parent reflects it; default to 1.
      process.exit(1);
    }
    process.exit(code ?? 0);
  });

  // Forward termination signals to the child so Ctrl-C cleans up.
  for (const sig of ["SIGINT", "SIGTERM"]) {
    process.on(sig, () => {
      if (!child.killed) child.kill(sig);
    });
  }
}

main();
