# Public harness (OpenHarness) vs private workspace

How to split what ships in **OpenHarness** (public reference) from what stays in **private / experimental** repos (e.g. portfolio-harness).

## Roles

| Layer | Typical repo | What belongs here |
|-------|----------------|-----------------|
| **Public reference** | OpenHarness | Patterns, skills, `state/` **schema** description, **synthetic** examples, audit/E2E playbooks, architecture docs |
| **Private / experimental** | portfolio-harness, org-internal forks | Real `.cursor/state/`, `handoff_latest.md`, `handoff_archive/`, `daily/`, credentials, experiment code, OpenAtlas app data |

**Rule of thumb:** If it names real projects, people, internal URLs, or unreleased decisions, **do not** commit it to OpenHarness. Teach the pattern with **fabricated** content instead.

## Handoffs and closeouts

- **Do not** publish real `handoff_latest.md` or archives in OpenHarness.
- **Do** publish a **synthetic** handoff that shows section order, tone, and fields: see [examples/HANDOFF_EXAMPLE_SYNTHETIC.md](examples/HANDOFF_EXAMPLE_SYNTHETIC.md).
- **Persist** real session closeouts in the **private** repo’s `.cursor/state/` (handoff, daily log, decision_index) per that repo’s [HANDOFF_FLOW.md](HANDOFF_FLOW.md) (or equivalent).

## Brain Map and audits

- OpenHarness: standalone viewer + [BRAIN_MAP_AUDIT.md](BRAIN_MAP_AUDIT.md) / [BRAIN_MAP_E2E.md](BRAIN_MAP_E2E.md) (no real graph data required in git).
- portfolio-harness: parser against real `.cursor/state/`, OpenAtlas, optional **BrowserStack scan log** rows with real scan IDs (private unless you redact).

## Operational todos (BrowserStack, etc.)

Tasks that require **your** credentials or internal URLs (e.g. configure BrowserStack MCP, run scans, append to scan logs) are tracked in **private** harness task lists (e.g. portfolio-harness `.cursor/state/pending_tasks.md`, section **PENDING_BRAIN_MAP**). OpenHarness documents *how* to do them, not your secrets or results.

## Forking OpenHarness

Consumers should:

1. Copy `state/` layout from docs, not from your private handoffs.
2. Keep their own `handoff_*` and `daily/` out of public forks (or use a private remote for state).
