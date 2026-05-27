# ADR-0006: Agent .toml Field Schema

**Status:** Proposed
**Date:** 2026-05-27

## Context

Per kit ADR-0005, the agent .toml is the single source of truth for agent
configuration. Every adapter agent needs a consistent schema for its .toml
file — skills, toolsets, model, provider, and adapter-specific metadata.

## Decision

Agent .toml files follow this schema:

```toml
# presentation/widget-composer.toml
[agent]
role = "widget-composer"
description = "Builds Flutter widgets from screen specifications"
layer = "presentation"

[model]
provider = "anthropic"
model = "claude-sonnet-4"

[skills]
names = [
  "flutter-tdd",
  "flutter-ui-design",
  "flutter-code-review"
]

[toolsets]
enabled = [
  "terminal",
  "file",
  "web",
  "delegation"
]

[context]
requires = [
  { role = "screen-builder", output = "screen-spec" },
  { role = "theme-builder", output = "design-tokens" }
]
produces = "widget-tree"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```

**Field definitions:**

| Section | Field | Type | Description |
|---------|-------|------|-------------|
| `[agent]` | `role` | string | Abstract role name, matches ADAPTER.toml |
| `[agent]` | `description` | string | Human-readable description |
| `[agent]` | `layer` | string | DDD layer (presentation, domain, etc.) |
| `[model]` | `provider` | string | LLM provider (anthropic, openai, deepseek) |
| `[model]` | `model` | string | Model identifier |
| `[skills]` | `names` | array | Stack-prefixed skill names (ADR-0004) |
| `[toolsets]` | `enabled` | array | Toolset names enabled for this agent |
| `[context]` | `requires` | array of {role, output} | Upstream agent outputs needed |
| `[context]` | `produces` | string | Output artifact this agent creates |
| `[dependencies]` | `adapters` | array | Other adapters this agent depends on |
| `[dependencies]` | `system_packages` | array | System packages needed (flutter, dart, etc.) |

**All fields optional except `[agent].role`**: Maestro provides sensible
defaults for model, skills, and toolsets. An agent .toml with only `role`
set is valid but underpowered.

## Rationale

- `[context].requires` declares dependency ordering. The orchestrator uses
  this to determine which sub-tickets can run in parallel and which must
  wait for upstream outputs. Without this, every build phase is sequential.
- `[dependencies].system_packages` lets the env-doctor agent validate the
  toolchain before the pipeline runs. If `flutter` isn't installed, the
  pipeline fails fast at phase 7 rather than mid-build at phase 3.
- `[toolsets].enabled` restricts which Hermes tools the agent can use —
  a widget-composer shouldn't need `browser` or `cronjob`. This follows
  the principle of least privilege for agent capabilities.
- `[context].produces` gives the orchestrator a key to look up when a
  downstream agent asks for that output.

## Consequences

- Every adapter agent needs a complete agent .toml. No implicit defaults
  or inheritance from a parent agent.
- The orchestrator uses `[context].requires` to build a dependency graph
  for phase 3 (parallel fan-out) — agents with no dependencies run first,
  dependent agents wait.
- Adding a new agent requires creating its .toml, adding it to ADAPTER.toml,
  and updating ADR-0003 (pipeline phases).
