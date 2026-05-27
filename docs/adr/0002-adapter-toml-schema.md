# ADR-0002: ADAPTER.toml Manifest Schema

**Status:** Proposed
**Date:** 2026-05-27

## Context

Every adapter must declare its identity, capabilities, and the agents it
provides in a machine-readable manifest. The kit's adapters.toml references
adapters by name and capabilities — the ADAPTER.toml is the adapter's side
of that contract.

## Decision

`ADAPTER.toml` uses the **MCP server card format** extended with a CrewAI-style
agent list:

```toml
name = "flutter-adapter"
version = "1.0.0"
description = "Flutter stack specialist — mobile + web agents, Material Design specs, CocoaPods CI, Shorebird code push"

[author]
name = "Maestro Platform"
url = "https://github.com/maestro-adapters/flutter-adapter"

[[agents]]
role = "screen-builder"
path = "specification/screen-builder.toml"
description = "Translates project briefs into screen specifications"

[[agents]]
role = "widget-composer"
path = "presentation/widget-composer.toml"
description = "Builds Flutter widgets from screen specs"

[[agents]]
role = "state-manager"
path = "application/state-manager.toml"
description = "Designs and implements state management (Riverpod, Bloc)"

[[agents]]
role = "navigation-designer"
path = "application/navigation-designer.toml"
description = "Designs route tables and navigation patterns"

[[agents]]
role = "entity-designer"
path = "domain/entity-designer.toml"
description = "Designs domain entities and value objects"

[[agents]]
role = "theme-builder"
path = "presentation/theme-builder.toml"
description = "Builds Material Design theme from design tokens"

[[agents]]
role = "test-runner"
path = "quality/test-runner.toml"
description = "Runs Flutter tests and reports results"

[[agents]]
role = "code-reviewer"
path = "quality/code-reviewer.toml"
description = "Reviews Flutter/Dart code for best practices"

[[agents]]
role = "build-agent"
path = "delivery/build-agent.toml"
description = "Builds Flutter APK/IPA/web artifacts"

[[agents]]
role = "deploy-agent"
path = "delivery/deploy-agent.toml"
description = "Deploys to app stores, Shorebird, or web hosting"

[[agents]]
role = "env-doctor"
path = "operations/env-doctor.toml"
description = "Validates Flutter/Dart/CocoaPods environment"

[[skills]]
name = "flutter-tdd"
description = "Test-driven development for Flutter/Dart with widget testing"

[[skills]]
name = "flutter-code-review"
description = "Flutter/Dart code review with best practice checks"

[[skills]]
name = "flutter-ui-design"
description = "Flutter Material Design composition patterns"

[[skills]]
name = "flutter-debugging"
description = "Flutter-specific debugging: CanvasKit, widget tree, state inspection"

[[skills]]
name = "flutter-platform-validation"
description = "PlatformView validation on Android and iOS"

[capabilities]
roles = [
  "screen-builder",
  "widget-composer",
  "state-manager",
  "navigation-designer",
  "entity-designer",
  "theme-builder",
  "test-runner",
  "code-reviewer",
  "build-agent",
  "deploy-agent",
  "env-doctor"
]
stacks = ["flutter", "dart"]
platforms = ["ios", "android", "web", "macos", "linux", "windows"]
```

## Rationale

- MCP server card format (`name`, `version`, `description`, `author`) is proven
  and minimal — adapters don't need to invent a discovery format.
- `[[agents]]` table with role+path is the CrewAI pattern: each agent
  declares its abstract role and the relative path to its .toml definition.
- `[[skills]]` is a catalog for discovery, not the runtime config — per
  ADR-0005 (kit), the agent .toml is the single source of truth for which
  skills an agent actually loads.
- `[capabilities]` duplicates the role list but adds `stacks` and `platforms`
  for tooling — `maestro kit install` can filter adapters by stack without
  reading every agent .toml.

## Consequences

- ADAPTER.toml must stay in sync with agent .toml files. Adding a new agent
  requires updating both the agent's .toml and the ADAPTER.toml agents table.
- The `skills` table in ADAPTER.toml is a catalog, not the load list. The
  agent .toml is authoritative for which skills are active.
- `capabilities.roles` and `[[agents]].role` must match. Drift is a detectable
  error at `maestro kit install`.
