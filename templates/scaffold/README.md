# Flutter Scaffold Template

Cookiecutter template for Flutter projects. Resolved at `maestro kit init`
from `defaults.toml` and the project brief.

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `project_slug` | `my-flutter-app` | Dart package name (lowercase, underscores) |
| `app_name` | `My Flutter App` | Display name |
| `org_identifier` | `com.example` | Reverse domain for Android/iOS bundle IDs |
| `use_riverpod` | `true` | Use Riverpod for state management |
| `use_go_router` | `true` | Use GoRouter for navigation |
| `use_shorebird` | `false` | Enable Shorebird code push |

## Usage

```bash
cookiecutter gh:maestro-adapters/flutter-adapter --directory=templates/scaffold
```

Or via Maestro:

```bash
maestro kit init --adapter flutter-adapter
```
