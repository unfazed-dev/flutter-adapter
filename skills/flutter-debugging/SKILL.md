---
name: flutter-debugging
description: Flutter-specific debugging — CanvasKit rendering, widget tree, state inspection, platform validation
stack: flutter
migrated_from: debugging
---

# Flutter Debugging

Stack-specific debugging skill for Flutter web and mobile.

## Triggers
- Flutter rendering issues (CanvasKit, Impeller)
- Widget not appearing as expected
- State management bugs
- Platform-specific crashes

## CanvasKit debugging
- Check if text disappears after Spacer in Row
- Replace Spacer with fixed-width SizedBox
- Use `print()` for debugging — maps to `console.log` in Flutter web
- Test on actual Flutter web, not just `flutter run`

## Widget tree debugging
- Flutter Inspector in DevTools
- `debugDumpApp()` for full widget tree
- `debugPaintSizeEnabled = true` for layout bounds
- Check `overflow` property on RenderFlex

## State debugging
- Add `print()` in `didChangeDependencies()` and `build()`
- Check `mounted` before `setState` in async callbacks
- Verify `dispose()` cancels all subscriptions
