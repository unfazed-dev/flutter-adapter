# ADR-0004: Flutter Skill Naming Convention

**Status:** Proposed
**Date:** 2026-05-27

## Context

Skills must be split into cross-cutting methodology skills (stay in the
Maestro skill registry) and stack-specific skills (move to adapters). Adapter
skills need a naming convention that prevents collisions and makes the stack
ownership immediately obvious.

## Decision

All stack-specific skills in adapters follow the **`{stack}-{skill}`** naming
convention:

| Generic Skill | Flutter-Adapter Skill |
|---------------|----------------------|
| `tdd` | `flutter-tdd` |
| `code-review` | `flutter-code-review` |
| `ui-design` | `flutter-ui-design` |
| `debugging` | `flutter-debugging` |
| `platform-validation` | `flutter-platform-validation` |
| `env-doctor` | `flutter-env-doctor` |

**Cross-cutting skills stay in Maestro skill registry** — no stack prefix:

- `superpowers-brainstorming`
- `superpowers-verification`
- `superpowers-systematic-debugging`
- `post-mortem`
- `pre-mortem`
- `security-first`
- `readme-generator`

## Rationale

- Stack prefix prevents skill name collisions when multiple adapters are
  installed in the same kit. `flutter-tdd` and `supabase-tdd` can coexist
  without ambiguity.
- The prefix makes ownership immediately obvious in logs and tickets: seeing
  `flutter-tdd` in a pipeline trace tells you exactly which adapter provided
  it.
- Cross-cutting skills don't get a prefix because they're not stack-specific.
  A `post-mortem` is the same process whether the project is Flutter or
  Svelte.

## Consequences

- All adapter skill references in agent .toml files must use the prefixed
  name: `skills = ["flutter-tdd", "flutter-code-review"]`.
- When migrating existing skills to adapters, rename them with the stack
  prefix.
- The Maestro skill registry must distinguish between cross-cutting skills
  (no prefix, platform-owned) and adapter skills (prefixed, adapter-owned).
