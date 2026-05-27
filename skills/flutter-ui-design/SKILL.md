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
  // Shape tokens — apply to component themes (CardTheme, DialogTheme, etc.), not top-level ThemeData
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
