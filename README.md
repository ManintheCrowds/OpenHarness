# Harness — Context and Intent Engineering

Portable AI harness: context engineering, intent engineering, handoff flow, and state schema. **Guide** in the Guard–Guide–Build taxonomy.

Use with Cursor, Codex, or any agent platform that supports structured state and handoff.

## Contents

- **[docs/AGENT_ENTRY.md](docs/AGENT_ENTRY.md)** — One-screen chain for agents: manifest → CHEATSHEET → HANDOFF_FLOW → `state/`
- **[docs/SESSION_BOOTSTRAP.md](docs/SESSION_BOOTSTRAP.md)** — What to load first in a new session (aligns with CHEATSHEET memory load order)
- **docs/** — Architecture, context, intent, handoff flow; **docs/research/** — paper digests and gap analyses (provenance; raw extractions gitignored)
- **state/** — State schema (handoff, decision-log, preferences, etc.)
- **scripts/** — Reference scripts (copy prompt, validate handoff). Canonical script list: [docs/CHEATSHEET.md](docs/CHEATSHEET.md) (Agent invocation index); do not duplicate long script tables here.
- **.cursor/rules/** — Starter rules (role-routing, capability-summary, critic-loop-gate, intent-alignment-gate, model-selection)
- **.cursor/skills/** — Domain-agnostic skills; index with one-line summaries: [.cursor/skills/README.md](.cursor/skills/README.md)
- **.cursor/commands/** — Slash commands (`architect`, `agent-native-audit`)
- **docs/contracts/** — Public MCP contracts (e.g. SCP v1) for verify-not-trust
- **docs/CHEATSHEET.md** — One-page harness compression; includes **Agent invocation index (scripts)** for agent–human action parity (see [AGENT_NATIVE_CHECKLIST.md](docs/AGENT_NATIVE_CHECKLIST.md))
- **[capabilities.harness.yaml](capabilities.harness.yaml)** — Structured manifest: `scripts[]`, `scripts_globs`, `skills_globs`, checklist section links; CHEATSHEET remains the canonical script *table* (see file header)
- **docs/HARNESS_AUDIT_ALIGNMENT.md** — Part B (OpenHarness bundle) dimensions ↔ paths; aligns with OpenGrimoire audit backlog without an API

## Agent-native audit (minimum bundle)

Meaningful **script/YAML parity** audits need this repo’s **checklist** ([docs/AGENT_NATIVE_CHECKLIST.md](docs/AGENT_NATIVE_CHECKLIST.md)), **CHEATSHEET** agent index, **capabilities.harness.yaml**, and `python scripts/verify_script_index.py` on disk—markdown-only copies are **inventory-only**. Slash command: `.cursor/commands/agent-native-audit.md` (load OpenHarness as a **Cursor workspace root** so the command resolves). **Portfolio:** sibling **MiscRepos** [`.cursor/docs/AGENT_NATIVE_CHECKLIST.md`](../MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST.md) is an entry **stub** (links here + MISCOPS); addendum [`.cursor/docs/AGENT_NATIVE_CHECKLIST_MISCOPS.md`](../MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST_MISCOPS.md). Do not duplicate normative checklist text outside OpenHarness.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Context engineering** | Economical use of LLM context: retrieval routing, compaction, memory |
| **Intent engineering** | Human intent as primary signal; scope, constraints, human gates |
| **Handoff** | Document-then-continue: write handoff, new chat, paste continue prompt |
| **State schema** | handoff_latest, decision-log, known-issues, preferences, rejection_log |
| **Authority model** | Cryptographic vs social; risk-tier mapping; pseudoanonymous proof |

## Integration

1. Copy or symlink `docs/`, `state/`, `.cursor/rules/`, and `.cursor/skills/` into your project (e.g. `.cursor/docs/`, `.cursor/state/`, `.cursor/rules/`, `.cursor/skills/`).
2. Configure `.cursorrules` or agent instructions to reference harness docs and rules.
3. Use `scripts/` as templates; adapt paths for your layout (e.g. `.cursor/state/`).
4. Run `pre-commit install` if using the included pre-commit config for handoff/state validation.

## Documentation link check (sibling portfolio-harness)

When **portfolio-harness** is cloned as a sibling of this repo (same parent directory), relative links such as `../../portfolio-harness/...` from `docs/**/*.md` should resolve. Run:

```powershell
python scripts/check_docs_portfolio_links.py
```

Exit code `0` means every markdown file link that references `portfolio-harness` points at an existing file. Schedule or run after edits that touch cross-repo doc links.

## Canonical bundle (verify-not-trust)

Pin this repo by **commit SHA** and run:

```powershell
.\scripts\verify_canonical_bundle.ps1
```

See [docs/CANONICAL_AGENT_BUNDLE.md](docs/CANONICAL_AGENT_BUNDLE.md) and [docs/VERIFY_NOT_TRUST.md](docs/VERIFY_NOT_TRUST.md). After changing bundled files: `.\scripts\update_canonical_bundle_hashes.ps1`, then commit `docs/canonical-bundle.sha256`.

## Dependencies

- **SCP** (optional): Configure an **SCP MCP server** in `mcp.json` per [docs/MCP_PRIVATE_HOST.md](docs/MCP_PRIVATE_HOST.md). Public **contract**: [docs/contracts/scp_mcp_v1.md](docs/contracts/scp_mcp_v1.md). A reference public package may exist (`scp-mcp`); **org-private** installs are supported. Run `validate_handoff_scp.py` and `sanitize_input.py` as pre-commit hooks when handoff/state files are staged. **Trust / env:** optional semantic judge and `OLLAMA_BASE_URL` — see [docs/SCP_ENV_AND_TRUST.md](docs/SCP_ENV_AND_TRUST.md).
- **PyYAML** (`pip install -r requirements.txt`): used by `verify_script_index.py` and `verify_skills_readme.py` for manifest and skill front matter.

## Private wellbeing / survival corpora

Do **not** commit purchased PDFs or full extracted text to this harness. Use a private path; run **SCP on extracted text** before any RAG or handoff. Canonical playbook: `local-proto` repo `docs/HUMAN_WELLBEING_CORPUS.md` and `docs/SURVIVAL_MEDICAL_RAG_DISCLAIMER.md` (sibling layout under the same workspace root). For decision history in this repo, prefer root [`state/decision-log.md`](state/decision-log.md); use a private `.cursor/state/` checkout for material that must not ship publicly.

## Pre-commit

```bash
pip install pre-commit scp-mcp PyYAML
pre-commit install
```

Hooks (see `.pre-commit-config.yaml`):

| Hook | Purpose |
|------|---------|
| **sanitize-input** | Sanitize `state/*.md` before commit |
| **handoff-scp** | Validate `state/handoff_latest.md` against SCP rules | 
| **verify-script-index** | `verify_script_index.py` — disk script basenames ↔ `capabilities.harness.yaml` `scripts[]` ↔ CHEATSHEET backticks |
| **verify-skills-readme** | `verify_skills_readme.py` — `.cursor/skills/README.md` vs each `SKILL.md` `description:` |

When copying harness into a project with `.cursor/state/`, set `HARNESS_STATE_DIR=.cursor/state` and update `.pre-commit-config.yaml` paths.

**Windows:** Write handoff/state files as UTF-8 without BOM. PowerShell `Out-File` adds BOM by default; use `[System.IO.File]::WriteAllText(path, content)` to avoid SCP false positives.

## Delineation

When extending harness or adding components, use [docs/DELINEATION.md](docs/DELINEATION.md) to decide what belongs in core (harness) vs your project. Primary prompt: "Would any developer be able to use this without context from other projects?" Yes → core; No → your project.

## Public vs private

This repo is a **public** reference: use **synthetic** handoff examples ([docs/examples/HANDOFF_EXAMPLE_SYNTHETIC.md](docs/examples/HANDOFF_EXAMPLE_SYNTHETIC.md)), not real session state. Root [`state/`](state/) holds **schema + synthetic placeholders** suitable for cloning; keep real handoffs, `daily/`, archives, and decision logs with identifying detail in a **private** workspace or fork. **`.cursor/state/`** is gitignored here so local session files are not committed by mistake; see [docs/PUBLIC_AND_PRIVATE_HARNESS.md](docs/PUBLIC_AND_PRIVATE_HARNESS.md).

**Secrets:** `.gitignore` excludes `.env*`, common key filenames, and `.cursor/mcp.json`. Do not commit credentials; use env vars or a private config path per [docs/MCP_PRIVATE_HOST.md](docs/MCP_PRIVATE_HOST.md).

## OpenGrimoire (related app, not in this repo)

**OpenHarness** stays portable (docs, rules, skills, `state/`). **OpenGrimoire** is a separate Next.js app under **portfolio-harness** (`OpenGrimoire/`) that visualizes a **brain-map graph** built from `.cursor/state` session text (handoffs, daily notes, decision-log)—see `OpenGrimoire/docs/OPENGRIMOIRE_SYSTEMS_INVENTORY.md` in that workspace. Paths are relative to wherever you clone **portfolio-harness**. It is **not** meant to live inside this repository. If the graph does not show files from your OpenHarness checkout, either point `CURSOR_STATE_DIR` at `openharness/.cursor/state` when running `build_brain_map.py`, or use **`CURSOR_STATE_DIRS`** to merge `portfolio-harness` and `openharness` state in one JSON (see portfolio-harness `docs/BRAIN_MAP_HUB.md`). Handoffs must still reference `.md` paths for nodes to appear.

## References

- [AGENT_ENTRY.md](docs/AGENT_ENTRY.md) — Agent start: [capabilities.harness.yaml](capabilities.harness.yaml) → [CHEATSHEET.md](docs/CHEATSHEET.md) → [HANDOFF_FLOW.md](docs/HANDOFF_FLOW.md) → [state/](state/)
- [SESSION_BOOTSTRAP.md](docs/SESSION_BOOTSTRAP.md)
- [HARNESS_ARCHITECTURE.md](docs/HARNESS_ARCHITECTURE.md)
- [CHEATSHEET.md](docs/CHEATSHEET.md)
- [HANDOFF_CHAIN_PATTERNS.md](docs/HANDOFF_CHAIN_PATTERNS.md)
- [CONTEXT_ENGINEERING.md](docs/CONTEXT_ENGINEERING.md)
- [INTENT_ENGINEERING.md](docs/INTENT_ENGINEERING.md)
- [HANDOFF_FLOW.md](docs/HANDOFF_FLOW.md) (includes **Definition of done** for P1 verification + dual gates)
- [PUBLIC_AND_PRIVATE_HARNESS.md](docs/PUBLIC_AND_PRIVATE_HARNESS.md)
- [CANONICAL_AGENT_BUNDLE.md](docs/CANONICAL_AGENT_BUNDLE.md), [VERIFY_NOT_TRUST.md](docs/VERIFY_NOT_TRUST.md), [MCP_TRANSPARENCY.md](docs/MCP_TRANSPARENCY.md), [GOVERNANCE.md](docs/GOVERNANCE.md)
- [contracts/scp_mcp_v1.md](docs/contracts/scp_mcp_v1.md), [SCP_ENV_AND_TRUST.md](docs/SCP_ENV_AND_TRUST.md)
- [AUTHORITY_MODEL.md](docs/AUTHORITY_MODEL.md)
- [state/README.md](state/README.md)

## License

MIT
