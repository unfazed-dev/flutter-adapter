# Flutter Scaffold Template

Cookiecutter template for Flutter projects. Resolved at `maestro kit init`
from `defaults.toml` and the project brief.

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `project_slug` | `my-flutter-app` | Dart package name (lowercase, underscores) |
| `app_name` | `My Flutter App` | Display name |
| `description` | `A Flutter application built with Maestro` | Project description |
| `org_identifier` | `com.example` | Reverse domain for Android/iOS bundle IDs |
| `platforms` | `["ios", "android", "web"]` | Target platforms |
| `use_riverpod` | `true` | Use Riverpod for state management |
| `use_go_router` | `true` | Use GoRouter for navigation |
| `use_shorebird` | `false` | Enable Shorebird code push |
| `min_sdk_version` | `21` | Android minimum SDK version |
| `target_sdk_version` | `34` | Android target SDK version |
| `ios_deployment_target` | `14.0` | iOS minimum deployment target |

## Usage

```bash
cookiecutter gh:maestro-adapters/flutter-adapter --directory=templates/scaffold
```

Or via Maestro:

```bash
maestro kit init --adapter flutter-adapter
```
