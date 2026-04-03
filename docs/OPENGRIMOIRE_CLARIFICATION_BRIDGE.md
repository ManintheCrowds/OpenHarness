# OpenGrimoire clarification queue ↔ OpenHarness

**Purpose:** Correlate **async human answers** to **agent runs** using stable UUIDs from OpenGrimoire (OpenGrimoire app).

## Stable identifier

When an agent creates a clarification request via `POST /api/clarification-requests`, the response includes `item.id` (UUID). Treat this as the canonical join key.

## Handoff convention

In `.cursor/state/handoff_latest.md` or session notes (reference only — not executable):

```text
OPENGRIMOIRE_CLARIFICATION_ID=<uuid>
OPENGRIMOIRE_BASE_URL=https://your-host (default local: http://localhost:3001)
```

Poll until `item.status` is `answered` or `superseded`:

`GET /api/clarification-requests/<uuid>` with:

- **`x-clarification-queue-key`** when OpenGrimoire has **`CLARIFICATION_QUEUE_API_SECRET`** set (recommended for production harnesses that only poll clarification — smaller blast radius than the alignment key), or
- **`x-alignment-context-key`** when using **`ALIGNMENT_CONTEXT_API_SECRET`** and no dedicated clarification secret (same key gates alignment + clarification).

## Optional script

If the OpenGrimoire repo is checked out, use:

`node scripts/poll-clarification.mjs <uuid>`

(from the OpenGrimoire/OpenGrimoire repo root; set **`CLARIFICATION_QUEUE_API_SECRET`** in the environment for the script to send **`x-clarification-queue-key`**, else **`ALIGNMENT_CONTEXT_API_SECRET`** for **`x-alignment-context-key`** — see script header).

## Normative API doc

In your OpenGrimoire clone: `docs/agent/CLARIFICATION_QUEUE_API.md`.

## Distinction

- **OpenHarness:** patterns, state schema, handoff — no clarification HTTP API.
- **OpenGrimoire:** persistence and operator UI for the queue (`/admin/clarification-queue`).
