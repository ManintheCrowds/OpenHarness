# Harness — Context and Intent Engineering

Portable AI harness: context engineering, intent engineering, handoff flow, and state schema. **Guide** in the Guard–Guide–Build taxonomy.

Use with Cursor, Codex, or any agent platform that supports structured state and handoff.

## Contents

- **docs/** — Architecture, context, intent, handoff flow
- **state/** — State schema (handoff, decision-log, preferences, etc.)
- **scripts/** — Reference scripts (copy prompt, validate handoff)
- **.cursor/rules/** — Starter rules (role-routing, capability-summary, critic-loop-gate, model-selection)
- **.cursor/skills/** — Domain-agnostic skills (planning, product-scope, docs, tech-lead, refactor-reuse, qa-verifier, secure-contain-protect)

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

## Dependencies

- **SCP** (optional): For handoff validation, use the [SCP](https://github.com/ManintheCrowds/scp) package (`pip install scp-mcp`). Run `validate_handoff_scp.py` and `sanitize_input.py` as pre-commit hooks when handoff/state files are staged.

## Pre-commit

```bash
pip install pre-commit scp-mcp
pre-commit install
```

Hooks run on `state/*.md` (sanitize) and `state/handoff_latest.md` (handoff SCP validation). When copying harness into a project with `.cursor/state/`, set `HARNESS_STATE_DIR=.cursor/state` and update `.pre-commit-config.yaml` paths.

**Windows:** Write handoff/state files as UTF-8 without BOM. PowerShell `Out-File` adds BOM by default; use `[System.IO.File]::WriteAllText(path, content)` to avoid SCP false positives.

## Delineation

When extending harness or adding components, use [docs/DELINEATION.md](docs/DELINEATION.md) to decide what belongs in core (harness) vs your project. Primary prompt: "Would any developer be able to use this without context from other projects?" Yes → core; No → your project.

## Public vs private

This repo is a **public** reference: use **synthetic** handoff examples ([docs/examples/HANDOFF_EXAMPLE_SYNTHETIC.md](docs/examples/HANDOFF_EXAMPLE_SYNTHETIC.md)), not real session state. Keep real handoffs and experimental work in a **private** workspace; see [docs/PUBLIC_AND_PRIVATE_HARNESS.md](docs/PUBLIC_AND_PRIVATE_HARNESS.md).

## OpenAtlas (related app, not in this repo)

**OpenHarness** stays portable (docs, rules, skills, `state/`). **OpenAtlas** is a separate Next.js app under **portfolio-harness** (`OpenAtlas/`) that visualizes a **brain-map graph** built from `.cursor/state` session text (handoffs, daily notes, decision-log)—see `OpenAtlas/docs/OPENATLAS_SYSTEMS_INVENTORY.md` in that workspace. Paths are relative to wherever you clone **portfolio-harness**. It is **not** meant to live inside this repository. If the graph does not show files from your OpenHarness checkout, point `CURSOR_STATE_DIR` at the state directory you actually write to when running `build_brain_map.py`, or ensure handoffs reference those paths.

## References

- [HARNESS_ARCHITECTURE.md](docs/HARNESS_ARCHITECTURE.md)
- [CHEATSHEET.md](docs/CHEATSHEET.md)
- [HANDOFF_CHAIN_PATTERNS.md](docs/HANDOFF_CHAIN_PATTERNS.md)
- [CONTEXT_ENGINEERING.md](docs/CONTEXT_ENGINEERING.md)
- [INTENT_ENGINEERING.md](docs/INTENT_ENGINEERING.md)
- [HANDOFF_FLOW.md](docs/HANDOFF_FLOW.md)
- [PUBLIC_AND_PRIVATE_HARNESS.md](docs/PUBLIC_AND_PRIVATE_HARNESS.md)
- [AUTHORITY_MODEL.md](docs/AUTHORITY_MODEL.md)
- [state/README.md](state/README.md)

## License

MIT
