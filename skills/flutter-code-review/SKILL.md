---
name: flutter-code-review
description: Code review checklist for Flutter/Dart — widget composition, state management, DDD layer discipline, accessibility, and performance
stack: flutter
migrated_from: code-review
---

# Flutter Code Review

Code review checklist specialized for Flutter/Dart applications. Covers widget composition patterns, state management correctness, DDD layer boundaries, accessibility, performance, and Dart best practices.

## Triggers

- Reviewing a Flutter PR or commit
- Pre-merge code review
- Code quality gate checks
- Peer review of Flutter widget or state management code

## Workflow

1. Load the file(s) under review
2. Run through the checklist below
3. Flag violations with file path, line number, and suggested fix
4. Re-check after fixes are applied

## Checklist

### DDD Layer Discipline
- [ ] Domain layer has no Flutter imports (`package:flutter`)
- [ ] Application layer has no widget code — only state management (Riverpod providers, Bloc cubits)
- [ ] Presentation layer has no direct data fetching — goes through application or infrastructure layer
- [ ] Infrastructure layer has no UI dependencies

### Widget Composition
- [ ] Widgets are small (< 200 lines) — extract reusable sub-widgets
- [ ] No `setState` in widgets with business logic — use Riverpod/Bloc
- [ ] `const` constructors used where possible
- [ ] `build()` methods have no side effects (API calls, navigation)
- [ ] Keys used correctly for stateful widgets in lists (`ValueKey`, not `UniqueKey` everywhere)

### State Management
- [ ] Riverpod: providers are `autoDispose` where appropriate
- [ ] Riverpod: no `ref.watch` inside `build()` for providers that trigger rebuilds unnecessarily
- [ ] Bloc: events and states are sealed classes (not strings/enums for dispatch)
- [ ] State is lifted to the lowest common ancestor — no prop drilling

### Performance
- [ ] `ListView.builder` (not `ListView`) for long lists
- [ ] No `Opacity` widgets where `Visibility` or `AnimatedOpacity` would work
- [ ] `const` widgets in build methods (avoids rebuilds)
- [ ] `RepaintBoundary` used for complex animations and charts
- [ ] Images cached with `cached_network_image`

### Accessibility
- [ ] `Semantics` labels on interactive widgets (`Semantics(label: 'Submit')`)
- [ ] `ExcludeSemantics` on decorative elements
- [ ] Contrast ratio ≥ 4.5:1 for text, ≥ 3:1 for large text
- [ ] Interactive targets are ≥ 48x48 logical pixels
- [ ] Text scales properly with `MediaQuery.textScaleFactor`

### Dart Best Practices
- [ ] `final` over `var` where possible
- [ ] No `dynamic` unless absolutely necessary
- [ ] Null safety: no `!` on potentially null values without prior check
- [ ] `late` only when guaranteed initialized before use
- [ ] Exported barrel files for public API surface
- [ ] No `print()` — use a logger (e.g. `package:logging`)

### Testing
- [ ] New code has corresponding widget or unit tests
- [ ] Golden tests exist for visual changes
- [ ] Tests don't depend on real network calls — mocks or fakes

## Commands

```bash
# Run Dart analyzer
flutter analyze

# Run tests
flutter test

# Check unused files/code
dart run dart_code_metrics:metrics analyze lib/

# Check dependency health
flutter pub outdated
```

## Pitfalls

- **Don't block PR on style nits**: Use `flutter format` (dart format) and CI enforcement for style. Reviews focus on logic, architecture, and correctness.
- **DDD violations are blocking**: A domain entity importing `package:flutter/material.dart` is a hard fail — architecture violations compound fast.
- **Accessibility is not optional**: Missing `Semantics` on interactive elements blocks the `design-critic` gate.
- **Performance regressions**: `ListView` (non-builder) with > 50 items is a blocking issue for release builds.
