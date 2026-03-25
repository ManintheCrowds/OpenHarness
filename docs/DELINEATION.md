# Core vs Implementation Delineation

Decide whether a component belongs in the **core** (portable, reusable) or **implementation** (your project, domain-specific). In this repo: core = harness; implementation = your project.

## Primary Prompt (use first)

> **"Would any developer be able to use this in their own project without context from other projects?"**
> - **Yes** → candidate for core
> - **No** → stays in implementation

## Secondary Prompts (when primary is ambiguous)

Adapt these to your stack. For harness:

| Question | Core | Implementation |
|----------|------|-----------------|
| Does this depend on a specific domain? | No | Yes |
| Is this a platform-agnostic pattern? | Yes | No |
| Would removing this break a minimal setup for a new user? | Yes | No |
| Is this a security baseline that applies broadly? | Yes | No (domain-specific) |
| Does this reference project-specific integrations not in the core baseline? | No | Yes |
| Is this a convention or preference? | No | Yes |

## Rule of Thumb

- **Core** = portable, reusable, minimal setup.
- **Implementation** = your project, preferences, domain-specific integrations.

**Script inventory:** Do not maintain a second long script table in the root README. The canonical list is [CHEATSHEET.md](CHEATSHEET.md) (Agent invocation index) plus [capabilities.harness.yaml](../capabilities.harness.yaml); [README.md](../README.md) points there by design.

## Checklist for New Components

1. Run primary prompt.
2. If unclear, run secondary prompts (adapt questions to your context).
3. If still unclear: start in implementation; promote to core when it proves reusable.

## Promotion Checklist (implementation → core)

Before promoting a component:

- [ ] Primary delineation prompt passes
- [ ] No references to implementation-specific projects or integrations
- [ ] Dependencies documented
- [ ] Paths use generic placeholders
- [ ] README or docs updated if it adds new concepts

## Reusing This Pattern

Copy this doc and replace "core" / "implementation" with your names (e.g. framework vs app, upstream vs fork). The primary prompt stays the same; adapt the secondary prompts to your stack.
