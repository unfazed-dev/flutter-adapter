# ADR-0001: DDD+Croft Package Layout

**Status:** Proposed
**Date:** 2026-05-27

## Context

The flutter-adapter needs a directory structure that is consistent across all
adapters, aligns with domain-driven design principles, and accommodates
agent-per-layer nesting. The structure must support both the four Evans DDD
layers and the James Croft agent-per-layer nesting model.

## Decision

The adapter uses a **nine-directory layout** combining Evans' four DDD layers
with additional lifecycle concerns:

```
flutter-adapter/
├── ADAPTER.toml              # Adapter manifest (ADR-0002)
├── specification/            # Evans: none (auxiliary)
│   ├── screen-builder.toml   # Agent definition
│   ├── skills/               # Agent-owned skills
│   └── templates/            # Agent-owned templates
├── discovery/                # Evans: none (auxiliary)
│   ├── requirement-analyst.toml
│   ├── skills/
│   └── templates/
├── domain/                   # Evans: Domain Layer
│   ├── entity-designer.toml
│   ├── value-object-builder.toml
│   ├── skills/
│   └── templates/
├── application/              # Evans: Application Layer
│   ├── state-manager.toml
│   ├── navigation-designer.toml
│   ├── skills/
│   └── templates/
├── infrastructure/           # Evans: Infrastructure Layer
│   ├── persistence/
│   │   ├── storage-agent.toml
│   │   ├── skills/
│   │   └── templates/
│   └── ci/
│       ├── ci-agent.toml
│       ├── skills/
│       └── templates/
├── presentation/             # Evans: Presentation/UI Layer
│   ├── widget-composer.toml
│   ├── theme-builder.toml
│   ├── skills/
│   └── templates/
├── quality/                  # Evans: none (auxiliary)
│   ├── test-runner.toml
│   ├── code-reviewer.toml
│   ├── skills/
│   └── templates/
├── delivery/                 # Evans: none (auxiliary)
│   ├── build-agent.toml
│   ├── deploy-agent.toml
│   ├── skills/
│   └── templates/
├── operations/               # Evans: none (auxiliary)
│   ├── env-doctor.toml
│   ├── skills/
│   └── templates/
└── context-map.toml          # Bounded context relationships
```

- **Nine top-level directories**: specification, discovery, domain, application,
  infrastructure, presentation, quality, delivery, operations.
- **Agent-per-layer nesting**: each layer directory contains agent `.toml`
  files, plus `skills/` and `templates/` subdirectories owned by those agents.
- **context-map.toml**: defines how bounded contexts interact (which agents
  depend on which other agents' outputs).

## Rationale

- Evans' four layers (domain, application, infrastructure, presentation)
  provide well-understood separation of concerns in software design.
- Five auxiliary layers (specification, discovery, quality, delivery,
  operations) cover the full app lifecycle beyond Evans' core four.
- Croft's agent-per-layer nesting makes each agent self-contained: its
  skills and templates live in its layer directory, not in a shared pool.
  This prevents skill name collisions and makes adapters independently
  portable.
- `context-map.toml` is the DDD strategic pattern for declaring bounded
  context relationships — applied here to agent dependency chains.

## Consequences

- Every adapter follows the same layout, making inspection and tooling
  predictable.
- Agent skills are scoped to their layer — no cross-layer skill leaking.
- Domain adapters (invoice, payroll) may omit layers they don't need
  (e.g., an invoice-adapter might only use domain + infrastructure).
- Layer names map to pipeline phases: specification → discovery → domain
  → application → infrastructure → presentation → quality → delivery →
  operations.
