# Agent entry — OpenHarness (one screen)

**Start here** if you are an agent (or human wiring an agent) using this repo as a **bundle**: markdown, scripts, `state/`, `.cursor/skills/` — not a web app. Follow this chain in order.

---

## 1. Capability manifest

**[`capabilities.harness.yaml`](../capabilities.harness.yaml)** — Machine-readable inventory: `harness_capability.scripts` (must match on-disk scripts), globs, pointers to the checklist, and links into docs. Run `python scripts/verify_script_index.py` after changing scripts or the manifest.

---

## 2. Scripts and parity

**[`CHEATSHEET.md`](CHEATSHEET.md)** — One-page harness map; **Agent invocation index** lists each script with purpose and example invocation. This is the canonical **human + agent** script table (keep it in sync with the manifest).

---

## 2b. Session bootstrap

**[`SESSION_BOOTSTRAP.md`](SESSION_BOOTSTRAP.md)** — What to load first in a new session (intent → handoff → preferences → rejection_log → decision-log → known-issues → daily), aligned with CHEATSHEET **Memory load order**. Checklist → paths: **[`OPENHARNESS_CONTEXT_MAP.md`](OPENHARNESS_CONTEXT_MAP.md)**.

---

## 2c. Slash commands (Cursor) and agent parity

- **Human:** Runs `/architect` or `/agent-native-audit` in the Cursor command palette.
- **Agent:** Reads the same workflow from **[`.cursor/commands/`](../.cursor/commands/)** (e.g. `architect.md`, `agent-native-audit.md`) and executes the documented steps. Treat **open command file + follow** as equivalent to invoking the slash command.

---

## 3. Handoff and continue

**[`HANDOFF_FLOW.md`](HANDOFF_FLOW.md)** — How to archive, write `handoff_latest`, use the continue prompt, and respect trust boundaries (SCP / pre-commit). For a fuller local procedure when the portfolio workspace is checked out, see the path note in HANDOFF_FLOW to sibling **`MiscRepos`** `HANDOFF_FLOW.md`.

---

## 3b. OpenGrimoire clarification queue (optional)

If you use **OpenGrimoire**  for async agent→human questions, stable UUIDs and handoff conventions live in **[`OPENGRIMOIRE_CLARIFICATION_BRIDGE.md`](./OPENGRIMOIRE_CLARIFICATION_BRIDGE.md)**. OpenHarness does not host this API; it is the join key between harness runs and Grimoire.

## 4. State on disk

**[`state/`](../state/)** — Schema and files agents and humans share: `handoff_latest.md`, `decision-log.md`, `continue_prompt.txt`, `daily/`, etc. Read **[`state/README.md`](../state/README.md)** for layout. After a handoff, load **handoff** → **preferences** → **rejection_log** as in CHEATSHEET **Memory load order**.

---

## Quick commands (from repo root)

```text
python scripts/verify_script_index.py
python scripts/verify_skills_readme.py
```

See also: [AGENT_NATIVE_CHECKLIST.md](AGENT_NATIVE_CHECKLIST.md), [HARNESS_AUDIT_ALIGNMENT.md](HARNESS_AUDIT_ALIGNMENT.md). **Portfolio GUI surfaces** (browser apps / generated HTML): onboarding checklist in sibling MiscRepos [docs/audit/NEW_GUI_SURFACE_CHECKLIST.md](../../MiscRepos/docs/audit/NEW_GUI_SURFACE_CHECKLIST.md) (path from repo root: `../MiscRepos/docs/audit/NEW_GUI_SURFACE_CHECKLIST.md` when OpenHarness and MiscRepos are siblings).
