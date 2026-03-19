# Example handoff (synthetic — for pattern only)

**This file is entirely fictional.** It demonstrates the shape of a context handoff for new sessions. Do not treat paths or decisions as real.

---

`Updated: 2026-01-15T18:00:00Z`  
`Session: Demo feature wiring`

## Done

- Added stub API route `GET /api/widgets` returning empty list.
- Documented env var `WIDGETS_API_URL` in README (example repo).
- Ran unit tests for the route; all pass locally.

## Next

- Implement `POST /api/widgets` with validation; add OpenAPI fragment; human must approve schema before merge.
- **Where:** `apps/example-api/src/routes/widgets.ts`
- **Verify:** `npm test` + manual curl per README.

## Paths / artifacts

- `apps/example-api/src/routes/widgets.ts`
- `docs/api/widgets.md`
- `README.md` (env section)

## Decisions / gotchas

- Use zod for request body; reject unknown keys.
- Rate limit deferred to milestone 2.

## Context (optional)

Spike proved SQLite is enough for dev; production TBD.

## Assumptions

- Example org uses Node 20+.

---

_End of synthetic example. Real handoffs belong in private `.cursor/state/` or your org’s equivalent._
