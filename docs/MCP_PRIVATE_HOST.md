# MCP private host (template)

Use this pattern when the **implementation** of an MCP server is private (internal repo, local checkout, or org registry) but the **agent contract** is public (e.g. [contracts/scp_mcp_v1.md](contracts/scp_mcp_v1.md)).

## Cursor `mcp.json` (example shape)

**Do not commit secrets.** Replace placeholders with your paths or package runner.

```json
{
  "mcpServers": {
    "scp": {
      "command": "python",
      "args": ["-m", "scp.scp_mcp"],
      "env": {}
    }
  }
}
```

Variations:

- **Editable install:** `"command": "D:/path/to/.venv/Scripts/python.exe"` and `args` pointing at your private checkout.
- **Published internal wheel:** same, with venv that `pip install`’d your private package.

## Verify

1. Confirm each tool name the agent expects appears in the host’s tool list (see contract doc).
2. Run your server’s **contract tests** (private CI) before tagging a release.
3. Record **CONTRACT_HASH** for that release in private changelog and optionally [SCP_SERVER_RELEASES.md](SCP_SERVER_RELEASES.md).
