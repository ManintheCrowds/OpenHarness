# SCP environment and trust (OpenHarness)

Pre-commit hooks [`scripts/sanitize_input.py`](../scripts/sanitize_input.py) and [`scripts/validate_handoff_scp.py`](../scripts/validate_handoff_scp.py) call the SCP package’s `run_pipeline` on handoff and state markdown. **mask-check** runs [`scripts/mask_check.py`](../scripts/mask_check.py), which refuses to scan unless installed `scp-mcp` is the pinned commit, then calls `mask_secrets --check` on `state/**/*.{md,json,jsonl,txt,yaml,yml}` (any case), plus `HANDOFF.md`, `handoffs/`, and `next_prompt` files. The pre-commit hook uses `language: python` so that commit is installed in the hook environment. **gitleaks** (CLI **v8.30.1**) scans staged changes. `scp-mcp` is pinned in `requirements.txt` to the SCP commit that added check mode; do not vendor that module.

## Optional semantic judge

When SCP’s **semantic judge** path is enabled (see SCP package docs and [`docs/contracts/scp_mcp_v1.md`](contracts/scp_mcp_v1.md)), pipeline code may send a **bounded excerpt** of your content to a **local LLM HTTP endpoint** (commonly `OLLAMA_BASE_URL`, default `http://localhost:11434`) for an additional tier decision.

**Treat this like any outbound request:**

- **`OLLAMA_BASE_URL`** must be an **origin only** (`http`/`https`, no path, query, or userinfo). Allowed hosts: `localhost`, `127.0.0.1`, `::1`, plus comma-separated **`OLLAMA_ALLOWED_HOSTS`**. Optional **`OLLAMA_URL_STRICT=1`** rejects names that resolve to private or link-local addresses.
- The client uses **`requests`** with **`allow_redirects=False`** to `/api/generate`; cross-host redirect chains are not followed.
- Optional auth: **`OLLAMA_API_KEY`** is sent as `Authorization: Bearer …` — **never** put tokens in the URL.
- Point the URL only at a **host you trust** (typically loopback for local Ollama). Use **firewall / network policy** so the process cannot reach sensitive internal subnets unless intended.
- Do **not** aim it at arbitrary URLs on shared or CI machines unless you intend that traffic.
- Keep semantic judge **off** in CI and locked-down environments unless you explicitly need it; default pre-commit does not require it.

Secrets and API keys do not belong in handoff or state files; SCP reduces prompt-injection risk but does not replace judgment about what you commit.

See also: [MCP_PRIVATE_HOST.md](MCP_PRIVATE_HOST.md), [VERIFY_NOT_TRUST.md](VERIFY_NOT_TRUST.md).
