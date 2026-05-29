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
