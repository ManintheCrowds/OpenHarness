# Backlog (OpenHarness)

Optional and future work that is **not** required for the core portable harness. Normative process remains [AGENT_NATIVE_CHECKLIST.md](AGENT_NATIVE_CHECKLIST.md) and [CONTRIBUTING.md](../CONTRIBUTING.md).

## Thin MCP over harness scripts (agent-native parity)

**Source:** [HARNESS_AUDIT_ALIGNMENT.md](HARNESS_AUDIT_ALIGNMENT.md) § Backlog (agent-native audit follow-up).

**Idea:** An MCP server that **lists** and **runs** only allowlisted scripts from [capabilities.harness.yaml](../capabilities.harness.yaml) and [CHEATSHEET.md](CHEATSHEET.md), subprocess from repo root, **no arbitrary shell**. Complements parity for agents that only expose MCP instead of `run_terminal_cmd`.

**Status:** Not implemented. Security, allowlisting, and host configuration should be documented alongside [MCP_PRIVATE_HOST.md](MCP_PRIVATE_HOST.md) when this is built.

**Scope guardrails (from alignment doc):** No new business logic in the server—thin wrapper over existing scripts only.
