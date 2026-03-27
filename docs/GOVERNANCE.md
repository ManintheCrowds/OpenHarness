# Governance (OpenHarness)

This repo is **documentation, rules, skills, and scripts**—not an authorization layer for production systems.

## Version control

- Prefer **pull requests** with review for substantive changes; avoid direct pushes to the default branch when branch protection is available.
- **Branch protection** (required reviewers, required status checks) is configured in the **Git host** (e.g. GitHub Settings → Rulesets). This repo’s markdown cannot enforce that; maintainers set policy per org.

## Skills and prompts are not authorization

- **Skills** (`.cursor/skills/*/SKILL.md`) and **rules** describe how agents *should* behave; they do **not** grant merge rights, deploy rights, or access to secrets.
- **Self-modification** and deployment narratives in reference docs (e.g. agent-native skill) assume **human gates**, **branch protection**, and **CI** outside the LLM. See [`.cursor/skills/agent-native-architecture/references/self-modification.md`](../.cursor/skills/agent-native-architecture/references/self-modification.md).

## Related

- [VERIFY_NOT_TRUST.md](VERIFY_NOT_TRUST.md) — MCP contract verification, canonical bundle
- [PUBLIC_AND_PRIVATE_HARNESS.md](PUBLIC_AND_PRIVATE_HARNESS.md) — what belongs in public vs private trees
- [SCP_SERVER_RELEASES.md](SCP_SERVER_RELEASES.md) — contract hash log for SCP MCP releases
