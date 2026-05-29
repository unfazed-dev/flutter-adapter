---
name: flutter-hig-design
description: Apple HIG design patterns for Flutter — Cupertino widgets, Liquid Glass materials (iOS 26 glassEffect), iOS color system, San Francisco typography, iOS-only deviations (toast→dialog). Use alongside flutter-ui-design for complete iOS target coverage.
---

# Flutter HIG Design

Apple Human Interface Guidelines patterns for Flutter agent output.

## When to use

When generating iOS-targeted Flutter UI — Cupertino widgets, Liquid Glass materials, iOS-native patterns. Used by hig-theme-builder, hig-widget-composer, and hig-design-critic.

## Cupertino widget patterns

Use `Cupertino*` widgets for iOS-native look:
- `CupertinoNavigationBar` — large title, back chevron, translucency
- `CupertinoButton` — default iOS button style (no elevation, text color)
- `CupertinoTextField` — iOS text field with clear button, placeholder style
- `CupertinoAlertDialog` — iOS alert with vertical button stack
- `CupertinoActionSheet` — bottom sheet with cancel button
- `CupertinoSlidingSegmentedControl` — segmented control rail
- `CupertinoSwitch` — iOS toggle with green track

## Liquid Glass material (iOS 26+)

Use `.glassEffect()` on SwiftUI views embedded via PlatformView:

```swift
RoundedRectangle(cornerRadius: 14)
    .fill(.regularMaterial)
    .glassEffect(.regular, in: RoundedRectangle(cornerRadius: 14))
```

Tier fallback for iOS 18: use `.regularMaterial` without `.glassEffect()`:

```swift
if #available(iOS 26, *) {
    view.glassEffect(.regular, in: shape)
} else {
    view.background(.regularMaterial)
}
```

## iOS color system

Semantic colors, not literal:
- `CupertinoColors.systemBackground` — root background
- `CupertinoColors.secondarySystemBackground` — grouped background
- `CupertinoColors.systemBlue` — primary action
- `CupertinoColors.label` — primary text
- `CupertinoColors.secondaryLabel` — secondary text
- `CupertinoColors.separator` — dividers

## iOS deviations

- **No native toast/snackbar** — Apple HIG explicitly discourages it. Use `CupertinoAlertDialog` (`.alert()`) for feedback.
- **No FAB** — use toolbar buttons or navigation bar actions.
- **Tab bar at bottom** with icons + labels, max 5 tabs.

## Pitfalls

- Don't mix Cupertino and Material widgets on the same screen — pick one design system per view
- `.glassEffect()` is iOS 26 only — always provide `.regularMaterial` fallback
- iOS doesn't have a native `Drawer` — use tab-based navigation or modal sheets
- `CupertinoPageScaffold` is required for proper iOS navigation bar translucency
