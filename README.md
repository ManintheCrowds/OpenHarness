# Harness — Context and Intent Engineering

Portable AI harness: context engineering, intent engineering, handoff flow, and state schema. **Guide** in the Guard–Guide–Build taxonomy.

Use with Cursor, Codex, or any agent platform that supports structured state and handoff.

## Contents

- **docs/** — Architecture, context, intent, handoff flow
- **state/** — State schema (handoff, decision-log, preferences, etc.)
- **scripts/** — Reference scripts (copy prompt, validate handoff)

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Context engineering** | Economical use of LLM context: retrieval routing, compaction, memory |
| **Intent engineering** | Human intent as primary signal; scope, constraints, human gates |
| **Handoff** | Document-then-continue: write handoff, new chat, paste continue prompt |
| **State schema** | handoff_latest, decision-log, known-issues, preferences, rejection_log |

## Integration

1. Copy or symlink `docs/` and `state/README.md` into your project (e.g. `.cursor/docs/`, `.cursor/state/`).
2. Configure `.cursorrules` or agent instructions to reference harness docs.
3. Use `scripts/` as templates; adapt paths for your layout (e.g. `.cursor/state/`).

## Dependencies

- **SCP** (optional): For handoff validation, use the [SCP](https://github.com/ManintheCrowds/SCP) package. Run `validate_handoff_scp.py` as a pre-commit hook when handoff is staged.

## References

- [HARNESS_ARCHITECTURE.md](docs/HARNESS_ARCHITECTURE.md)
- [CHEATSHEET.md](docs/CHEATSHEET.md)
- [HANDOFF_CHAIN_PATTERNS.md](docs/HANDOFF_CHAIN_PATTERNS.md)
- [CONTEXT_ENGINEERING.md](docs/CONTEXT_ENGINEERING.md)
- [INTENT_ENGINEERING.md](docs/INTENT_ENGINEERING.md)
- [HANDOFF_FLOW.md](docs/HANDOFF_FLOW.md)
- [state/README.md](state/README.md)

## License

MIT
