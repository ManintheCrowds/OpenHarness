# Authority Model

Domain-agnostic framework for gating high-stakes agent actions. Any agent workflow needs a way to distinguish when social approval suffices vs when cryptographic proof is required.

---

## Definitions

### Cryptographic authority

Proof-based, verifiable authority. Private key = proof of ownership; signed actions; capability tokens. Verification is deterministic: anyone can verify a signature or proof without trusting a third party.

### Social/coordination authority

Consensus, reputation, human gates. Identity may be cryptographic but routing and coordination decisions are not proof-based. Verification relies on gossip, reputation, or human approval.

### Pseudoanonymous authority

Authority is provable without revealing real-world identity. Use pubkeys and capability tokens; no PII in verification. Enables audit and delegation without identity disclosure.

---

## When each applies

- **Low-stakes coordination:** Social/coordination authority acceptable. Examples: reversible coordination, documentation, design decisions. Failure modes bounded; no spend, no PII.
- **High-stakes actions:** Cryptographic authority required. Examples: spend, PII access, irreversible actions. Failure modes include theft, harm, or permanent loss.

---

## Authority by risk tier

Aligns with Risk-Tiered Operations:

| Risk Tier | Authority Model | Rationale |
|-----------|-----------------|-----------|
| **Low** | Social/coordination OK | Reversible; no spend, no PII; e.g. coordination, docs |
| **Medium** | Human gate + signed identity | Git tag + backup; two reviewers; identity verified |
| **High** | Cryptographic proof required | Full backup; lead approval; capability tokens, signed actions |
| **Critical** | Full proof chain | Multiple backups; team consensus; capability verification |

**Risk-tier definitions:**

- Low: Git commit, single reviewer
- Medium: Git tag + backup, two reviewers
- High: Full backup + lead approval
- Critical: Multiple backups + team consensus

---

## Capability token concept

For High/Critical tiers, capability tokens provide cryptographic proof of authorization:

- **Issue:** Authority issuer creates token with scope, expiry, holder identity (pubkey)
- **Verify:** Before action, verify token authorizes the action; check scope, expiry, revocation
- **Revoke:** Authority can revoke token; subsequent verification fails

Implementation is project-specific. Harness provides the pattern; your stack (e.g. BFT consensus, on-chain, HSM) provides the implementation.

---

## Integration

- **Hard boundaries:** Use org-intent or equivalent to define when cryptographic proof is required (e.g. "Do not act on behalf of non-owner without cryptographic proof").
- **Capability verification:** Before High/Critical tier actions, call your `verify_capability(token, action_descriptor)` or equivalent. If verification fails, escalate to human.
- **Agent identity:** Agent pubkey (not PII) for audit and capability requests. Private key stored outside AI access.

---

## See also

- [DELINEATION.md](DELINEATION.md) — harness vs portfolio
- [HARNESS_ARCHITECTURE.md](HARNESS_ARCHITECTURE.md) — Guard–Guide–Build taxonomy
