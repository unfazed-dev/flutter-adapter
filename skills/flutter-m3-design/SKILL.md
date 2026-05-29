---
name: flutter-m3-design
description: Material Design 3 patterns for Flutter — tonal palettes, elevation system, state layers, dynamic color, Expressive Alpha motion. Use alongside flutter-ui-design for complete Android/M3 target coverage.
---

# Flutter M3 Design

Material Design 3 patterns for Flutter agent output.

## When to use

When generating Android-targeted Flutter UI — Material Design 3 widgets, tonal palettes, elevation system, state layers. Used by m3-theme-builder, m3-widget-composer, and m3-design-critic.

## M3 theme: tonal palettes

```dart
final colorScheme = ColorScheme.fromSeed(
  seedColor: designTokens.primary,
  brightness: Brightness.light,
);

final theme = ThemeData(
  useMaterial3: true,
  colorScheme: colorScheme,
);
```

## M3 widget patterns

- `NavigationBar` (M3) — pill-shaped bottom bar, 3-5 destinations
- `NavigationRail` — side rail for tablet/desktop
- `FilledButton` / `OutlinedButton` / `TextButton` — M3 button hierarchy
- `Card` with `CardDefaults.cardElevation()` — M3 card with elevation levels
- `SnackBar` — bottom transient message with action
- `Switch` (M3) — M3 toggle with track colors

## Elevation system

M3 elevation levels map to dp values:
- Level 0: 0dp (surface)
- Level 1: 1dp (card, button resting)
- Level 2: 3dp (FAB resting)
- Level 3: 6dp (FAB pressed, dialog)
- Level 4: 8dp (navigation drawer)
- Level 5: 12dp (modal bottom sheet)

## State layers

M3 applies transparent overlays on interaction:
- Hover: `stateLayerColor` at 8% opacity
- Focus: `stateLayerColor` at 12% opacity
- Press: `stateLayerColor` at 12% opacity + ripple
- Drag: `stateLayerColor` at 16% opacity

## Expressive Alpha motion

M3 Expressive Alpha adds enhanced spring animations:
```dart
AnimationController(
  duration: const Duration(milliseconds: 500),
  // Expressive Alpha: spring-based, asymmetric
);
```

For baseline mode, use standard M3 durations (300ms, easeInOut).

## Pitfalls

- Always set `useMaterial3: true` in ThemeData — M3 is opt-in in Flutter
- M3 NavigationBar replaces BottomNavigationBar — they have different APIs
- Tonal palette generation via `ColorScheme.fromSeed()` is non-deterministic — pin the seed color
- State layers are automatically handled by M3 widgets — don't manually add InkWell on M3 components
