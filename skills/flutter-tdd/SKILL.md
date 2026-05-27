---
name: flutter-tdd
description: Test-driven development for Flutter/Dart with widget testing and Golden tests
stack: flutter
migrated_from: tdd
---

# Flutter TDD

Stack-specific TDD skill for Flutter/Dart development.

## Triggers
- Writing Flutter widget code
- Adding new features to Flutter apps
- Refactoring Flutter/Dart code

## Workflow
1. Write a failing widget test or unit test
2. Run `flutter test` to confirm failure
3. Write minimal implementation to pass
4. Run `flutter test` to confirm pass
5. Refactor with tests green

## Flutter-specific patterns
- Use `testWidgets()` for widget tests
- Use `pumpWidget()` to render widgets in test
- Use `pump()` and `pumpAndSettle()` for frame updates
- Golden tests with `matchesGoldenFile()`
- Mock providers with `ProviderScope.overrides` or `blocTest`
