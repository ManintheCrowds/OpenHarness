# Context Handoff Flow

"Document then continue" — write handoff, open new chat, paste continue prompt.

## Flow

1. **Trigger** — Say "handoff", "write handoff", or "context handoff".
2. **Archive then write** — Copy existing handoff to archive; write handoff_latest.md with Done, Next, Paths, Decisions.
3. **Append to daily log** — Add short block to daily/YYYY-MM-DD.md.
4. **New chat** — Open new chat (Cmd/Ctrl+L).
5. **Paste** — Paste continue prompt (or run copy script), then send.

## Trust Boundary

Handoff is a **trust boundary**. Before pasting:

- Run SCP validation on handoff when staged (pre-commit).
- Optional: Run integrity check to verify handoff was not modified.

## Continue Prompt

Canonical source: `state/continue_prompt.txt`. Run copy script to paste.

## Scripts

- **copy_continue_prompt.ps1** (Windows) / **copy_continue_prompt.sh** (macOS/Linux) — Copy prompt to clipboard.
- **validate_handoff_scp.py** — SCP validation; use as pre-commit hook when handoff is staged.

## Human Gate

When agent reaches a human gate: write handoff with "Awaiting approval"; next session asks human before proceeding. See [INTENT_ENGINEERING.md](INTENT_ENGINEERING.md).

## Definition of done (P1 — verifiable rewards + dual gates)

When the session produced **substantive code, config, or behavior-changing docs**, add a block (below Next or under Paths):

- **Verification commands run** — e.g. `pytest`, `ruff check`, `mypy`, `npm test`, `npm run build` (project-appropriate). Record **pass / fail**.
- **UI / E2E** — if the change touches UI, note browser or Playwright runs when applicable.
- **Dual gates (multi-file / high-stakes)** — attach or summarize **critic JSON** ([critic-loop-gate.mdc](../.cursor/rules/critic-loop-gate.mdc)) and **intent-alignment JSON** ([intent-alignment-gate.mdc](../.cursor/rules/intent-alignment-gate.mdc)). If `aligned=false` or `escalate=true`, state that the next step requires **human review** before merge.

This aligns “done” with **green CI** (tests/lint/build), not model confidence alone. See [2511.18538-harness-gap-analysis.md](research/2511.18538-harness-gap-analysis.md) § Value-add.

## Public repos

Do not commit **real** handoffs to a public harness fork. Use a **private** `state/` (or private remote) for live handoffs. For teaching the format, see [examples/HANDOFF_EXAMPLE_SYNTHETIC.md](examples/HANDOFF_EXAMPLE_SYNTHETIC.md) and [PUBLIC_AND_PRIVATE_HARNESS.md](PUBLIC_AND_PRIVATE_HARNESS.md).
