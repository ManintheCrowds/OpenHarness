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
