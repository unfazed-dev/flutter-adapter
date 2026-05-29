---
name: flutter-ui-design
description: Shared Flutter design fundamentals — responsive layout, widget composition, animation basics, state management patterns, accessibility, and design token application. Use alongside flutter-hig-design or flutter-m3-design for platform-specific patterns.
stack: flutter
migrated_from: ui-design
---

# Flutter UI Design

Shared Flutter design fundamentals for agent output. Platform-specific patterns have moved to flutter-hig-design (iOS/Cupertino) and flutter-m3-design (Android/Material).

## When to use

When generating any Flutter UI code regardless of target platform. All widget composers and theme builders load this skill alongside their platform-specific design skill.

## Responsive layout patterns

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

// Breakpoint constants
class Breakpoints {
  static const double mobile = 600;
  static const double tablet = 1200;
}
```

## Widget composition patterns

Composition over inheritance — always prefer composing small focused widgets over monolithic screens:

```dart
// GOOD: composition
class SignInScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(children: [
      const SignInHeader(),
      const SignInForm(),
      SignInFooter(onTap: () {}),
    ]);
  }
}

// BAD: inheritance
class SignInScreen extends BaseScreen { ... }
```

## Widget lifecycle

```dart
class MyWidget extends StatefulWidget {
  @override
  State<MyWidget> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  @override
  void initState() {
    super.initState();
    // One-time setup: listeners, initial data
  }

  @override
  void dispose() {
    // Teardown: cancel subscriptions, dispose controllers
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Pure render — no side effects
    return Container();
  }
}
```

## Design token application

Always consume tokens through the theme, never hardcode values:

```dart
// Spacing tokens → EdgeInsets
Padding(
  padding: EdgeInsets.all(16), // md token
)

// Color tokens → ColorScheme
Container(
  color: Theme.of(context).colorScheme.surface,
)

// Typography tokens → TextTheme
Text(
  'Title',
  style: Theme.of(context).textTheme.titleLarge,
)
```

## Accessibility patterns

```dart
// Semantic labels for screen readers
Semantics(
  label: 'Sign in button',
  child: ElevatedButton(onPressed: () {}, child: const Text('Sign in')),
)

// Merge semantics for compound widgets
MergeSemantics(
  child: Row(children: [Checkbox(...), Text('Accept terms')]),
)

// Exclude decorative elements
ExcludeSemantics(
  child: Icon(Icons.star, color: Colors.amber),
)
```

## Animation basics

```dart
// AnimationController for explicit animations
late final AnimationController _controller;
late final Animation<double> _animation;

@override
void initState() {
  super.initState();
  _controller = AnimationController(
    duration: const Duration(milliseconds: 300),
    vsync: this,
  );
  _animation = Tween<double>(begin: 0, end: 1).animate(_controller);
}

// AnimatedBuilder for custom animated widgets
AnimatedBuilder(
  animation: _animation,
  builder: (context, child) {
    return Opacity(opacity: _animation.value, child: child);
  },
  child: const Text('Hello'),
);
```

## State management patterns

Architecture-agnostic patterns that work with any state management solution:

```dart
// setState — local ephemeral state
setState(() { _count++; });

// ChangeNotifier — observable model
class CounterModel extends ChangeNotifier {
  int _count = 0;
  int get count => _count;
  void increment() { _count++; notifyListeners(); }
}

// ListenableBuilder — rebuild on ChangeNotifier
ListenableBuilder(
  listenable: _model,
  builder: (context, child) => Text('${_model.count}'),
);
```

## Spacing scale

Use an 8dp grid:
- `4` — micro (icon padding)
- `8` — small (item spacing)
- `16` — medium (card padding, section gap)
- `24` — large (section separation)
- `32` — xlarge (page margins)
- `48` — xxlarge (hero spacing)

## Pitfalls

- **Don't hardcode colors**: Always use `Theme.of(context).colorScheme.primary`, never `Color(0xFF...)` directly. Enables dark mode and theme swapping.
- **Overflow on small screens**: Every screen should work at 360x640 (smallest Android). Use `SingleChildScrollView` and `Flexible` generously.
- **build() must be pure**: No side effects, no API calls, no async work in build. Put side effects in initState or ViewModel.
- **Platform-specific fonts**: Flutter handles iOS (San Francisco) and Android (Roboto) automatically with the default `TextTheme` — don't set custom `fontFamily` unless branding requires it.
