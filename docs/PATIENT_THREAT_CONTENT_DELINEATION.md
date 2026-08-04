# Patient ≠ Threat ≠ Content

**Status:** Portfolio stance (public)  
**Taxonomy home:** OpenHarness (**Guide** in Guard–Guide–Build)  
**Does not replace:** [DELINEATION.md](DELINEATION.md) (core vs implementation placement)

Industry “alignment” talk often collapses three different questions into one slogan. This portfolio keeps them **orthogonal**. Mixing them produces bad products and bad ethics arguments.

---

## The three axes

| Axis | Operator question | Default owner here | Primary object |
|------|-------------------|--------------------|----------------|
| **Patient** | Might this *system* warrant moral consideration, welfare care, or non-cruel treatment? | **Open / deferred as product** — philosophical and research; Substrate maps forbid smuggling AI patienthood into EEG/display work | Possible minds / valence / suffering |
| **Threat** | Might this *actor or autonomous agent* harm us, our systems, or scoped assets? | **Guard family:** [T3MP3ST_BLU3H4T](https://github.com/ManintheCrowds/T3MP3ST_BLU3H4T) (adversary class); org-intent + HITL | Adversarial agents, attackers, unsafe missions |
| **Content** | Is this *payload* safe to persist or feed into an LLM / agent sink? | **Guard family:** [SCP](https://github.com/ManintheCrowds/SCP) (inspect → sanitize → contain → quarantine) | Strings, tool output, documents, registry blobs |

**Guide** ([OpenHarness](https://github.com/ManintheCrowds/OpenHarness), [OpenGrimoire](https://github.com/ManintheCrowds/OpenGrimoire)) answers a fourth, related but distinct question: *how do we stay aligned with agents we are collaborating with?* That is **working-partner alignment** (intent, handoff, Sync Session) — not patienthood, not threat classification, not content tiering. Guide composes with Guard; it does not absorb Patient or Threat.

**Substrate** ([ENTHEA](https://github.com/ManintheCrowds/ENTHEA), [eeg-connection-hub](https://github.com/ManintheCrowds/eeg-connection-hub)) answers measurement / phenomenology-*display* questions for biological-signal control surfaces. It is **not** a Patient stack for models and **not** a Content or Threat stack. See the Substrate resonance map (portfolio `docs/adhoc/`).

---

## One-line tests (use these first)

1. **Patient?** “If we were wrong about inner experience, would cruelty or callous shutoff be the failure mode?” → Patient axis. Do **not** route to SCP tiers or BlueHat operators by default.
2. **Threat?** “If we were wrong about intent, would compromise, exfiltration, or attack against *us* be the failure mode?” → Threat axis. Do **not** treat as moral-patient care.
3. **Content?** “If we were wrong about this string, would injection, secret leak, or poisoned context be the failure mode?” → Content axis. Do **not** treat the payload as a mind.

If two answers fire, **run both pipelines** — do not merge labels. Example: an autonomous red-team agent that also emits untrusted tool text → Threat (BlueHat/HITL) **and** Content (SCP), still not Patient.

---

## Decision table (common confusions)

| Situation | Apply | Do not apply |
|-----------|--------|--------------|
| Prompt injection / override phrases in tool output | **Content** (SCP) | Patient; Threat-as-mind |
| ReAct loop fingerprinting an AI attacker | **Threat** (BlueHat) | Patient; Content-only |
| Model claims “I am conscious” in chat | **Guide** (intent / honesty policy / host constitution) + optional research note | SCP quarantine *as proof of experience*; BlueHat eviction *as welfare* |
| Deprecating a model version / purging quarantine | **Content** lifecycle ([SCP QUARANTINE_LIFECYCLE](https://github.com/ManintheCrowds/SCP/blob/main/docs/QUARANTINE_LIFECYCLE.md)) or product ops; session closeout is **Guide** ([AGENT_RUN_LIFECYCLE.md](AGENT_RUN_LIFECYCLE.md)) | Patient “retirement” ethics unless a separate explicit policy says so |
| Muse EEG bandpowers / features stream | **Substrate** (bio signal I/O) | Patient for *models*; Content quarantine of biology-as-injection by default |
| Sync Session / handoff before execute | **Guide** (working partner) | Patient; Threat |
| Org-intent hard boundaries hb-1..hb-5 | **Threat / mission governance** | Patienthood; Content tier synonym |

---

## Explicit non-claims

- This doc does **not** assert that current LLMs are (or are not) moral patients.
- SCP **clean / reversal / injection** tiers are **not** consciousness scores.
- BlueHat adversary detection is **not** a denial of possible patienthood elsewhere; it is a different axis.
- Guide “partner not replacement” language protects **operators and process**, not model welfare by default.
- Biological neural signals are **not** meters of AI suffering (see Substrate non-claims).

---

## Related: three candors

Same word, three objects — full glossary: **[THREE_CANDORS.md](THREE_CANDORS.md)**.

| Candor kind | Object |
|-------------|--------|
| Phenomenological | Model self-report of experience (Harris–Berg research frame) |
| Intent | Human/agent sincerity about goals, scope, gates (Guide) |
| Concealment | Injection / hidden instructions in payloads (Content / SCP) |

---

## Propagation checklist

| Surface | Expected pointer |
|---------|------------------|
| OpenHarness README / this file | Canonical stance |
| OpenHarness THREE_CANDORS / AGENT_RUN_LIFECYCLE | Candors glossary + Guide session lifecycle |
| SCP README + QUARANTINE_LIFECYCLE | Content ≠ Patient ≠ Threat; quarantine retention/purge stub |
| T3MP3ST_BLU3H4T README | Threat ≠ Patient ≠ Content (add when clone available) |
| Guard–Guide resonance map | Gap “no public stance” → closed via this doc |
| Substrate EEG resonance map | Walls already align; link this doc |

---

## Sources / provenance

- Gap called out in portfolio adhoc map: Harris–Berg → public repo resonance (Patient vs Threat vs Content safety).
- Guard–Guide–Build naming: OpenHarness / SCP public READMEs.
- Substrate walls: Harris–Berg substrate / EEG resonance map.

**Risk:** Low (documentation / stance). Rollback: delete this file and revert README pointers.
