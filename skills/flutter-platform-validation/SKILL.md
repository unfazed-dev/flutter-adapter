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
