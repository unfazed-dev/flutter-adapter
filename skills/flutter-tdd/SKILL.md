---
name: flutter-tdd
description: Test-driven development for Flutter/Dart — widget tests, Golden tests, unit tests, and integration tests with Riverpod/Bloc state management
stack: flutter
migrated_from: tdd
---

# Flutter TDD

Test-driven development workflow tailored for Flutter/Dart applications. Covers widget testing, Golden image tests, unit testing for state management (Riverpod/Bloc), and integration testing.

## Triggers

- Writing Flutter widget code
- Adding new features to Flutter apps
- Refactoring Flutter/Dart code
- Creating or modifying Riverpod providers or Bloc states
- Building custom widgets

## Workflow

### Red phase
1. Identify the behavior: a widget render, a state transition, a user interaction
2. Write the minimal failing test first
3. Run `flutter test` to confirm RED

### Green phase
1. Write the minimal implementation to make the test pass
2. Run `flutter test` again — must be GREEN
3. No premature abstraction or optimization

### Refactor phase
1. Clean up implementation while tests stay green
2. Extract reusable widgets, providers, or helpers
3. Run full test suite: `flutter test`

## Commands

```bash
# Run all tests
flutter test

# Run a specific test file
flutter test test/widgets/my_widget_test.dart

# Run a specific test by name
flutter test --name "should render correctly"

# Run with coverage
flutter test --coverage

# Generate Golden image files (first run creates them)
flutter test --update-goldens

# Run on a specific device (integration tests)
flutter test integration_test/
```

## Widget Testing Patterns

```dart
// Basic widget test
testWidgets('MyWidget renders title', (tester) async {
  await tester.pumpWidget(
    MaterialApp(home: MyWidget(title: 'Hello')),
  );
  expect(find.text('Hello'), findsOneWidget);
});

// Provider-scoped widget test
testWidgets('Counter increments on tap', (tester) async {
  await tester.pumpWidget(
    ProviderScope(
      child: MaterialApp(home: CounterPage()),
    ),
  );
  await tester.tap(find.byIcon(Icons.add));
  await tester.pump();
  expect(find.text('1'), findsOneWidget);
});

// Golden image test
testWidgets('Button golden', (tester) async {
  await tester.pumpWidget(
    MaterialApp(home: Scaffold(body: MyButton('Submit'))),
  );
  await expectLater(
    find.byType(MyButton),
    matchesGoldenFile('goldens/my_button.png'),
  );
});
```

## Riverpod Testing

```dart
// Provider test with ProviderContainer
test('counterProvider increments', () {
  final container = ProviderContainer();
  addTearDown(container.dispose);
  final notifier = container.read(counterProvider.notifier);
  notifier.increment();
  expect(container.read(counterProvider), 1);
});

// Async provider test
test('userProvider fetches user', () async {
  final container = ProviderContainer(
    overrides: [apiServiceProvider.overrideWith(MockApiService())],
  );
  addTearDown(container.dispose);
  final user = await container.read(userProvider.future);
  expect(user.name, 'Test User');
});
```

## Pitfalls

- **Golden tests are platform-sensitive**: Goldens generated on macOS will fail on Linux CI. Use `skip: Platform.isLinux` or check in Linux goldens separately.
- **Pump vs pumpAndSettle**: `pumpAndSettle` waits for all animations to complete — use `pump()` with a specific duration for animated widgets to avoid timeouts.
- **MaterialApp wrapper**: Most widget tests need a `MaterialApp` or `Material` ancestor for `TextDirection` and theming. Wrap with `wrapWithMaterial()` helper.
- **Riverpod overrides must have matching types**: `overrideWith` requires the exact provider type — use `ProviderScope(overrides: [...])` at the test root, not `ProviderScope` per test.
- **Don't test framework behavior**: Don't test that `Text` renders text or `ElevatedButton` presses — test *your* logic, not Flutter's.
- **Integration tests are slow**: Reserve `integration_test/` for end-to-end flows. Most logic should be unit- or widget-tested.
