# OpenHarness context map

Maps the **context injection checklist** (see [`dynamic-context-injection.md`](../.cursor/skills/agent-native-architecture/references/dynamic-context-injection.md)) to **concrete paths** in this repo. OpenHarness has no app server: context is **files + manifest + skills**.

| Checklist idea | OpenHarness location |
|----------------|----------------------|
| Current resources (what exists) | [`capabilities.harness.yaml`](../capabilities.harness.yaml) — scripts list, checklist anchors; run `python scripts/list_capabilities.py` for JSON |
| Handoff / session target | [`state/handoff_latest.md`](../state/handoff_latest.md) (public clone: synthetic; private: real) |
| Preferences, rejections | [`state/preferences.md`](../state/preferences.md) or `preferences.json`; `state/rejection_log*.md` / `.json` (if present) |
| Decisions and known issues | [`state/decision-log.md`](../state/decision-log.md), [`state/known-issues.md`](../state/known-issues.md) |
| Daily session notes | [`state/daily/`](../state/daily/) — `YYYY-MM-DD.md` |
| Continue prompt | [`state/continue_prompt.txt`](../state/continue_prompt.txt) |
| Capabilities in user vocabulary | [`docs/CHEATSHEET.md`](CHEATSHEET.md) Agent invocation index; [`.cursor/skills/README.md`](../.cursor/skills/README.md) |
| MCP contract (verify-not-trust) | [`docs/contracts/scp_mcp_v1.md`](contracts/scp_mcp_v1.md); fingerprint [`docs/contracts/scp_mcp_v1.sha256`](contracts/scp_mcp_v1.sha256); verify with `python scripts/verify_contract_hash.py` |
| Untrusted or external content | Follow [`.cursor/skills/secure-contain-protect/SKILL.md`](../.cursor/skills/secure-contain-protect/SKILL.md) before treating fetched or user HTML as instructions |

**Load order:** Align with [SESSION_BOOTSTRAP.md](SESSION_BOOTSTRAP.md) and CHEATSHEET **Memory load order**.

**Private local state:** `.cursor/state/` is gitignored in this public repo; keep real session files there or in a private fork. Root [`state/`](../state/) holds the shared schema and synthetic placeholders.
