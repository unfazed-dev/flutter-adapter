---
name: flutter-platformview
description: PlatformView native embed generation for Flutter — UiKitView factory patterns (Swift), AndroidView factory patterns (Kotlin), MethodChannel bridges, view type registration. Use when generating PlatformView code for native widget embeds.
---

# Flutter PlatformView

Generates PlatformView native embed code for Flutter apps targeting iOS and Android.

## When to use

When a widget-composer needs to generate native platform views — UiKitView wrappers for SwiftUI on iOS, AndroidView wrappers for Compose on Android. Used by HIG and M3 widget-composers.

## iOS: UiKitView factory pattern

```swift
// ios/Runner/UILibraryCardPlatformView.swift
import SwiftUI
import Flutter

class UILibraryCardPlatformViewFactory: NSObject, FlutterPlatformViewFactory {
    private var messenger: FlutterBinaryMessenger
    
    init(messenger: FlutterBinaryMessenger) {
        self.messenger = messenger
        super.init()
    }
    
    func create(withFrame frame: CGRect, viewIdentifier viewId: Int64, arguments args: Any?) -> FlutterPlatformView {
        return UILibraryCardPlatformView(frame: frame, viewId: viewId, args: args, messenger: messenger)
    }
    
    func createArgsCodec() -> FlutterMessageCodec & NSObjectProtocol {
        return FlutterStandardMessageCodec.sharedInstance()
    }
}

class UILibraryCardPlatformView: NSObject, FlutterPlatformView {
    private var _view: UIView
    private var _methodChannel: FlutterMethodChannel
    
    init(frame: CGRect, viewId: Int64, args: Any?, messenger: FlutterBinaryMessenger) {
        _methodChannel = FlutterMethodChannel(name: "com.engineering-pack.ui-library.card/\(viewId)", binaryMessenger: messenger)
        _view = UIView(frame: frame)
        super.init()
        
        let child = UIHostingController(rootView: NativeCardView(channel: _methodChannel))
        child.view.frame = _view.bounds
        child.view.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        _view.addSubview(child.view)
    }
    
    func view() -> UIView { return _view }
}

struct NativeCardView: View {
    let channel: FlutterMethodChannel
    @State private var isPressed = false
    
    var body: some View {
        RoundedRectangle(cornerRadius: 14)
            .fill(.regularMaterial)
            .glassEffect(.regular, in: RoundedRectangle(cornerRadius: 14))
            .scaleEffect(isPressed ? 0.97 : 1.0)
            .animation(.spring(response: 0.3, dampingFraction: 0.6), value: isPressed)
            .onTapGesture {
                isPressed = true
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
                    isPressed = false
                    channel.invokeMethod("tapped", arguments: nil)
                }
            }
    }
}
```

AppDelegate registration:
```swift
// ios/Runner/AppDelegate.swift
let registrar = self.registrar(forPlugin: "com.engineering-pack.ui-library")!
registrar.register(
    UILibraryCardPlatformViewFactory(messenger: registrar.messenger()),
    withId: "com.engineering-pack.ui-library.card"
)
```

## Android: AndroidView factory pattern

```kotlin
// android/app/src/main/kotlin/com/example/app/UILibraryCardPlatformView.kt
package com.example.app

import android.content.Context
import android.view.View
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.ComposeView
import androidx.compose.ui.unit.dp
import io.flutter.plugin.common.MethodCall
import io.flutter.plugin.common.MethodChannel
import io.flutter.plugin.platform.PlatformView

class UILibraryCardPlatformView(
    context: Context,
    viewId: Int,
    args: Map<String, Any>?
) : PlatformView, MethodChannel.MethodCallHandler {
    private val channel = MethodChannel(
        (context as android.app.Activity).flutterEngine!!.dartExecutor.binaryMessenger,
        "com.engineering-pack.ui-library.card/$viewId"
    )
    private val composeView = ComposeView(context)

    init {
        channel.setMethodCallHandler(this)
        composeView.setContent {
            var pressed by remember { mutableStateOf(false) }
            Card(
                modifier = Modifier.fillMaxWidth().padding(16.dp),
                elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
                onClick = {
                    pressed = true
                    channel.invokeMethod("tapped", null)
                }
            ) {
                // Content passed via method channel arguments
            }
        }
    }

    override fun getView(): View = composeView
    override fun dispose() { channel.setMethodCallHandler(null) }
    override fun onMethodCall(call: MethodCall, result: MethodChannel.Result) {}
}
```

MainActivity registration:
```kotlin
// android/app/src/main/kotlin/com/example/app/MainActivity.kt
override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
    super.configureFlutterEngine(flutterEngine)
    flutterEngine.platformViewsController.registry
        .registerViewFactory("com.engineering-pack.ui-library.card") {
            UILibraryCardPlatformView(context, it.id(), null)
        }
}
```

## Flutter side: PlatformView widget

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class NativeCard extends StatelessWidget {
  final Widget child;
  final VoidCallback? onTap;
  
  const NativeCard({super.key, required this.child, this.onTap});

  @override
  Widget build(BuildContext context) {
    if (defaultTargetPlatform == TargetPlatform.iOS) {
      return UiKitView(
        viewType: 'com.engineering-pack.ui-library.card',
        onPlatformViewCreated: (id) {
          if (onTap != null) {
            MethodChannel('com.engineering-pack.ui-library.card/$id')
              ..setMethodCallHandler((call) {
                if (call.method == 'tapped') onTap!();
                return Future.value(null);
              });
          }
        },
      );
    } else if (defaultTargetPlatform == TargetPlatform.android) {
      return AndroidView(
        viewType: 'com.engineering-pack.ui-library.card',
        onPlatformViewCreated: (id) {
          if (onTap != null) {
            MethodChannel('com.engineering-pack.ui-library.card/$id')
              ..setMethodCallHandler((call) {
                if (call.method == 'tapped') onTap!();
                return Future.value(null);
              });
          }
        },
      );
    }
    return child; // Fallback to standard Flutter widget
  }
}
```

## Pitfalls

- PlatformView viewType must match the string registered in AppDelegate/MainActivity exactly
- Hybrid composition (`HCUiKitView`/`HCAndroidView`) is preferred over virtual display for interactive widgets
- MethodChannel names must include viewId for per-instance dispatch (`"prefix/$viewId"`)
- On iOS, the hosting controller's view must match the factory frame bounds and use flexible autoresizing
- On Android, the ComposeView must use the activity's flutterEngine binaryMessenger, not a new one
