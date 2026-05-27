# ADR-0003: Flutter Pipeline Phases and Agent Roles

**Status:** Proposed
**Date:** 2026-05-27

## Context

The kit pipeline (phases.toml) defines abstract phases with abstract agent
roles. The flutter-adapter must declare which concrete agents implement those
roles, and which pipeline phases are relevant to Flutter development.

## Decision

The flutter-adapter provides agents for these pipeline phases:

| Phase | Role | Agent | Layer |
|-------|------|-------|-------|
| 1. Specify | `requirement-analyst` | requirement-analyst | discovery |
| 2. Design | `screen-builder` | screen-builder | specification |
| 3. Build | `widget-composer` | widget-composer | presentation |
| 3. Build | `state-manager` | state-manager | application |
| 3. Build | `navigation-designer` | navigation-designer | application |
| 3. Build | `entity-designer` | entity-designer | domain |
| 3. Build | `theme-builder` | theme-builder | presentation |
| 4. Verify | `test-runner` | test-runner | quality |
| 4. Verify | `code-reviewer` | code-reviewer | quality |
| 5. Package | `build-agent` | build-agent | delivery |
| 6. Deploy | `deploy-agent` | deploy-agent | delivery |
| 7. Operate | `env-doctor` | env-doctor | operations |

**Key design decisions:**

- **Phase 3 (Build) runs multiple agents in parallel**: widget-composer,
  state-manager, navigation-designer, entity-designer, and theme-builder work
  on different concerns simultaneously. The orchestrator fans out sub-tickets
  and collects results.
- **Phase 4 (Verify) runs sequentially**: test-runner first (all tests must
  pass), then code-reviewer (review passes code). If tests fail, code review
  is skipped.
- **Phase 7 (Operate) is a validation gate**, not a build step: env-doctor
  validates the Flutter/Dart/CocoaPods environment and produces a readiness
  report.

## Rationale

- Phase 3 parallelization reflects how Flutter development actually works:
  widgets, state, navigation, entities, and theming are independent concerns
  that can be built concurrently. A single "screen-builder" trying to do all
  five would be slow and error-prone.
- Sequential verification (test → review) is standard CI practice: don't
  review code that doesn't compile or pass tests.
- Environment validation at phase 7 catches misconfigured toolchains before
  the next pipeline run, not during it.

## Consequences

- The orchestrator must support fan-out/fan-in for phase 3: dispatch 5
  sub-tickets, wait for all to complete, merge results.
- Agent .toml files for phase 3 agents must declare their input dependencies
  — widget-composer depends on screen-builder's output, theme-builder depends
  on design tokens from specification.
- Adding a new Flutter agent (e.g., `animation-designer`) means updating this
  ADR, ADAPTER.toml, and the agent .toml.
