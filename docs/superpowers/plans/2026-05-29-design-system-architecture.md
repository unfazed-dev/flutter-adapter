# Flutter Adapter — Design System Architecture Implementation Plan
> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-subagent-driven-development (recommended) or superpowers-executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
**Goal:** Refactor flutter-adapter from 17 generic agents to 25 specialist agents with HIG/M3 design system split, Stacked MVVM architecture, and 8-layer determinism model per ADR-0007.
**Architecture:** Three presentation pipelines split by design system (iOS/HIG, Android/M3, Web/shadcn) plus replica mode. Feature-first DDD layout with Stacked MVVM nested inside bounded contexts. Compiled primitives for deterministic generation. 8 skills (5 existing + 3 new). 25 agents (17 original → 3 split into 9 → +2 new).
**Tech Stack:** TOML configuration files, Dart/Flutter (3.44+), Stacked framework (3.5.0+), shadcn_flutter, Swift (iOS PlatformView), Kotlin (Android PlatformView), probe-runner (verification).
**Parent ADR:** ADR-0007
---

## File Map

```
flutter-adapter/
├── ADAPTER.toml                          # MODIFY: 17→25 agents, 5→8 skills, 17→25 capabilities
├── context-map.toml                      # MODIFY: add 4 new bounded contexts
├── CONTEXT.md                            # DONE: grilling session complete
│
├── presentation/
│   ├── theme-builder.toml                # DELETE
│   ├── widget-composer.toml              # DELETE
│   ├── hig-theme-builder.toml            # CREATE
│   ├── m3-theme-builder.toml             # CREATE
│   ├── shadcn-theme-builder.toml         # CREATE
│   ├── hig-widget-composer.toml          # CREATE
│   ├── m3-widget-composer.toml           # CREATE
│   ├── shadcn-widget-composer.toml       # CREATE
│   └── replica-widget-composer.toml      # CREATE
│
├── quality/
│   ├── design-critic.toml                # DELETE
│   ├── hig-design-critic.toml            # CREATE
│   └── m3-design-critic.toml             # CREATE
│
├── delivery/
│   └── stacked-scaffolder.toml           # CREATE
│
├── operations/
│   └── idempotency-verifier.toml         # CREATE
│
├── spec-author.toml                      # MODIFY: add flutter-stacked skill
├── entity-designer.toml                  # MODIFY: add flutter-stacked skill
├── state-manager.toml                    # MODIFY: add flutter-stacked skill
├── infra-builder.toml                    # MODIFY: add flutter-stacked skill
├── navigation-designer.toml              # MODIFY: add flutter-stacked skill
├── widget-composer variants (above)      # MODIFY: skills updated
│
├── skills/
│   ├── flutter-ui-design/SKILL.md        # MODIFY: strip to shared fundamentals only
│   ├── flutter-stacked/SKILL.md          # CREATE
│   ├── flutter-platformview/SKILL.md     # CREATE
│   ├── flutter-hig-design/SKILL.md       # CREATE
│   └── flutter-m3-design/SKILL.md        # CREATE
│
├── tables/
│   ├── intent-adapter.md                 # CREATE
│   ├── motion-adapter.md                 # CREATE
│   └── visual-adapter.md                 # CREATE
│
└── compiled/
    └── .gitkeep                          # CREATE
```

## Task 1: Delete superseded agent TOML files

**Files:**
- Delete: `presentation/theme-builder.toml`
- Delete: `presentation/widget-composer.toml`
- Delete: `quality/design-critic.toml`

- [ ] **Step 1: Remove old agent files**
```bash
cd /Users/unfazed-mac/Developer/business/flutter-adapter
git rm presentation/theme-builder.toml presentation/widget-composer.toml quality/design-critic.toml
```
- [ ] **Step 2: Commit**
```bash
git commit -m "refactor: remove superseded theme-builder, widget-composer, design-critic agents"
```

## Task 2: Create HIG theme builder agent

**Files:**
- Create: `presentation/hig-theme-builder.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "hig-theme-builder"
description = "Generates Cupertino/HIG theme from design tokens — Liquid Glass materials, iOS color system, San Francisco typography scale"
layer = "presentation"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-hig-design",
  "flutter-ui-design",
  "flutter-tdd"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" }
]
produces = "hig-design-tokens"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('presentation/hig-theme-builder.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add presentation/hig-theme-builder.toml
git commit -m "feat: add hig-theme-builder agent — Cupertino + Liquid Glass theme generation"
```

## Task 3: Create M3 theme builder agent

**Files:**
- Create: `presentation/m3-theme-builder.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "m3-theme-builder"
description = "Generates Material Design 3 theme from design tokens — tonal palettes, elevation system, type scale, state layers"
layer = "presentation"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-m3-design",
  "flutter-ui-design",
  "flutter-tdd"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" }
]
produces = "m3-design-tokens"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('presentation/m3-theme-builder.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add presentation/m3-theme-builder.toml
git commit -m "feat: add m3-theme-builder agent — Material Design 3 theme generation"
```

## Task 4: Create Shadcn theme builder agent

**Files:**
- Create: `presentation/shadcn-theme-builder.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "shadcn-theme-builder"
description = "Generates shadcn_flutter theme from design tokens — ShadTheme configuration, color scheme, border radius scale"
layer = "presentation"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-m3-design",
  "flutter-ui-design",
  "flutter-tdd"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" }
]
produces = "shadcn-design-tokens"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('presentation/shadcn-theme-builder.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add presentation/shadcn-theme-builder.toml
git commit -m "feat: add shadcn-theme-builder agent — shadcn_flutter theme generation"
```

## Task 5: Create HIG widget composer agent

**Files:**
- Create: `presentation/hig-widget-composer.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "hig-widget-composer"
description = "Builds iOS-native Flutter widgets with PlatformView embeds — Cupertino widgets + UiKitView SwiftUI wrappers for visual-critical primitives"
layer = "presentation"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-hig-design",
  "flutter-ui-design",
  "flutter-stacked",
  "flutter-platformview",
  "flutter-tdd"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" },
  { role = "entity-designer", output = "shared/domain/" },
  { role = "infra-builder", output = "shared/infrastructure/" },
  { role = "state-manager", output = "shared/application/" },
  { role = "hig-theme-builder", output = "hig-design-tokens" }
]
produces = "flutter-app/presentation/ios/"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('presentation/hig-widget-composer.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add presentation/hig-widget-composer.toml
git commit -m "feat: add hig-widget-composer agent — iOS native widget generation"
```

## Task 6: Create M3 widget composer agent

**Files:**
- Create: `presentation/m3-widget-composer.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "m3-widget-composer"
description = "Builds Android-native Flutter widgets with PlatformView embeds — Material widgets + AndroidView Compose wrappers for visual-critical primitives"
layer = "presentation"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-m3-design",
  "flutter-ui-design",
  "flutter-stacked",
  "flutter-platformview",
  "flutter-tdd"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" },
  { role = "entity-designer", output = "shared/domain/" },
  { role = "infra-builder", output = "shared/infrastructure/" },
  { role = "state-manager", output = "shared/application/" },
  { role = "m3-theme-builder", output = "m3-design-tokens" }
]
produces = "flutter-app/presentation/android/"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('presentation/m3-widget-composer.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add presentation/m3-widget-composer.toml
git commit -m "feat: add m3-widget-composer agent — Android native widget generation"
```

## Task 7: Create Shadcn widget composer agent

**Files:**
- Create: `presentation/shadcn-widget-composer.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "shadcn-widget-composer"
description = "Builds web/desktop Flutter widgets using shadcn_flutter — accessible components with built-in a11y as native anchor"
layer = "presentation"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-m3-design",
  "flutter-ui-design",
  "flutter-stacked",
  "flutter-tdd"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" },
  { role = "entity-designer", output = "shared/domain/" },
  { role = "infra-builder", output = "shared/infrastructure/" },
  { role = "state-manager", output = "shared/application/" },
  { role = "shadcn-theme-builder", output = "shadcn-design-tokens" }
]
produces = "flutter-app/presentation/web/"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('presentation/shadcn-widget-composer.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add presentation/shadcn-widget-composer.toml
git commit -m "feat: add shadcn-widget-composer agent — web/desktop shadcn_flutter generation"
```

## Task 8: Create Replica widget composer agent

**Files:**
- Create: `presentation/replica-widget-composer.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "replica-widget-composer"
description = "Generates pure Flutter pixel-perfect replicas from design mockups — no native widgets, design is the single source of truth"
layer = "presentation"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-ui-design",
  "flutter-stacked",
  "flutter-tdd"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" }
]
produces = "flutter-app/presentation/replica/"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('presentation/replica-widget-composer.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add presentation/replica-widget-composer.toml
git commit -m "feat: add replica-widget-composer agent — pure Flutter pixel-perfect generation"
```

## Task 9: Create HIG design critic agent

**Files:**
- Create: `quality/hig-design-critic.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "hig-design-critic"
description = "Validates iOS/HIG design output — Liquid Glass material correctness, Cupertino widget conformance, iOS-only deviations (toast→dialog), contrast, missing states"
layer = "quality"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-hig-design",
  "flutter-ui-design",
  "flutter-platform-validation"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" },
  { role = "hig-widget-composer", output = "flutter-app/presentation/ios/" }
]
produces = "hig-design-critique.md"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('quality/hig-design-critic.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add quality/hig-design-critic.toml
git commit -m "feat: add hig-design-critic agent — HIG Liquid Glass validation"
```

## Task 10: Create M3 design critic agent

**Files:**
- Create: `quality/m3-design-critic.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "m3-design-critic"
description = "Validates Android/M3 design output — tonal palette accuracy, elevation levels, state layer application, Material widget conformance"
layer = "quality"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-m3-design",
  "flutter-ui-design",
  "flutter-platform-validation"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" },
  { role = "m3-widget-composer", output = "flutter-app/presentation/android/" }
]
produces = "m3-design-critique.md"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('quality/m3-design-critic.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add quality/m3-design-critic.toml
git commit -m "feat: add m3-design-critic agent — M3 Expressive Alpha validation"
```

## Task 11: Create Stacked scaffolder agent

**Files:**
- Create: `delivery/stacked-scaffolder.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "stacked-scaffolder"
description = "Scaffolds the Stacked MVVM project skeleton via stacked create app — sets up routing, service registration, and feature folder structure before widget composers run"
layer = "delivery"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-stacked"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "spec-author", output = "design-system-specs" }
]
produces = "flutter-app/"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('delivery/stacked-scaffolder.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add delivery/stacked-scaffolder.toml
git commit -m "feat: add stacked-scaffolder agent — Stacked MVVM project scaffolding"
```

## Task 12: Create idempotency verifier agent

**Files:**
- Create: `operations/idempotency-verifier.toml`

- [ ] **Step 1: Write agent TOML**
```toml
[agent]
role = "idempotency-verifier"
description = "Runs probe-runner to verify golden-spec fidelity and snapshot idempotency — captures design bundle vs app bundle, diffs with skeleton_diff, certifies deterministic output"
layer = "operations"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-platform-validation"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "hig-widget-composer", output = "flutter-app/presentation/ios/" },
  { role = "m3-widget-composer", output = "flutter-app/presentation/android/" },
  { role = "shadcn-widget-composer", output = "flutter-app/presentation/web/" },
  { role = "replica-widget-composer", output = "flutter-app/presentation/replica/" }
]
produces = "verification-report.json"

[dependencies]
adapters = []
system_packages = ["python3", "probe-runner"]
```
- [ ] **Step 2: Validate TOML parse**
```bash
python3 -c "import tomllib; tomllib.load(open('operations/idempotency-verifier.toml','rb')); print('OK')"
```
- [ ] **Step 3: Commit**
```bash
git add operations/idempotency-verifier.toml
git commit -m "feat: add idempotency-verifier agent — probe-runner deterministic validation"
```

## Task 13: Update existing agents with flutter-stacked skill

**Files:**
- Modify: `specification/spec-author.toml`
- Modify: `domain/entity-designer.toml`
- Modify: `application/state-manager.toml`
- Modify: `infrastructure/persistence/infra-builder.toml`
- Modify: `application/navigation-designer.toml`
- Modify: `quality/code-reviewer.toml`

- [ ] **Step 1: Update spec-author.toml skills**
Read the file, then add `"flutter-stacked"` to its `[skills] names` array.

- [ ] **Step 2: Update entity-designer.toml skills**
Read the file, then add `"flutter-stacked"` to its `[skills] names` array.

- [ ] **Step 3: Update state-manager.toml skills**
Read the file, then add `"flutter-stacked"` to its `[skills] names` array.

- [ ] **Step 4: Update infra-builder.toml skills**
Read the file, then add `"flutter-stacked"` to its `[skills] names` array.

- [ ] **Step 5: Update navigation-designer.toml skills**
Read the file, then add `"flutter-stacked"` to its `[skills] names` array.

- [ ] **Step 6: Update code-reviewer.toml skills**
Read the file, then add `"flutter-stacked"` to its `[skills] names` array.

- [ ] **Step 7: Commit all skill updates**
```bash
git add specification/spec-author.toml domain/entity-designer.toml application/state-manager.toml infrastructure/persistence/infra-builder.toml application/navigation-designer.toml quality/code-reviewer.toml
git commit -m "feat: add flutter-stacked skill to all application-layer agents"
```

## Task 14: Create flutter-stacked skill

**Files:**
- Create: `skills/flutter-stacked/SKILL.md`

- [ ] **Step 1: Write SKILL.md**
```markdown
---
name: flutter-stacked
description: Stacked MVVM patterns for Flutter — ViewModels with BaseViewModel, Views with ViewModelBuilder, service registration via get_it, Stacked routing with @StackedApp annotations. Use when generating Stacked-conformant Flutter code in any agent.
---

# Flutter Stacked

Stacked production MVVM patterns for Flutter agent output.

## When to use

When generating any Flutter code that must conform to the Stacked framework. All agents in the application layer and below load this skill.

## ViewModel patterns

Stacked ViewModels extend `BaseViewModel` and call `notifyListeners()` on state changes.

```dart
import 'package:stacked/stacked.dart';

class SignInViewModel extends BaseViewModel {
  final _authService = locator<AuthService>();
  
  String? _errorMessage;
  String? get errorMessage => _errorMessage;
  
  bool _isBusy = false;
  bool get isBusy => _isBusy;
  
  Future<void> signIn(String email, String password) async {
    _isBusy = true;
    _errorMessage = null;
    notifyListeners();
    
    try {
      await _authService.signIn(email, password);
    } catch (e) {
      _errorMessage = e.toString();
    }
    
    _isBusy = false;
    notifyListeners();
  }
}
```

## View patterns

Views use `ViewModelBuilder<T>.reactive()` for reactive rebuilds.

```dart
import 'package:stacked/stacked.dart';

class SignInView extends StackedView<SignInViewModel> {
  const SignInView({super.key});

  @override
  Widget builder(
    BuildContext context,
    SignInViewModel viewModel,
    Widget? child,
  ) {
    return Scaffold(
      body: viewModel.isBusy
          ? const Center(child: CircularProgressIndicator())
          : Column(children: [
              if (viewModel.errorMessage != null)
                Text(viewModel.errorMessage!, style: TextStyle(color: Colors.red)),
              // form fields here
            ]),
    );
  }

  @override
  SignInViewModel viewModelBuilder(BuildContext context) => SignInViewModel();
}
```

## Service registration

All services registered via `get_it` in `app/app.dart`:

```dart
import 'package:get_it/get_it.dart';
import 'package:stacked/stacked.dart';
import 'package:stacked_services/stacked_services.dart';

final locator = GetIt.instance;

@StackedApp(
  routes: [/* ... */],
  dependencies: [
    LazySingleton(classType: NavigationService),
    LazySingleton(classType: DialogService),
    LazySingleton(classType: AuthService),
  ],
)
class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'App',
      navigatorKey: StackedService.navigatorKey,
      onGenerateRoute: StackedRouter().onGenerateRoute,
    );
  }
}
```

## Feature-first folder structure

Each DDD bounded context maps to a feature folder:

```
lib/features/<context>/
├── ui/views/          # Stacked Views (widgets)
├── ui/viewmodels/     # Stacked ViewModels
├── domain/            # DDD entities, value objects (pure Dart)
├── data/repositories/ # get_it registered
├── data/services/     # API/storage wrappers
└── application/       # DDD commands/queries
```

## Pitfalls

- ViewModels must call `notifyListeners()` after every state mutation
- Services must be registered in `@StackedApp(dependencies: [...])` to be available via `locator<>()`
- Views should NOT contain business logic — only widget composition and simple if/else
- `StackedView` vs `ViewModelBuilder` — use `StackedView` for new code, `ViewModelBuilder` for compatibility
```
- [ ] **Step 2: Commit**
```bash
git add skills/flutter-stacked/SKILL.md
git commit -m "feat: add flutter-stacked skill — Stacked MVVM patterns"
```

## Task 15: Create flutter-platformview skill

**Files:**
- Create: `skills/flutter-platformview/SKILL.md`

- [ ] **Step 1: Write SKILL.md**
```markdown
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
```
- [ ] **Step 2: Commit**
```bash
git add skills/flutter-platformview/SKILL.md
git commit -m "feat: add flutter-platformview skill — PlatformView native embed generation"
```

## Task 16: Create flutter-hig-design skill

**Files:**
- Create: `skills/flutter-hig-design/SKILL.md`

- [ ] **Step 1: Write SKILL.md**
```markdown
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
```
- [ ] **Step 2: Commit**
```bash
git add skills/flutter-hig-design/SKILL.md
git commit -m "feat: add flutter-hig-design skill — HIG Cupertino + Liquid Glass patterns"
```

## Task 17: Create flutter-m3-design skill

**Files:**
- Create: `skills/flutter-m3-design/SKILL.md`

- [ ] **Step 1: Write SKILL.md**
```markdown
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
```
- [ ] **Step 2: Commit**
```bash
git add skills/flutter-m3-design/SKILL.md
git commit -m "feat: add flutter-m3-design skill — M3 tonal palettes + elevation patterns"
```

## Task 18: Refactor flutter-ui-design skill to shared fundamentals

**Files:**
- Modify: `skills/flutter-ui-design/SKILL.md`

- [ ] **Step 1: Read current skill content**
Read the current `skills/flutter-ui-design/SKILL.md` to understand existing content.

- [ ] **Step 2: Strip HIG/M3-specific content, keep shared fundamentals**
Rewrite SKILL.md to contain only shared Flutter design fundamentals:
- Responsive layout patterns (LayoutBuilder, MediaQuery, Breakpoint)
- Widget composition patterns (composition over inheritance)
- Widget lifecycle (initState, build, dispose)
- Design token application (spacing tokens → EdgeInsets, color tokens → ColorScheme)
- Accessibility patterns (Semantics, MergeSemantics, ExcludeSemantics)
- Animation basics (AnimationController, Tween, AnimatedBuilder)
- State management patterns (architecture-agnostic: setState, ChangeNotifier, ListenableBuilder)

Remove: Cupertino widget specifics (moved to flutter-hig-design), Material widget specifics (moved to flutter-m3-design).

- [ ] **Step 3: Commit**
```bash
git add skills/flutter-ui-design/SKILL.md
git commit -m "refactor: strip flutter-ui-design to shared fundamentals — move HIG/M3 specifics to extension skills"
```

## Task 19: Create adapter tables directory

**Files:**
- Create: `tables/intent-adapter.md`
- Create: `tables/motion-adapter.md`
- Create: `tables/visual-adapter.md`

- [ ] **Step 1: Create intent-adapter.md**
```bash
mkdir -p tables
```
```markdown
# Intent Adapter Table

Maps abstract ButtonIntent / DialogIntent / ToastIntent / SurfaceIntent enums to per-platform native widget choices.

## ButtonIntent → Platform Widget

| Intent | iOS (HIG) | Android (M3) | Web (shadcn) |
|--------|-----------|--------------|--------------|
| Primary | CupertinoButton + systemBlue bg | FilledButton | ShadButton.primary |
| Secondary | CupertinoButton + systemGray bg | OutlinedButton | ShadButton.outline |
| Tertiary | CupertinoButton + clear bg | TextButton | ShadButton.ghost |
| Text | Text with tap gesture | TextButton | ShadButton.link |
| Destructive | CupertinoButton + systemRed | FilledButton + error color | ShadButton.destructive |

## DialogIntent → Platform Widget

| Intent | iOS (HIG) | Android (M3) | Web (shadcn) |
|--------|-----------|--------------|--------------|
| Confirmation | CupertinoAlertDialog | AlertDialog + confirm | ShadAlertDialog |
| Destructive | CupertinoAlertDialog + destructive | AlertDialog + destructive | ShadAlertDialog.destructive |
| Informational | CupertinoAlertDialog | AlertDialog | ShadAlertDialog |

## SurfaceIntent → Platform Widget

| Intent | iOS (HIG) | Android (M3) | Web (shadcn) |
|--------|-----------|--------------|--------------|
| Default | Container + systemBackground | Surface | ShadCard |
| Glass | UiKitView + glassEffect | Material + elevation 1 | liquid-glass CSS |
| Elevated | Container + shadow | Surface + elevation 3 | ShadCard + shadow |
```
- [ ] **Step 2: Create motion-adapter.md**
```markdown
# Motion Adapter Table

Maps MotionIntent enums to per-platform timing curves.

| MotionIntent | iOS (HIG) | Android (M3) | Web |
|--------------|-----------|--------------|-----|
| Press | spring(0.3, 0.6) scale 0.97 | 100ms easeOut scale 0.95 | 100ms ease-out |
| Select | 200ms easeInOut | 200ms easeInOut | 200ms ease-in-out |
| Toggle | 150ms easeOut | 150ms easeOut | 150ms ease-out |
| Expand | 300ms easeOut | 300ms easeOut | 300ms ease-out |
| Collapse | 250ms easeIn | 250ms easeIn | 250ms ease-in |
| Present | 400ms spring(0.4, 0.7) | 300ms easeOut | 300ms ease-out |
| Dismiss | 300ms easeIn | 250ms easeIn | 250ms ease-in |
| ToastEnter | N/A (use dialog) | 300ms easeOut slide up | 300ms ease-out |
| ToastExit | N/A (use dialog) | 250ms easeIn fade | 250ms ease-in |
| NavPush | 350ms easeOut slide left | 300ms easeOut slide left | 300ms ease-out |
| NavPop | 300ms easeIn slide right | 250ms easeIn slide right | 250ms ease-in |
| Focus | 200ms easeOut | 200ms easeOut | 200ms ease-out |
| LoadingPulse | 1.5s easeInOut repeat | 1.5s easeInOut repeat | 1.5s ease-in-out infinite |
| ErrorShake | 500ms keyframe (3 shakes) | 500ms keyframe (3 shakes) | 500ms shake keyframe |
| SuccessCheck | 300ms easeOut scale 1.1 | 300ms easeOut scale 1.1 | 300ms ease-out |
```
- [ ] **Step 3: Create visual-adapter.md**
```markdown
# Visual Adapter Table

Maps abstract design tokens to per-platform concrete values.

## Spacing tokens

| Token | iOS (HIG) | Android (M3) | Web |
|-------|-----------|--------------|-----|
| space.xs | 4pt | 4dp | 0.25rem |
| space.sm | 8pt | 8dp | 0.5rem |
| space.md | 16pt | 16dp | 1rem |
| space.lg | 24pt | 24dp | 1.5rem |
| space.xl | 32pt | 32dp | 2rem |
| space.card | 16pt | 20dp | 1.25rem |
| space.card-gap | 12pt | 16dp | 1rem |

## Radius tokens

| Token | iOS (HIG) | Android (M3) | Web |
|-------|-----------|--------------|-----|
| radius.sm | 6pt | 8dp (shape.small) | 0.375rem |
| radius.md | 10pt | 12dp (shape.medium) | 0.5rem |
| radius.lg | 14pt | 16dp (shape.large) | 0.75rem |
| radius.card | 14pt | 12dp | 0.75rem |

## Color semantics (light mode)

| Token | iOS (HIG) | Android (M3) | Web |
|-------|-----------|--------------|-----|
| bg | systemBackground (#F2F2F7) | surface (#FFFBFE) | hsl(var(--background)) |
| surface | secondarySystemBackground (#FFFFFF) | surface-container-low (#F3EDF7) | hsl(var(--card)) |
| primary | systemBlue (#007AFF) | primary (#6750A4) | hsl(var(--primary)) |
| text | label (#000000) | on-surface (#1C1B1F) | hsl(var(--foreground)) |
| muted | secondaryLabel (#3C3C4399) | on-surface-variant (#49454F) | hsl(var(--muted-foreground)) |
| border | separator (#3C3C434D) | outline (#79747E) | hsl(var(--border)) |
```
- [ ] **Step 4: Commit all adapter tables**
```bash
git add tables/intent-adapter.md tables/motion-adapter.md tables/visual-adapter.md
git commit -m "feat: add adapter tables — intent, motion, visual mappings per platform"
```

## Task 20: Create compiled primitives directory

**Files:**
- Create: `compiled/.gitkeep`

- [ ] **Step 1: Create directory with gitkeep**
```bash
mkdir -p compiled
touch compiled/.gitkeep
```
- [ ] **Step 2: Commit**
```bash
git add compiled/.gitkeep
git commit -m "feat: add compiled/ directory for compiled primitive artifacts"
```

## Task 21: Update ADAPTER.toml manifest

**Files:**
- Modify: `ADAPTER.toml`

- [ ] **Step 1: Replace agent entries**
Remove old `theme-builder`, `widget-composer`, `design-critic` entries. Add new entries for all 11 new/replacement agents:

```toml
[[agents]]
role = "hig-theme-builder"
path = "presentation/hig-theme-builder.toml"
description = "Generates Cupertino/HIG theme from design tokens — Liquid Glass materials, iOS color system, SF typography"

[[agents]]
role = "m3-theme-builder"
path = "presentation/m3-theme-builder.toml"
description = "Generates Material Design 3 theme — tonal palettes, elevation system, state layers"

[[agents]]
role = "shadcn-theme-builder"
path = "presentation/shadcn-theme-builder.toml"
description = "Generates shadcn_flutter theme — ShadTheme configuration, color scheme, radii scale"

[[agents]]
role = "hig-widget-composer"
path = "presentation/hig-widget-composer.toml"
description = "Builds iOS-native Flutter widgets with PlatformView embeds — Cupertino + UiKitView SwiftUI wrappers"

[[agents]]
role = "m3-widget-composer"
path = "presentation/m3-widget-composer.toml"
description = "Builds Android-native Flutter widgets with PlatformView embeds — Material + AndroidView Compose wrappers"

[[agents]]
role = "shadcn-widget-composer"
path = "presentation/shadcn-widget-composer.toml"
description = "Builds web/desktop Flutter widgets using shadcn_flutter — accessible components with built-in a11y"

[[agents]]
role = "replica-widget-composer"
path = "presentation/replica-widget-composer.toml"
description = "Generates pure Flutter pixel-perfect replicas from design mockups — design is single source of truth"

[[agents]]
role = "hig-design-critic"
path = "quality/hig-design-critic.toml"
description = "Validates iOS/HIG output — Liquid Glass correctness, Cupertino conformance, iOS deviations"

[[agents]]
role = "m3-design-critic"
path = "quality/m3-design-critic.toml"
description = "Validates Android/M3 output — tonal palette accuracy, elevation levels, state layers"

[[agents]]
role = "stacked-scaffolder"
path = "delivery/stacked-scaffolder.toml"
description = "Scaffolds the Stacked MVVM project skeleton via stacked create app"

[[agents]]
role = "idempotency-verifier"
path = "operations/idempotency-verifier.toml"
description = "Runs probe-runner to verify golden-spec fidelity and snapshot idempotency"
```
Replace the 3 old entries (theme-builder, widget-composer, design-critic) with these 11.

- [ ] **Step 2: Update skills section**
Replace the current `[[skills]]` entries with the full 8-skill inventory:

```toml
[[skills]]
name = "flutter-tdd"
description = "Test-driven development for Flutter/Dart with widget testing and Golden tests"

[[skills]]
name = "flutter-code-review"
description = "Flutter/Dart code review with best practice checks and DDD layer discipline"

[[skills]]
name = "flutter-ui-design"
description = "Shared Flutter design fundamentals — layout, composition, responsive patterns, widget lifecycle"

[[skills]]
name = "flutter-hig-design"
description = "Apple HIG design patterns — Cupertino widgets, Liquid Glass materials, iOS color system, iOS deviations"

[[skills]]
name = "flutter-m3-design"
description = "Material Design 3 patterns — tonal palettes, elevation system, state layers, dynamic color"

[[skills]]
name = "flutter-debugging"
description = "Flutter-specific debugging: CanvasKit rendering, widget tree, state inspection, platform validation"

[[skills]]
name = "flutter-platform-validation"
description = "PlatformView and native embed validation on Android and iOS"

[[skills]]
name = "flutter-stacked"
description = "Stacked MVVM patterns — ViewModels, Views, service registration, routing"

[[skills]]
name = "flutter-platformview"
description = "PlatformView native embed code generation — UiKitView/AndroidView factories, MethodChannel bridges"
```

- [ ] **Step 3: Update capabilities.roles**
Update the `[capabilities] roles` array from 17 to 25 entries. Remove the 3 old roles, add the 11 new ones:

```toml
[capabilities]
roles = [
  "requirement-analyst",
  "context-mapper",
  "spec-author",
  "entity-designer",
  "infra-builder",
  "state-manager",
  "navigation-designer",
  "hig-theme-builder",
  "m3-theme-builder",
  "shadcn-theme-builder",
  "hig-widget-composer",
  "m3-widget-composer",
  "shadcn-widget-composer",
  "replica-widget-composer",
  "test-runner",
  "code-reviewer",
  "hig-design-critic",
  "m3-design-critic",
  "build-agent",
  "deploy-agent",
  "env-doctor",
  "spec-inspector",
  "code-critic",
  "stacked-scaffolder",
  "idempotency-verifier"
]
```

- [ ] **Step 4: Update version**
Bump version to `1.1.0`:
```toml
version = "1.1.0"
```

- [ ] **Step 5: Validate full TOML parse**
```bash
python3 -c "import tomllib; d=tomllib.load(open('ADAPTER.toml','rb')); print(f'Agents: {len(d[\"agents\"])}, Skills: {len(d.get(\"skills\",[]))}, Roles: {len(d[\"capabilities\"][\"roles\"])}')"
```
Expected: `Agents: 25, Skills: 9, Roles: 25`

- [ ] **Step 6: Commit**
```bash
git add ADAPTER.toml
git commit -m "feat: update ADAPTER.toml — 25 agents, 9 skills, 25 capabilities, v1.1.0"
```

## Task 22: Update context-map.toml

**Files:**
- Modify: `context-map.toml`

- [ ] **Step 1: Add new bounded contexts**
After the existing `[[contexts]]` entries for the 9 original contexts, add 4 new ones:

```toml
[[contexts]]
name = "hig-design-system"
description = "Apple HIG design system — Cupertino theme, Liquid Glass materials, iOS platform patterns"
owner = "hig-theme-builder"

[[contexts]]
name = "m3-design-system"
description = "Material Design 3 system — tonal palettes, elevation, state layers, Android platform patterns"
owner = "m3-theme-builder"

[[contexts]]
name = "shadcn-design-system"
description = "shadcn_flutter design system — accessible web/desktop components"
owner = "shadcn-theme-builder"

[[contexts]]
name = "replica-mode"
description = "Pure Flutter pixel-perfect replica rendering — no native widgets, design as source of truth"
owner = "replica-widget-composer"
```

- [ ] **Step 2: Update existing context owners**
Change `presentation` context owner from `widget-composer` to `hig-widget-composer` (primary, iOS-first).
Change `quality` context owner from `test-runner` to `test-runner` (unchanged, still the entry point).

- [ ] **Step 3: Add new relationships**
After existing `[[relationships]]`, add:

```toml
[[relationships]]
upstream = "specification"
downstream = "hig-design-system"
pattern = "customer-supplier"
description = "HIG theme is generated from design system specs"

[[relationships]]
upstream = "specification"
downstream = "m3-design-system"
pattern = "customer-supplier"
description = "M3 theme is generated from design system specs"

[[relationships]]
upstream = "specification"
downstream = "shadcn-design-system"
pattern = "customer-supplier"
description = "Shadcn theme is generated from design system specs"

[[relationships]]
upstream = "hig-design-system"
downstream = "presentation"
pattern = "customer-supplier"
description = "HIG widgets consume HIG theme tokens"

[[relationships]]
upstream = "m3-design-system"
downstream = "presentation"
pattern = "customer-supplier"
description = "M3 widgets consume M3 theme tokens"

[[relationships]]
upstream = "presentation"
downstream = "quality"
pattern = "customer-supplier"
description = "Design critics validate widget output"

[[relationships]]
upstream = "specification"
downstream = "replica-mode"
pattern = "customer-supplier"
description = "Replica widgets consume design specs directly"
```

- [ ] **Step 4: Commit**
```bash
git add context-map.toml
git commit -m "feat: update context-map — 4 new bounded contexts (hig, m3, shadcn, replica)"
```

## Task 23: Verification — full cross-reference check

**Files:**
- Verify: all TOML files parse and cross-reference correctly

- [ ] **Step 1: Verify all 25 agents have valid TOML**
```bash
cd /Users/unfazed-mac/Developer/business/flutter-adapter
python3 -c "
import tomllib, os, glob
errors = []
for f in sorted(glob.glob('**/*.toml', recursive=True)):
    if 'skills/' in f:
        continue
    try:
        d = tomllib.load(open(f, 'rb'))
        agent = d.get('agent', {})
        role = agent.get('role', 'MISSING')
        layer = agent.get('layer', 'MISSING')
        skills = d.get('skills', {}).get('names', [])
        if not role or role == 'MISSING':
            errors.append(f'{f}: missing agent.role')
        if not layer or layer == 'MISSING':
            errors.append(f'{f}: missing agent.layer')
        if not skills:
            errors.append(f'{f}: no skills assigned')
    except Exception as e:
        errors.append(f'{f}: {e}')
if errors:
    print('ERRORS:')
    for e in errors:
        print(f'  {e}')
else:
    print('All 25 agents: VALID')
"
```

- [ ] **Step 2: Verify all ADAPTER.toml agent paths exist on disk**
```bash
python3 -c "
import tomllib, os
d = tomllib.load(open('ADAPTER.toml', 'rb'))
errors = []
for a in d['agents']:
    if not os.path.exists(a['path']):
        errors.append(f'Missing: {a[\"path\"]} (role={a[\"role\"]})')
roles = [a['role'] for a in d['agents']]
if len(roles) != 25:
    errors.append(f'Expected 25 agents, got {len(roles)}')
if errors:
    print('ERRORS:')
    for e in errors:
        print(f'  {e}')
else:
    print(f'All {len(roles)} agent paths: EXIST')
"
```

- [ ] **Step 3: Verify all capabilities.roles match declared agents**
```bash
python3 -c "
import tomllib
d = tomllib.load(open('ADAPTER.toml', 'rb'))
agent_roles = {a['role'] for a in d['agents']}
cap_roles = set(d['capabilities']['roles'])
missing_from_agents = cap_roles - agent_roles
missing_from_caps = agent_roles - cap_roles
if missing_from_agents:
    print(f'In capabilities but not agents: {missing_from_agents}')
if missing_from_caps:
    print(f'In agents but not capabilities: {missing_from_caps}')
if not missing_from_agents and not missing_from_caps:
    print('Agent roles ↔ capabilities: MATCH')
"
```

- [ ] **Step 4: Verify all skills are referenced by at least one agent**
```bash
python3 -c "
import tomllib, glob
d = tomllib.load(open('ADAPTER.toml', 'rb'))
declared_skills = {s['name'] for s in d['skills']}
used_skills = set()
for a in d['agents']:
    used_skills.update(a.get('skills', {}).get('names', []))
unused = declared_skills - used_skills
missing = used_skills - declared_skills
if unused:
    print(f'Declared but unused: {unused}')
if missing:
    print(f'Used but not declared: {missing}')
if not unused and not missing:
    print(f'All {len(declared_skills)} skills: REFERENCED')
"
```

- [ ] **Step 5: Verify context-map owners reference real agents**
```bash
python3 -c "
import tomllib
d = tomllib.load(open('ADAPTER.toml', 'rb'))
agents = {a['role'] for a in d['agents']}
cm = tomllib.load(open('context-map.toml', 'rb'))
errors = []
for c in cm['contexts']:
    if c['owner'] not in agents:
        errors.append(f'Context {c[\"name\"]}: owner {c[\"owner\"]} not an agent')
if errors:
    print('ERRORS:')
    for e in errors:
        print(f'  {e}')
else:
    print(f'All {len(cm[\"contexts\"])} context owners: VALID')
"
```

- [ ] **Step 6: Commit verification results**
```bash
git add -A
git commit -m "verify: all 25 agents pass cross-reference checks — TOML parse, path existence, role/capability/skill/context-map consistency"
```

## Task 24: Push to origin

- [ ] **Step 1: Verify clean state**
```bash
cd /Users/unfazed-mac/Developer/business/flutter-adapter
git status
git log --oneline -5
```
- [ ] **Step 2: Push**
```bash
git push origin main
```
