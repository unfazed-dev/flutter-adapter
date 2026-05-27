# Flutter Skill Content Implementation Plan
> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-subagent-driven-development (recommended) or superpowers-executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
**Goal:** Replace all 5 flutter-adapter skill stubs with complete SKILL.md content — triggers, workflow steps, CLI commands, pitfalls, and verification patterns.
**Architecture:** Each skill lives in `skills/<name>/SKILL.md` with YAML frontmatter (name, description, stack) and a markdown body covering triggers, workflow, commands, and pitfalls. Skills are referenced by agent .toml files in the `[skills]` section.
**Tech Stack:** Flutter/Dart, widget testing, Golden tests, Riverpod, GoRouter, CanvasKit, PlatformViews
---
**Pre-requisite:** This plan assumes you are in the flutter-adapter repo (`~/Developer/business/flutter-adapter`). All paths are relative to repo root.

### Task 1: Complete flutter-tdd skill
**Files:**
- Overwrite: `skills/flutter-tdd/SKILL.md`
- [ ] **Step 1: Write the complete SKILL.md**
```markdown
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
```
- [ ] **Step 2: Verify the file parses correctly**
```bash
cat skills/flutter-tdd/SKILL.md | head -6
```
Expected: valid YAML frontmatter with name, description, stack fields.
- [ ] **Step 3: Verify the skill is referenced by at least one agent**
```bash
grep -rl "flutter-tdd" --include="*.toml" . | head -5
```
Expected: at least one agent .toml file lists flutter-tdd in its `[skills]` section.
- [ ] **Step 4: Commit**
```bash
git add skills/flutter-tdd/SKILL.md
git commit -m "feat: complete flutter-tdd skill — widget/Golden/Riverpod/Bloc testing patterns"
```

### Task 2: Complete flutter-code-review skill
**Files:**
- Overwrite: `skills/flutter-code-review/SKILL.md`
- [ ] **Step 1: Write the complete SKILL.md**
```markdown
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
```
- [ ] **Step 2: Verify the file parses**
```bash
cat skills/flutter-code-review/SKILL.md | head -6
```
- [ ] **Step 3: Verify agent references**
```bash
grep -rl "flutter-code-review" --include="*.toml" . | head -5
```
- [ ] **Step 4: Commit**
```bash
git add skills/flutter-code-review/SKILL.md
git commit -m "feat: complete flutter-code-review skill — DDD discipline, widget composition, accessibility, perf"
```

### Task 3: Complete flutter-ui-design skill
**Files:**
- Overwrite: `skills/flutter-ui-design/SKILL.md`
- [ ] **Step 1: Write the complete SKILL.md**
```markdown
---
name: flutter-ui-design
description: Flutter UI design patterns — Material Design 3 token system, theming, typography, color roles, elevation, responsive layout, and Flutter-specific implementation
stack: flutter
migrated_from: ui-design
---

# Flutter UI Design

Material Design 3 token-driven UI design for Flutter applications. Covers the M3 token system (color roles, typography scale, shape families), Flutter `ThemeData` implementation, responsive layout patterns with `LayoutBuilder`/`MediaQuery`, and platform adaptations.

## Triggers

- Building or theming a Flutter UI
- Creating design system tokens for a new app
- Converting Figma/design specs to Flutter widgets
- Ensuring visual consistency across screens
- Responsive layout implementation

## Workflow

1. Start from the design token table (colors, typography, spacing)
2. Generate `ThemeData` from tokens
3. Apply theme via `MaterialApp(theme: ...)`
4. Build widgets consuming theme tokens: `Theme.of(context).colorScheme.primary`
5. Verify on multiple screen sizes

## M3 Color System

```dart
final colorScheme = ColorScheme.fromSeed(
  seedColor: Color(0xFF6750A4), // Primary brand color
  brightness: Brightness.light,
);

// Available roles:
// - primary, onPrimary, primaryContainer, onPrimaryContainer
// - secondary, onSecondary, secondaryContainer, onSecondaryContainer
// - tertiary, onTertiary, tertiaryContainer, onTertiaryContainer
// - error, onError, errorContainer, onErrorContainer
// - background, onBackground, surface, onSurface
// - surfaceVariant, onSurfaceVariant, outline, outlineVariant
// - inverseSurface, onInverseSurface, inversePrimary, shadow, scrim
```

## ThemeData Implementation

```dart
ThemeData(
  useMaterial3: true,
  colorScheme: colorScheme,
  textTheme: TextTheme(
    displayLarge: TextStyle(fontSize: 57, fontWeight: FontWeight.w400, letterSpacing: -0.25),
    headlineMedium: TextStyle(fontSize: 28, fontWeight: FontWeight.w400),
    titleLarge: TextStyle(fontSize: 22, fontWeight: FontWeight.w400),
    titleMedium: TextStyle(fontSize: 16, fontWeight: FontWeight.w500, letterSpacing: 0.15),
    bodyLarge: TextStyle(fontSize: 16, fontWeight: FontWeight.w400, letterSpacing: 0.5),
    bodyMedium: TextStyle(fontSize: 14, fontWeight: FontWeight.w400, letterSpacing: 0.25),
    labelLarge: TextStyle(fontSize: 14, fontWeight: FontWeight.w500, letterSpacing: 0.1),
  ),
  // Elevation tokens
  elevation: 0, // Flat cards in M3
  cardTheme: CardTheme(
    elevation: 0,
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
  ),
  // Shape tokens
  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
);
```

## Responsive Layout

```dart
// LayoutBuilder for adaptive layouts
LayoutBuilder(
  builder: (context, constraints) {
    if (constraints.maxWidth < 600) {
      return MobileLayout();
    } else if (constraints.maxWidth < 1200) {
      return TabletLayout();
    } else {
      return DesktopLayout();
    }
  },
);

// Adaptive navigation
NavigationBar(  // M3 bottom nav — mobile
  destinations: [...],
);

NavigationRail( // M3 side rail — tablet
  destinations: [...],
);
```

## Spacing Scale

Use an 8dp grid:
- `4` — micro (icon padding)
- `8` — small (item spacing)
- `16` — medium (card padding, section gap)
- `24` — large (section separation)
- `32` — xlarge (page margins)
- `48` — xxlarge (hero spacing)

## Commands

```bash
# Generate theme from design tokens (if using token generator)
dart run design_tokens:generate

# Hot reload to preview theme changes
flutter run

# Check contrast ratios
flutter test test/accessibility/contrast_test.dart
```

## Pitfalls

- **Don't hardcode colors**: Always use `Theme.of(context).colorScheme.primary`, never `Color(0xFF...)` directly. Enables dark mode and theme swapping.
- **Elevation in M3**: M3 uses tonal overlays instead of shadow elevation for surfaces. `ElevatedButton` uses `elevation: 0` by default in M3.
- **Typography scale**: Don't use `fontSize: 14` — use the semantic token: `Theme.of(context).textTheme.bodyMedium`.
- **Platform-specific fonts**: iOS uses San Francisco, Android uses Roboto. Flutter handles this automatically with the default `TextTheme` — don't set custom `fontFamily` unless branding requires it.
- **Dark mode contrast**: M3 dark mode reduces text contrast intentionally (onSurface is `#E6E1E5` not white). Test both modes.
- **Overflow on small screens**: Every screen should work at 360x640 (smallest Android). Use `SingleChildScrollView` and `Flexible` generously.
```
- [ ] **Step 2: Verify the file parses**
```bash
cat skills/flutter-ui-design/SKILL.md | head -6
```
- [ ] **Step 3: Verify agent references**
```bash
grep -rl "flutter-ui-design" --include="*.toml" . | head -5
```
- [ ] **Step 4: Commit**
```bash
git add skills/flutter-ui-design/SKILL.md
git commit -m "feat: complete flutter-ui-design skill — M3 tokens, ThemeData, responsive layout, spacing"
```

### Task 4: Complete flutter-debugging skill
**Files:**
- Overwrite: `skills/flutter-debugging/SKILL.md`
- [ ] **Step 1: Write the complete SKILL.md**
```markdown
---
name: flutter-debugging
description: Flutter debugging — CanvasKit rendering issues, widget tree inspection, DevTools profiling, layout overflow diagnosis, build errors, and platform-specific debugging
stack: flutter
migrated_from: debugging
---

# Flutter Debugging

Debugging workflows for Flutter applications. Covers CanvasKit-specific rendering bugs, DevTools profiling, widget tree inspection, layout overflow diagnosis, platform-specific issues (iOS/Android/web), and common build errors.

## Triggers

- Visual rendering glitches (blank screens, missing widgets, rendering artifacts)
- Layout overflow errors (`A RenderFlex overflowed by ... pixels`)
- Build failures (`flutter build` errors)
- Performance issues (jank, slow frames)
- Platform-specific bugs (iOS works, Android crashes — or vice versa)
- CanvasKit web rendering issues

## Workflow

1. Reproduce the issue reliably
2. Check Flutter DevTools for the widget tree, frame rendering stats, or memory leaks
3. Isolate: does it happen on all platforms or just one?
4. Narrow the cause with bisecting or `debugDumpApp()`
5. Apply the fix and verify on all target platforms

## Common Errors and Fixes

### CanvasKit Web Rendering
```bash
# Switch to HTML renderer (fixes CanvasKit-specific bugs)
flutter run -d chrome --web-renderer html

# Or set permanently in launch.json
"args": ["--web-renderer", "html"]
```
**Symptoms**: Blank screen, missing text, font rendering issues, blurry widgets.
**Root cause**: CanvasKit uses Skia compiled to WASM — font loading, shader compilation, and image codec issues.

### Layout Overflow
```
══╡ EXCEPTION CAUGHT BY RENDERING LIBRARY ╞══
The following assertion was thrown during layout:
A RenderFlex overflowed by 42 pixels on the right.
```
**Fix**: Wrap in `SingleChildScrollView`, `Flexible`, `Expanded`, or reduce content size.

### Widget Not Updating
Check: is `setState` called? Is the provider watching the right state? Is the widget key stable?

### Build Failures
```bash
# Clean build artifacts
flutter clean
flutter pub get
flutter run

# Invalidate Gradle cache (Android)
cd android && ./gradlew clean && cd ..

# Clear CocoaPods (iOS)
cd ios && pod deintegrate && pod install && cd ..
```

## DevTools Commands

```bash
# Launch DevTools for running app
flutter pub global run devtools

# Profile mode (performance)
flutter run --profile

# Widget tree dump
flutter run  # then press 'w' in terminal for widget tree

# Debug paint (shows repaint boundaries)
flutter run --debug  # then press 'p' in terminal

# Timeline view for frame analysis
flutter run --profile --trace-skia
```

## Widget Tree Inspection

```dart
// Print widget tree to console
debugDumpApp();

// Print render tree to console
debugDumpRenderTree();

// Print layer tree (for compositing issues)
debugDumpLayerTree();

// Toggle debug paint
debugPaintSizeEnabled = true;
```

## Platform-Specific Debugging

### iOS
```bash
# Open Xcode for native debugging
open ios/Runner.xcworkspace

# Check signing
cd ios && xcodebuild -list
```

### Android
```bash
# Gradle dependency tree
cd android && ./gradlew :app:dependencies

# Check manifest
cat android/app/src/main/AndroidManifest.xml
```

### Web
```bash
# Browser console shows Flutter errors
flutter run -d chrome --web-renderer canvaskit
# Open Chrome DevTools → Console tab
```

## Pitfalls

- **Blank screen on web is almost always CanvasKit**: Try `--web-renderer html` first before deeper debugging.
- **Hot restart vs hot reload**: Hot reload preserves state; hot restart (`Shift+R` or `R`) is a full restart. If state changes don't take effect, hot restart.
- **Platform channel errors**: `MissingPluginException` means the native side isn't registered. Check `MainActivity.kt` (Android) or `AppDelegate.swift` (iOS).
- **Don't ship debug mode**: `flutter build` defaults to release. Profile mode (`--profile`) is for performance debugging only.
- **`assert()` is stripped in release**: Don't put critical logic inside `assert()` — it's removed in release builds.
```
- [ ] **Step 2: Verify the file parses**
```bash
cat skills/flutter-debugging/SKILL.md | head -6
```
- [ ] **Step 3: Verify agent references**
```bash
grep -rl "flutter-debugging" --include="*.toml" . | head -5
```
- [ ] **Step 4: Commit**
```bash
git add skills/flutter-debugging/SKILL.md
git commit -m "feat: complete flutter-debugging skill — CanvasKit, DevTools, layout overflow, platform bugs"
```

### Task 5: Complete flutter-platform-validation skill
**Files:**
- Overwrite: `skills/flutter-platform-validation/SKILL.md`
- [ ] **Step 1: Write the complete SKILL.md**
```markdown
---
name: flutter-platform-validation
description: Visual validation of Flutter PlatformViews on Android (SurfaceView/TextureView) and iOS (UiKitView) — hybrid composition, gesture disambiguation, z-ordering, and keyboard handling
stack: flutter
migrated_from: platform-validation
---

# Flutter Platform Validation

Validation workflows for Flutter PlatformViews — native views embedded in Flutter widget trees. Covers hybrid composition on Android and iOS, gesture handling, z-ordering, keyboard issues, and visual regression detection across platform channels.

## Triggers

- Using platform views (maps, webviews, camera, native ads)
- Gesture conflicts between Flutter and native views
- Z-ordering issues (platform view covers/obscures Flutter widgets)
- Keyboard handling around native text fields
- Platform-specific visual regressions

## Workflow

1. Identify the PlatformView widget and its creation params
2. Check the composition mode (hybrid, virtual display, texture layer)
3. Run the visual validation checklist on both Android and iOS
4. For gesture issues: use `GestureRecognizer` interop
5. For z-ordering: check `clipBehavior` and overlay placement
6. Screenshot diff against golden images

## PlatformView Composition Modes

### Android
```dart
// Hybrid composition (default since Flutter 3.0)
PlatformViewLink(
  viewType: 'my-native-view',
  surfaceFactory: (context, controller) {
    return AndroidViewSurface(
      controller: controller as AndroidViewController,
      gestureRecognizers: {},
      hitTestBehavior: PlatformViewHitTestBehavior.opaque,
    );
  },
  onCreatePlatformView: (params) {
    return PlatformViewsService.initSurfaceAndroidView(
      id: params.id,
      viewType: 'my-native-view',
      layoutDirection: TextDirection.ltr,
      creationParams: {},
      creationParamsCodec: StandardMessageCodec(),
    )
      ..addOnPlatformViewCreatedListener(params.onPlatformViewCreated)
      ..create();
  },
);
```

### iOS
```dart
UiKitView(
  viewType: 'my-native-view',
  layoutDirection: TextDirection.ltr,
  creationParams: {},
  creationParamsCodec: StandardMessageCodec(),
  gestureRecognizers: {},
);
```

## Validation Checklist

### Visual
- [ ] Platform view renders at correct size and position
- [ ] No flickering during Flutter rebuilds
- [ ] Platform view clips correctly to its bounds
- [ ] `Opacity`/`Transform` on parent widget works
- [ ] Golden image matches baseline

### Gesture
- [ ] Native gestures (scroll, pinch) work inside the platform view
- [ ] Flutter gestures work outside the platform view
- [ ] No gesture conflicts at the boundary
- [ ] `gestureRecognizers` configured for competing gestures
- [ ] Back gesture/edge swipe works on both platforms

### Z-Order
- [ ] Platform view doesn't cover Flutter overlays (dialogs, tooltips)
- [ ] `Overlay` widgets appear above platform view
- [ ] Dropdown menus, snackbars render on top

### Keyboard
- [ ] Native text input works (WebView, text fields)
- [ ] Keyboard shows/hides without layout jumps
- [ ] `android:windowSoftInputMode` in AndroidManifest is correct
- [ ] iOS `resizeToAvoidBottomInset: true` on Scaffold

## Commands

```bash
# Run with PlatformView debugging
flutter run --enable-software-rendering

# Take screenshots for golden comparison
flutter test --update-goldens test/platform_view_golden_test.dart

# Run on specific device
flutter run -d <device_id>

# Profile platform channel performance
flutter run --profile --trace-platform-channels
```

## Golden Test for PlatformViews

```dart
testWidgets('MapView renders correctly', (tester) async {
  final mockController = MockMapController();
  await tester.pumpWidget(
    MaterialApp(
      home: Scaffold(
        body: MapWidget(controller: mockController),
      ),
    ),
  );
  await tester.pumpAndSettle();
  await expectLater(
    find.byType(MapWidget),
    matchesGoldenFile('goldens/map_view.png'),
  );
});
```

## Pitfalls

- **Android Virtual Display vs Hybrid Composition**: Virtual display mode renders the platform view to a texture (better performance, limited gestures). Hybrid composition embeds the native view in the Flutter view hierarchy (full gestures, higher overhead). Use hybrid composition for interactive views, virtual display for display-only views.
- **iOS `clipBehavior`**: PlatformViews on iOS don't clip children by default. Set `clipBehavior: Clip.hardEdge` on the parent widget to prevent overflow.
- **`AndroidView` is deprecated**: Use `PlatformViewLink` with `AndroidViewSurface` for new code. `AndroidView` will be removed.
- **WebView keyboard**: WebView text fields don't trigger Flutter's `TextInputConnection`. Keyboard handling is entirely native — check WebView settings for `javascriptMode` and `zoomEnabled`.
- **Golden test platform sensitivity**: PlatformViews render differently on Android vs iOS. Separate golden directories (`goldens/android/`, `goldens/ios/`).
```
- [ ] **Step 2: Verify the file parses**
```bash
cat skills/flutter-platform-validation/SKILL.md | head -6
```
- [ ] **Step 3: Verify agent references**
```bash
grep -rl "flutter-platform-validation" --include="*.toml" . | head -5
```
- [ ] **Step 4: Commit**
```bash
git add skills/flutter-platform-validation/SKILL.md
git commit -m "feat: complete flutter-platform-validation skill — PlatformViews, hybrid composition, gestures, z-order"
```

### Task 6: Final verification
**Files:**
- None (verification only)
- [ ] **Step 1: Verify all skills parse as valid markdown with frontmatter**
```bash
for skill in flutter-tdd flutter-code-review flutter-ui-design flutter-debugging flutter-platform-validation; do
  echo "=== $skill ==="
  head -6 skills/$skill/SKILL.md
  echo ""
done
```
Expected: each shows valid YAML frontmatter with `name`, `description`, `stack` fields.
- [ ] **Step 2: Verify all skills are referenced by at least one agent**
```bash
for skill in flutter-tdd flutter-code-review flutter-ui-design flutter-debugging flutter-platform-validation; do
  refs=$(grep -rl "$skill" --include="*.toml" . | wc -l | tr -d ' ')
  echo "$skill: $refs agent(s) reference it"
done
```
Expected: each skill has at least 1 agent reference (printed count > 0).
- [ ] **Step 3: Verify no TODO/TBD placeholders remain in skill files**
```bash
grep -rn "TODO\|TBD\|FIXME" skills/
```
Expected: no output (empty).
- [ ] **Step 4: Verify ADAPTER.toml lists all 5 skills**
```bash
grep -A1 "skills = \[" ADAPTER.toml
```
Expected: lists all 5 flutter-* skills.
- [ ] **Step 5: Commit verification**
```bash
git status
```
Expected: clean working tree (all skill changes already committed).
