# ADR-0007: Design System Architecture — HIG/M3 Split, Stacked MVVM, and Deterministic Pipeline

**Status:** Accepted
**Date:** 2026-05-29
**Deciders:** Architecture grilling session (Q1–Q13)

## Context

The flutter-adapter was built with 17 generic agents — a single `theme-builder` generating Material Design themes, a single `widget-composer` building Flutter widgets, and a single `design-critic` reviewing both HIG Liquid Glass and M3 Expressive Alpha. This generic-agent pattern contradicts the specialist-agent principle established in the kit's Q1 decision. Meanwhile, the PlatformView infrastructure demonstrated that native embeds (SwiftUI `glassEffect` on iOS, Compose on Android) produce pixel-perfect fidelity that standard Flutter widgets cannot match.

The adapter also lacks a deterministic generation model. Running the same design through the pipeline twice produces functionally similar but not provably identical output. For production vertical kits, operators need the guarantee: same design in, same application out, every time.

## Decision

### Design system architecture (Q1–Q5, Q8)

The presentation pipeline splits by design system with three rendering modes controlled by operator `tier` and `mode` parameters:

- **spec-author** stays design-system-agnostic — generates abstract specs from primitives.
- **hig-theme-builder** + **m3-theme-builder** + **shadcn-theme-builder**: three specialist theme-builders for iOS/HIG (Cupertino + Liquid Glass), Android/M3 (tonal palettes, elevation), and web/desktop (shadcn_flutter).
- **hig-widget-composer** + **m3-widget-composer** + **shadcn-widget-composer** + **replica-widget-composer**: four specialist widget-composers. HIG/M3/Shadcn handle default and baseline modes. Replica handles pure Flutter pixel-perfect output.
- **hig-design-critic** + **m3-design-critic**: two specialist critics. HIG critic validates Liquid Glass correctness, Cupertino conformance, iOS deviations (toast→dialog). M3 critic validates tonal palettes, elevation, state layers. Replica mode has no design-critic — the mockup is the spec.

Rendering modes:
- **default** (`tier=default`): native widget skeleton (SwiftUI/Compose/shadcn) skinned with design tokens. Tier 1 fidelity.
- **baseline** (`tier=baseline`): native widget skeleton with conservative materials — standard Cupertino, standard M3 elevation. Tier 2/3 fidelity. Mode switch on existing composers, not new agents.
- **replica** (`mode=replica`): pure Flutter pixel-perfect, no native widgets. Design is the single source of truth.

Rendering approach for default/baseline is hybrid: PlatformView native embeds (UiKitView/AndroidView) for visual-critical primitives (Card, Button, Dialog), standard Flutter widgets for the rest.

### Architecture pattern (Q6)

All generated code uses **Stacked** — a production MVVM framework aligned with Flutter's official architecture recommendation (Views + ViewModels + Repositories + Services + optional Domain layer). Built by FilledStacks (30+ production apps, 52.5k weekly downloads). Ships its own CLI (`stacked create app`) that scaffolds the project skeleton. Agents fill ViewModels and Services within the structured output.

### Stacked within DDD (Q11)

Feature-first layout where each DDD bounded context becomes a feature folder:

```
lib/features/<context>/
├── ui/views/          # Stacked Views (widgets)
├── ui/viewmodels/     # Stacked ViewModels (BaseViewModel)
├── domain/            # DDD entities, value objects (pure Dart, no Flutter)
├── data/repositories/ # Stacked-compatible, get_it registered
├── data/services/     # Stacked services
└── application/       # DDD commands/queries
```

Every agent in the application layer and below loads the `flutter-stacked` skill for Stacked pattern awareness.

### Skill split (Q7, Q9)

The `flutter-ui-design` skill splits into three layered skills:
- `flutter-ui-design` (shared): layout composition, responsive patterns, widget lifecycle.
- `flutter-hig-design` (HIG extension): Cupertino widgets, Liquid Glass tokens, iOS deviations.
- `flutter-m3-design` (M3 extension): Material widgets, tonal palettes, elevation.

New skills: `flutter-stacked` (Stacked MVVM patterns), `flutter-platformview` (PlatformView generation — UiKitView/AndroidView factories, MethodChannel bridges, view type registration). Total skills: 8 (from original 5).

### Agent inventory (Q10)

25 agents total. 17 original → 3 split (theme-builder → 3, widget-composer → 4, design-critic → 2) → 23. Plus `stacked-scaffolder` (scaffolds the Stacked project skeleton) and `idempotency-verifier` (runs probe-runner for golden-spec and snapshot-idempotency validation). Pipeline per mode:

- iOS: spec-author → hig-theme-builder(tier) → hig-widget-composer(tier) → hig-design-critic(tier)
- Android: spec-author → m3-theme-builder(tier) → m3-widget-composer(tier) → m3-design-critic(tier)
- Web/Desktop: spec-author → shadcn-theme-builder → shadcn-widget-composer → m3-design-critic
- Replica: spec-author → replica-widget-composer (no theme-builder, no design-critic)

### Determinism model (Q13)

Eight-layer model ensuring same design input produces functionally identical application output:

1. **Deterministic scaffolding** — `stacked create app` CLI, zero AI invocation.
2. **Schema-constrained generation** — structured `design-analysis.json` constrains agent prompts.
3. **Adapter table mapping** — intent/motion/visual tables are deterministic lookups, not AI judgment.
4. **Golden-spec validation** — `idempotency-verifier` runs probe-runner: captures design mockup skeleton + tokens → design_bundle; captures generated app skeleton → app_bundle; diffs via `skeleton_diff` (IoU ≥ 0.98, position ≤ 1px).
5. **Idempotent pipeline** — stable import ordering, no UUIDs, no timestamps, deterministic file naming.
6. **Snapshot-idempotency gate** — pipeline runs twice on same input; verifier diffs both output bundles; certified:true only when identical.
7. **Compiled primitives** — agent generates each primitive once; probe-runner certifies; output stored as compiled artifact. Same input → compiled output reused (zero LLM tokens). Input changes → regenerate. Replaces hand-coded templates with self-compiling system.
8. **Canonical output formatter** — build script normalizes imports, `dart format`, file ordering.

## Rationale

- **Specialist over generic**: The kit's Q1 decision established that specialist agents per stack reduce hallucination and match industry practice. The same principle applies within a stack — HIG and M3 are different design systems with different token vocabularies, material models, and platform behaviors. A single agent context-switching between them is the generic pattern we rejected.
- **Stacked over plain MVVM**: Flutter officially recommends MVVM but provides no framework. Stacked provides the CLI, service registration, routing, and testability patterns that the agent would otherwise generate boilerplate for. Less code to generate = fewer agent mistakes.
- **DDD for swapability**: The domain layer is pure Dart with no Flutter imports. Changing the UI framework (Stacked → BLoC) or the entire stack (Flutter → Dioxus) preserves the domain model. This is the adapter-swap promise: same bounded contexts, different technology.
- **Compiled primitives over hand-coded templates**: Hand-coding 10 primitive templates is up-front cost that grows with each new primitive. The compiled approach automates this — the system discovers and locks the stable output, reusing it deterministically. The LLM is a compiler, not a runtime.
- **Probe-runner as validation substrate**: `skeleton_diff` provides mechanical proof that two outputs match (IoU, position, sizing, font) without relying on LLM judgment. Validation is deterministic code, not another AI step. This follows the Compiled AI insight: validation must be programmatic.

## Consequences

**Positive:**
- Deterministic pipeline: same design in, functionally identical app out. Operator trust.
- Specialist agents per design system reduce hallucination and produce platform-appropriate code.
- DDD architecture enables UI framework swap and stack swap without domain model changes.
- Compiled primitives eliminate repeated LLM token costs for stable 1:1 mappings.
- Probe-runner integration provides mechanical proof of output correctness and idempotency.

**Negative:**
- 25 agents (up from 17) with more TOML configuration, more pipeline branches to maintain.
- New skills (flutter-stacked, flutter-platformview, flutter-hig-design, flutter-m3-design) must be authored.
- `flutter_skeleton` in probe-runner is roadmap — native skeleton capture not built yet. Full determinism verification requires closing this gap.
- Stacked is a third-party dependency with maintenance risk (single maintainer, weekly schedule).

**Risks:**
- **Stacked maintenance risk**: single maintainer with weekly schedule. Mitigation: the architecture pattern (MVVM) is standard — migration path to plain MVVM exists if Stacked is abandoned. Domain layer is unaffected.
- **Probe-runner native skeleton gap**: `flutter_skeleton` is not built. Web targets verified today; iOS/Android native verification deferred. Mitigation: web targets cover the critical path; native skeleton prioritized in probe-runner roadmap.
- **Agent count complexity**: 25 agents require careful pipeline orchestration. Mitigation: the mode/tier parameters route deterministically — no runtime agent selection needed. The spec-author is the single entry point.
- **Compiled primitive staleness**: compiled artifacts can drift from current adapter tables. Mitigation: adapter table changes trigger automatic invalidation and regeneration of affected compiled primitives.
