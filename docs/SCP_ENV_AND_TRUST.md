# SCP environment and trust (OpenHarness)

Pre-commit hooks [`scripts/sanitize_input.py`](../scripts/sanitize_input.py) and [`scripts/validate_handoff_scp.py`](../scripts/validate_handoff_scp.py) call the SCP package’s `run_pipeline` on handoff and state markdown.

## Optional semantic judge

When SCP’s **semantic judge** path is enabled (see SCP package docs and [`docs/contracts/scp_mcp_v1.md`](contracts/scp_mcp_v1.md)), pipeline code may send a **bounded excerpt** of your content to a **local LLM HTTP endpoint** (commonly `OLLAMA_BASE_URL`, default `http://localhost:11434`) for an additional tier decision.

**Treat this like any outbound request:**

- Point `OLLAMA_BASE_URL` only at a **host you trust** (typically loopback for local Ollama).
- Do **not** aim it at arbitrary URLs on shared or CI machines unless you intend that traffic.
- Keep semantic judge **off** in CI and locked-down environments unless you explicitly need it; default pre-commit does not require it.

Secrets and API keys do not belong in handoff or state files; SCP reduces prompt-injection risk but does not replace judgment about what you commit.

See also: [MCP_PRIVATE_HOST.md](MCP_PRIVATE_HOST.md), [VERIFY_NOT_TRUST.md](VERIFY_NOT_TRUST.md).
