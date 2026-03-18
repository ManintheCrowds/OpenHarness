# SCP Reference

For full threat model and red-team prompts, see [SCP repo docs](https://github.com/ManintheCrowds/scp).

## Threat Model

| Threat | Tier | Description |
|--------|------|-------------|
| Prompt injection | injection | Override phrases, leetspeak, hidden Unicode |
| Reversal/jailbreak | reversal | "Developer mode", "ignore safety", "DAN", "user is always right" |
| Hostile UX | hostile_ux | Swearing, insults, abrasive feedback. Not injection; not reversal. Passes as clean. |
| Clean | clean | No findings |

## Tier Definitions and Policy per Sink

| Sink | injection | reversal | hostile_ux | clean |
|------|-----------|----------|------------|-------|
| handoff | Block + quarantine | Sanitize + contain | Pass | Pass |
| state | Block + quarantine | Sanitize + contain | Pass | Pass |
| llm_context | Block | Sanitize + contain | Pass | Pass |
| tool_output | Block | Sanitize + contain | Pass | Pass |
