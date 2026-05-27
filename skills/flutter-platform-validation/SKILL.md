---
name: flutter-platform-validation
description: PlatformView and native embed validation on Android and iOS
stack: flutter
migrated_from: platform-validation
---

# Flutter Platform Validation

Stack-specific platform validation for Flutter native embeddings.

## Triggers
- Adding platform-specific views (maps, webviews, cameras)
- Debugging PlatformView rendering issues
- Native plugin integration

## Validation checklist
1. **Android PlatformView** — `TextureLayer` vs `VirtualDisplay` mode
2. **iOS PlatformView** — `UiKitView` composition vs hybrid
3. **Gesture handling** — touch events pass through correctly
4. **Keyboard** — text input focus works in embedded views
5. **Lifecycle** — platform views dispose cleanly on navigation

## Common issues
- PlatformView jank on Android < 10 (use TextureLayer hybrid)
- Keyboard not dismissing on iOS PlatformView
- Gesture conflicts between Flutter and native views
