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
