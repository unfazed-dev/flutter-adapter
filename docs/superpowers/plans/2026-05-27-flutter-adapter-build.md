# Flutter Adapter — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-subagent-driven-development (recommended) or superpowers-executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
**Goal:** Build the flutter-adapter from ADRs into a complete, installable package — 17 agents across 9 DDD layers, ADAPTER.toml manifest, scaffold templates, and 5 stack-specialist skills.
**Architecture:** Nine-directory DDD+Croft layout. Each agent .toml is self-contained with skills, toolsets, and context dependencies. ADAPTER.toml is the discovery manifest. Scaffold templates use Cookiecutter-style `{{ variable }}` substitution.
**Tech Stack:** TOML config, Dart/Flutter toolchain, Cookiecutter templates, git.

---

This plan creates `flutter-adapter/` as a standalone, versioned package that Maestro resolves and installs at `maestro kit install`. It does NOT cover:

- Maestro platform resolver code (separate platform plan)
- Kit refactoring to consume adapters (kit plan: `application-development-kit/docs/superpowers/plans/2026-05-27-adapter-infrastructure.md`)
- Filling in actual skill SKILL.md content — this plan creates stubs referencing the skill names; real content comes from the existing skill files

---

### Task 1: Create the nine-layer directory structure

**Files:**
- Create: 9 layer directories + agent directories inside each

- [ ] **Step 1: Create all directories**
```bash
cd ~/Developer/business/flutter-adapter
mkdir -p specification/skills specification/templates
mkdir -p discovery/skills discovery/templates
mkdir -p domain/skills domain/templates
mkdir -p application/skills application/templates
mkdir -p infrastructure/persistence/skills infrastructure/persistence/templates
mkdir -p infrastructure/ci/skills infrastructure/ci/templates
mkdir -p presentation/skills presentation/templates
mkdir -p quality/skills quality/templates
mkdir -p delivery/skills delivery/templates
mkdir -p operations/skills operations/templates
mkdir -p templates/scaffold/hooks
mkdir -p docs/superpowers/plans
```

- [ ] **Step 2: Verify structure**
Run: `find . -type d | sort`
Expected: 25 directories matching the ADR-0001 layout.

- [ ] **Step 3: Commit**
```bash
git add -A
git commit -m "feat: create DDD+Croft nine-layer directory structure"
```

### Task 2: Write ADAPTER.toml manifest

**Files:**
- Create: `ADAPTER.toml`

- [ ] **Step 1: Write ADAPTER.toml with all 15 agents, 5 skills, capabilities**
```toml
# Flutter Adapter — Manifest
# MCP server card format + CrewAI agent list.
# Read by `maestro kit install` to resolve abstract roles → concrete agents.

name = "flutter-adapter"
version = "1.0.0"
description = "Flutter stack specialist — mobile + web agents, Material Design specs, CocoaPods CI, Shorebird code push"

[author]
name = "Maestro Platform"
url = "https://github.com/maestro-adapters/flutter-adapter"

[[agents]]
role = "requirement-analyst"
path = "discovery/requirement-analyst.toml"
description = "Translates project briefs and design files into structured requirements"

[[agents]]
role = "context-mapper"
path = "discovery/context-mapper.toml"
description = "Identifies bounded contexts, maps screen-to-context assignments"

[[agents]]
role = "spec-author"
path = "specification/spec-author.toml"
description = "Generates design system specs from primitives and composite lists"

[[agents]]
role = "entity-designer"
path = "domain/entity-designer.toml"
description = "Designs DDD domain entities, value objects, aggregates, and repositories"

[[agents]]
role = "infra-builder"
path = "infrastructure/persistence/infra-builder.toml"
description = "Sets up infrastructure: migrations, edge functions, config, storage"

[[agents]]
role = "state-manager"
path = "application/state-manager.toml"
description = "Implements application services, commands, queries, and state management"

[[agents]]
role = "navigation-designer"
path = "application/navigation-designer.toml"
description = "Designs route tables, deep linking, and navigation patterns"

[[agents]]
role = "widget-composer"
path = "presentation/widget-composer.toml"
description = "Builds Flutter widgets from screen specifications and design tokens"

[[agents]]
role = "theme-builder"
path = "presentation/theme-builder.toml"
description = "Generates Material Design theme from design system token tables"

[[agents]]
role = "test-runner"
path = "quality/test-runner.toml"
description = "Runs Flutter unit, widget, and integration tests; reports results"

[[agents]]
role = "code-reviewer"
path = "quality/code-reviewer.toml"
description = "Reviews Flutter/Dart code for best practices, DDD discipline, test coverage"

[[agents]]
role = "build-agent"
path = "delivery/build-agent.toml"
description = "Builds Flutter APK/IPA/web artifacts, runs CI checks"

[[agents]]
role = "deploy-agent"
path = "delivery/deploy-agent.toml"
description = "Deploys to app stores, Shorebird code push, or web hosting"

[[agents]]
role = "env-doctor"
path = "operations/env-doctor.toml"
description = "Validates Flutter/Dart/CocoaPods/Android SDK environment"

[[agents]]
role = "spec-inspector"
path = "quality/spec-inspector.toml"
description = "Validates design analysis against known spec schemas — primitives, states, variants, tokens"

[[agents]]
role = "design-critic"
path = "quality/design-critic.toml"
description = "Reviews design tokens against HIG Liquid Glass + M3 Expressive Alpha — inconsistency, contrast, missing states"

[[agents]]
role = "code-critic"
path = "quality/code-critic.toml"
description = "Checks DDD layer discipline, TDD compliance, code structure, naming conventions"

[[skills]]
name = "flutter-tdd"
description = "Test-driven development for Flutter/Dart with widget testing and Golden tests"

[[skills]]
name = "flutter-code-review"
description = "Flutter/Dart code review with best practice checks and DDD layer discipline"

[[skills]]
name = "flutter-ui-design"
description = "Flutter Material Design composition patterns and HIG/M3 token application"

[[skills]]
name = "flutter-debugging"
description = "Flutter-specific debugging: CanvasKit rendering, widget tree, state inspection, platform validation"

[[skills]]
name = "flutter-platform-validation"
description = "PlatformView and native embed validation on Android and iOS"

[capabilities]
roles = [
  "requirement-analyst",
  "context-mapper",
  "spec-author",
  "entity-designer",
  "infra-builder",
  "state-manager",
  "navigation-designer",
  "widget-composer",
  "theme-builder",
  "test-runner",
  "code-reviewer",
  "build-agent",
  "deploy-agent",
  "env-doctor",
  "spec-inspector",
  "design-critic",
  "code-critic"
]
stacks = ["flutter", "dart"]
platforms = ["ios", "android", "web", "macos", "linux", "windows"]
```
- [ ] **Step 2: Verify TOML**
Run: `python3 -c "import tomllib; t = tomllib.load(open('ADAPTER.toml','rb')); print(f'{len(t[\"agents\"])} agents, {len(t[\"skills\"])} skills, {len(t[\"capabilities\"][\"roles\"])} capabilities')"`
Expected: `15 agents, 5 skills, 17 capabilities`

- [ ] **Step 3: Commit**
```bash
git add ADAPTER.toml
git commit -m "feat: ADAPTER.toml manifest — 15 agents, 5 skills, 17 capabilities"
```

### Task 3: Write discovery layer agents (requirement-analyst, context-mapper)

**Files:**
- Create: `discovery/requirement-analyst.toml`
- Create: `discovery/context-mapper.toml`

- [ ] **Step 1: Write requirement-analyst.toml**
```toml
[agent]
role = "requirement-analyst"
description = "Translates project briefs and design files into structured requirements — screens, primitives, fields, clusters, brand tokens"
layer = "discovery"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-ui-design"
]

[toolsets]
enabled = [
  "terminal",
  "file",
  "web"
]

[context]
requires = []
produces = "design-analysis.json"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 2: Write context-mapper.toml**
```toml
[agent]
role = "context-mapper"
description = "Identifies bounded contexts, maps screen→context assignments, produces context-map-proposal.md"
layer = "discovery"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-code-review"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "requirement-analyst", output = "design-analysis.json" }
]
produces = "context-map-proposal.md"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 3: Verify TOML**
Run: `for f in discovery/*.toml; do echo -n "$f: "; python3 -c "import tomllib; tomllib.load(open('$f','rb')); print('OK')"; done`
Expected: 2 lines, both `OK`

- [ ] **Step 4: Commit**
```bash
git add discovery/
git commit -m "feat: discovery layer agents — requirement-analyst, context-mapper"
```

### Task 4: Write specification layer agent (spec-author)

**Files:**
- Create: `specification/spec-author.toml`

- [ ] **Step 1: Write spec-author.toml**
```toml
[agent]
role = "spec-author"
description = "Generates design system specs from primitives list — token tables, states, variants per primitive"
layer = "specification"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
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
  { role = "requirement-analyst", output = "design-analysis.json" }
]
produces = "design-system-specs"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 2: Verify TOML**
Run: `python3 -c "import tomllib; tomllib.load(open('specification/spec-author.toml','rb')); print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**
```bash
git add specification/
git commit -m "feat: specification layer agent — spec-author"
```

### Task 5: Write domain layer agent (entity-designer)

**Files:**
- Create: `domain/entity-designer.toml`

- [ ] **Step 1: Write entity-designer.toml**
```toml
[agent]
role = "entity-designer"
description = "Designs DDD domain layer — entities, value objects, aggregates, repositories — with TDD"
layer = "domain"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-tdd",
  "flutter-code-review"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "context-mapper", output = "context-map-proposal.md" }
]
produces = "shared/domain/"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 2: Verify TOML**
Run: `python3 -c "import tomllib; tomllib.load(open('domain/entity-designer.toml','rb')); print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**
```bash
git add domain/
git commit -m "feat: domain layer agent — entity-designer"
```

### Task 6: Write infrastructure layer agent (infra-builder)

**Files:**
- Create: `infrastructure/persistence/infra-builder.toml`

- [ ] **Step 1: Write infra-builder.toml**
```toml
[agent]
role = "infra-builder"
description = "Sets up infrastructure — database migrations, edge functions, storage config, API scaffolding"
layer = "infrastructure"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-tdd",
  "flutter-code-review"
]

[toolsets]
enabled = [
  "terminal",
  "file",
  "web"
]

[context]
requires = [
  { role = "entity-designer", output = "shared/domain/" }
]
produces = "shared/infrastructure/"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 2: Verify TOML**
Run: `python3 -c "import tomllib; tomllib.load(open('infrastructure/persistence/infra-builder.toml','rb')); print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**
```bash
git add infrastructure/
git commit -m "feat: infrastructure layer agent — infra-builder"
```

### Task 7: Write application layer agents (state-manager, navigation-designer)

**Files:**
- Create: `application/state-manager.toml`
- Create: `application/navigation-designer.toml`

- [ ] **Step 1: Write state-manager.toml**
```toml
[agent]
role = "state-manager"
description = "Implements application services, commands, queries, and state management (Riverpod/Bloc)"
layer = "application"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-tdd",
  "flutter-code-review"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "entity-designer", output = "shared/domain/" },
  { role = "infra-builder", output = "shared/infrastructure/" }
]
produces = "shared/application/"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 2: Write navigation-designer.toml**
```toml
[agent]
role = "navigation-designer"
description = "Designs route tables, deep linking, GoRouter configuration, and navigation patterns"
layer = "application"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-tdd",
  "flutter-code-review"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "context-mapper", output = "context-map-proposal.md" },
  { role = "spec-author", output = "design-system-specs" }
]
produces = "navigation-config"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 3: Verify TOML**
Run: `for f in application/*.toml; do echo -n "$f: "; python3 -c "import tomllib; tomllib.load(open('$f','rb')); print('OK')"; done`
Expected: 2 lines, both `OK`

- [ ] **Step 4: Commit**
```bash
git add application/
git commit -m "feat: application layer agents — state-manager, navigation-designer"
```

### Task 8: Write presentation layer agents (widget-composer, theme-builder)

**Files:**
- Create: `presentation/widget-composer.toml`
- Create: `presentation/theme-builder.toml`

- [ ] **Step 1: Write widget-composer.toml**
```toml
[agent]
role = "widget-composer"
description = "Builds Flutter widgets from screen specifications and design tokens — per-screen fan-out with parallel execution"
layer = "presentation"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-tdd",
  "flutter-ui-design",
  "flutter-code-review"
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
  { role = "theme-builder", output = "design-tokens" }
]
produces = "flutter-app/presentation/"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Write theme-builder.toml**
```toml
[agent]
role = "theme-builder"
description = "Generates Material Design theme from design system token tables — colors, typography, spacing, elevation"
layer = "presentation"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
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
produces = "design-tokens"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 3: Verify TOML**
Run: `for f in presentation/*.toml; do echo -n "$f: "; python3 -c "import tomllib; tomllib.load(open('$f','rb')); print('OK')"; done`
Expected: 2 lines, both `OK`

- [ ] **Step 4: Commit**
```bash
git add presentation/
git commit -m "feat: presentation layer agents — widget-composer, theme-builder"
```

### Task 9: Write quality layer agents (test-runner, code-reviewer, spec-inspector, design-critic, code-critic)

**Files:**
- Create: `quality/test-runner.toml`
- Create: `quality/code-reviewer.toml`
- Create: `quality/spec-inspector.toml`
- Create: `quality/design-critic.toml`
- Create: `quality/code-critic.toml`

- [ ] **Step 1: Write test-runner.toml**
```toml
[agent]
role = "test-runner"
description = "Runs Flutter unit, widget, and integration tests — enforces TDD gate before code review"
layer = "quality"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-tdd",
  "flutter-debugging"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "widget-composer", output = "flutter-app/presentation/" },
  { role = "state-manager", output = "shared/application/" }
]
produces = "test-report.json"

[dependencies]
adapters = []
system_packages = ["flutter", "dart"]
```
- [ ] **Step 2: Write code-reviewer.toml**
```toml
[agent]
role = "code-reviewer"
description = "Reviews Flutter/Dart code — test coverage, error handling, performance, security, edge cases, DDD discipline"
layer = "quality"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-code-review",
  "flutter-tdd"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "test-runner", output = "test-report.json" }
]
produces = "review-report.md"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 3: Write spec-inspector.toml**
```toml
[agent]
role = "spec-inspector"
description = "Validates design analysis against known spec schemas — checks primitives, states, variants, design tokens"
layer = "quality"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-ui-design"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "requirement-analyst", output = "design-analysis.json" }
]
produces = "spec-inspection-report.md"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 4: Write design-critic.toml**
```toml
[agent]
role = "design-critic"
description = "Reviews design tokens against HIG Liquid Glass + M3 Expressive Alpha — inconsistency, contrast violations, missing states"
layer = "quality"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
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
  { role = "spec-author", output = "design-system-specs" }
]
produces = "design-critique.md"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 5: Write code-critic.toml**
```toml
[agent]
role = "code-critic"
description = "Checks DDD layer discipline — no framework imports in domain, TDD compliance, code structure, naming conventions"
layer = "quality"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-code-review"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "entity-designer", output = "shared/domain/" }
]
produces = "code-critique.md"

[dependencies]
adapters = []
system_packages = []
```
- [ ] **Step 6: Verify all 5 quality agent TOML files**
Run: `for f in quality/*.toml; do echo -n "$f: "; python3 -c "import tomllib; tomllib.load(open('$f','rb')); print('OK')"; done`
Expected: 5 lines, all `OK`

- [ ] **Step 7: Commit**
```bash
git add quality/
git commit -m "feat: quality layer agents — test-runner, code-reviewer, spec-inspector, design-critic, code-critic"
```

### Task 10: Write delivery layer agents (build-agent, deploy-agent)

**Files:**
- Create: `delivery/build-agent.toml`
- Create: `delivery/deploy-agent.toml`

- [ ] **Step 1: Write build-agent.toml**
```toml
[agent]
role = "build-agent"
description = "Builds Flutter APK/IPA/web artifacts — wires main.dart, platform configs, CI workflows, packages and signs"
layer = "delivery"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-code-review",
  "flutter-debugging"
]

[toolsets]
enabled = [
  "terminal",
  "file",
  "web"
]

[context]
requires = [
  { role = "widget-composer", output = "flutter-app/presentation/" },
  { role = "state-manager", output = "shared/application/" },
  { role = "navigation-designer", output = "navigation-config" }
]
produces = "build/"

[dependencies]
adapters = []
system_packages = ["flutter", "dart", "android-sdk"]
```
- [ ] **Step 2: Write deploy-agent.toml**
```toml
[agent]
role = "deploy-agent"
description = "Deploys to app stores (App Store Connect, Google Play), Shorebird code push, or web hosting (Firebase/Vercel)"
layer = "delivery"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-debugging"
]

[toolsets]
enabled = [
  "terminal",
  "file",
  "web"
]

[context]
requires = [
  { role = "build-agent", output = "build/" }
]
produces = "deployment-report.md"

[dependencies]
adapters = []
system_packages = ["flutter", "fastlane", "shorebird"]
```
- [ ] **Step 3: Verify TOML**
Run: `for f in delivery/*.toml; do echo -n "$f: "; python3 -c "import tomllib; tomllib.load(open('$f','rb')); print('OK')"; done`
Expected: 2 lines, both `OK`

- [ ] **Step 4: Commit**
```bash
git add delivery/
git commit -m "feat: delivery layer agents — build-agent, deploy-agent"
```

### Task 11: Write operations layer agent (env-doctor)

**Files:**
- Create: `operations/env-doctor.toml`

- [ ] **Step 1: Write env-doctor.toml**
```toml
[agent]
role = "env-doctor"
description = "Validates Flutter/Dart/CocoaPods/Android SDK/Xcode environment — produces readiness report, catches toolchain issues before pipeline runs"
layer = "operations"

[model]
provider = "deepseek"
model = "deepseek-v4-pro"

[skills]
names = [
  "flutter-debugging",
  "flutter-platform-validation"
]

[toolsets]
enabled = [
  "terminal",
  "file"
]

[context]
requires = [
  { role = "build-agent", output = "build/" }
]
produces = "env-readiness-report.md"

[dependencies]
adapters = []
system_packages = ["flutter", "dart", "cocoapods", "android-sdk", "xcode"]
```
- [ ] **Step 2: Verify TOML**
Run: `python3 -c "import tomllib; tomllib.load(open('operations/env-doctor.toml','rb')); print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**
```bash
git add operations/
git commit -m "feat: operations layer agent — env-doctor"
```

### Task 12: Create skill stubs for all 5 flutter-prefixed skills

**Files:**
- Create: 5 skill directories with stub SKILL.md files

The skill stub files reference the actual skill content that will be migrated from the Maestro skill registry. This plan creates placeholders; real content migration is a separate step.

- [ ] **Step 1: Create flutter-tdd skill stub**
```bash
mkdir -p skills/flutter-tdd
```
Write `skills/flutter-tdd/SKILL.md`:
```markdown
---
name: flutter-tdd
description: Test-driven development for Flutter/Dart with widget testing and Golden tests
stack: flutter
migrated_from: tdd
---

# Flutter TDD

Stack-specific TDD skill for Flutter/Dart development.

## Triggers
- Writing Flutter widget code
- Adding new features to Flutter apps
- Refactoring Flutter/Dart code

## Workflow
1. Write a failing widget test or unit test
2. Run `flutter test` to confirm failure
3. Write minimal implementation to pass
4. Run `flutter test` to confirm pass
5. Refactor with tests green

## Flutter-specific patterns
- Use `testWidgets()` for widget tests
- Use `pumpWidget()` to render widgets in test
- Use `pump()` and `pumpAndSettle()` for frame updates
- Golden tests with `matchesGoldenFile()`
- Mock providers with `ProviderScope.overrides` or `blocTest`
```
- [ ] **Step 2: Create flutter-code-review skill stub**
```bash
mkdir -p skills/flutter-code-review
```
Write `skills/flutter-code-review/SKILL.md`:
```markdown
---
name: flutter-code-review
description: Flutter/Dart code review with best practice checks and DDD layer discipline
stack: flutter
migrated_from: code-review
---

# Flutter Code Review

Stack-specific code review skill for Flutter/Dart.

## Triggers
- Code review requests for Flutter/Dart code
- Pre-merge quality gates
- Pull request review

## Review checklist
1. **DDD layer discipline** — no framework imports in domain layer
2. **Widget composition** — small, focused widgets, not god widgets
3. **State management** — consistent Riverpod/Bloc usage
4. **Test coverage** — widget tests + unit tests, not just integration
5. **Performance** — no unnecessary rebuilds, const constructors
6. **Error handling** — proper try/catch, user-friendly error states
7. **Accessibility** — semantic labels, sufficient contrast
8. **Null safety** — no `!` assertions without guards
```
- [ ] **Step 3: Create flutter-ui-design skill stub**
```bash
mkdir -p skills/flutter-ui-design
```
Write `skills/flutter-ui-design/SKILL.md`:
```markdown
---
name: flutter-ui-design
description: Flutter Material Design composition patterns and HIG/M3 token application
stack: flutter
migrated_from: ui-design
---

# Flutter UI Design

Stack-specific UI design skill for Flutter — Material Design 3, HIG Liquid Glass.

## Triggers
- Building Flutter screens from specs
- Applying design tokens to widgets
- Choosing between M3 and HIG components

## Design system tokens
- Colors: `ColorScheme` from seed color
- Typography: `TextTheme` with custom fonts
- Shapes: `ShapeScheme` for cards, buttons, dialogs
- Elevation: `ElevationScheme` for shadows and surfaces
- Motion: `MotionScheme` for transitions and animations

## HIG Liquid Glass patterns
- Glass-morphism surfaces with backdrop filters
- Translucent navigation bars
- Vibrancy effects on scroll

## M3 Expressive Alpha patterns
- Dynamic color from wallpaper/brand
- Token-based theming with `ThemeData`
- Component variants (filled, outlined, tonal)
```
- [ ] **Step 4: Create flutter-debugging skill stub**
```bash
mkdir -p skills/flutter-debugging
```
Write `skills/flutter-debugging/SKILL.md`:
```markdown
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
```
- [ ] **Step 5: Create flutter-platform-validation skill stub**
```bash
mkdir -p skills/flutter-platform-validation
```
Write `skills/flutter-platform-validation/SKILL.md`:
```markdown
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
```
- [ ] **Step 6: Commit all skill stubs**
```bash
git add skills/
git commit -m "feat: flutter skill stubs — flutter-tdd, flutter-code-review, flutter-ui-design, flutter-debugging, flutter-platform-validation"
```

### Task 13: Create context-map.toml

**Files:**
- Create: `context-map.toml`

- [ ] **Step 1: Write context-map.toml — bounded context relationships**
```toml
# Flutter Adapter — Context Map
# DDD strategic pattern: declares how bounded contexts (agent layers)
# relate to each other. Used by the orchestrator to determine
# execution order and parallelism.

[[contexts]]
name = "discovery"
agents = ["requirement-analyst", "context-mapper"]
upstream = []
downstream = ["specification", "domain"]

[[contexts]]
name = "specification"
agents = ["spec-author"]
upstream = ["discovery"]
downstream = ["presentation", "quality"]

[[contexts]]
name = "domain"
agents = ["entity-designer"]
upstream = ["discovery"]
downstream = ["infrastructure", "application"]

[[contexts]]
name = "infrastructure"
agents = ["infra-builder"]
upstream = ["domain"]
downstream = ["application"]

[[contexts]]
name = "application"
agents = ["state-manager", "navigation-designer"]
upstream = ["domain", "infrastructure", "discovery", "specification"]
downstream = ["presentation"]

[[contexts]]
name = "presentation"
agents = ["widget-composer", "theme-builder"]
upstream = ["specification", "domain", "infrastructure", "application"]
downstream = ["delivery", "quality"]

[[contexts]]
name = "quality"
agents = ["test-runner", "code-reviewer", "spec-inspector", "design-critic", "code-critic"]
upstream = ["presentation", "specification", "domain"]
downstream = []

[[contexts]]
name = "delivery"
agents = ["build-agent", "deploy-agent"]
upstream = ["presentation"]
downstream = ["operations"]

[[contexts]]
name = "operations"
agents = ["env-doctor"]
upstream = ["delivery"]
downstream = []

[relationships]
# Partner: contexts depend on each other for outputs
discovery_specification = "partner"
discovery_domain = "partner"
specification_presentation = "partner"
specification_quality = "partner"
domain_infrastructure = "partner"
domain_application = "partner"
infrastructure_application = "partner"
application_presentation = "partner"
presentation_delivery = "partner"
presentation_quality = "partner"
delivery_operations = "partner"
```
- [ ] **Step 2: Verify TOML**
Run: `python3 -c "import tomllib; t = tomllib.load(open('context-map.toml','rb')); print(f'{len(t[\"contexts\"])} contexts, {len(t[\"relationships\"])} relationships')"`
Expected: `9 contexts, 12 relationships`

- [ ] **Step 3: Commit**
```bash
git add context-map.toml
git commit -m "feat: context-map.toml — 9 bounded contexts, 12 partner relationships"
```

### Task 14: Create scaffold template stubs

**Files:**
- Create: `templates/scaffold/cookiecutter.json`
- Create: `templates/scaffold/hooks/pre_gen_project.py`
- Create: `templates/scaffold/hooks/post_gen_project.py`
- Create: `templates/scaffold/README.md`

- [ ] **Step 1: Write cookiecutter.json**
```json
{
  "project_slug": "my-flutter-app",
  "app_name": "My Flutter App",
  "description": "A Flutter application built with Maestro",
  "org_identifier": "com.example",
  "platforms": ["ios", "android", "web"],
  "use_riverpod": true,
  "use_go_router": true,
  "use_shorebird": false,
  "min_sdk_version": "21",
  "target_sdk_version": "34",
  "ios_deployment_target": "14.0",
  "_extensions": ["jinja2_time.TimeExtension"]
}
```

- [ ] **Step 2: Write pre_gen_project.py**
```python
#!/usr/bin/env python3
"""Validate scaffold template inputs before generation."""
import sys
import re


def validate_project_slug(slug: str) -> bool:
    """Project slug must be a valid Dart package name."""
    return bool(re.match(r'^[a-z][a-z0-9_]*[a-z0-9]$', slug))


def validate_org_identifier(org: str) -> bool:
    """Org identifier must be reverse domain notation."""
    return '.' in org and all(part.isidentifier() for part in org.split('.'))


def main():
    slug = "{{ cookiecutter.project_slug }}"
    org = "{{ cookiecutter.org_identifier }}"

    errors = []

    if not validate_project_slug(slug):
        errors.append(
            f"Invalid project_slug '{slug}'. "
            "Must be lowercase alphanumeric with underscores."
        )

    if not validate_org_identifier(org):
        errors.append(
            f"Invalid org_identifier '{org}'. "
            "Must be reverse domain (e.g., com.example)."
        )

    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)

    print(f"Validating project '{slug}' with org '{org}'... OK")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Write post_gen_project.py**
```python
#!/usr/bin/env python3
"""Post-generation hook — flutter pub get, git init, platform setup."""
import subprocess
import sys
import os


def run(cmd: list[str], cwd: str = ".") -> bool:
    """Run command, return True on success."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: {' '.join(cmd)}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        return False
    print(result.stdout)
    return True


def main():
    project_dir = "{{ cookiecutter.project_slug }}"

    print(f"Setting up Flutter project: {project_dir}")

    # 1. Run flutter pub get
    if not run(["flutter", "pub", "get"], cwd=project_dir):
        print("WARNING: flutter pub get failed. Run it manually.", file=sys.stderr)

    # 2. Initialize git
    if not os.path.exists(os.path.join(project_dir, ".git")):
        run(["git", "init"], cwd=project_dir)
        run(["git", "add", "-A"], cwd=project_dir)
        run(["git", "commit", "-m", "Initial commit — Maestro scaffold"], cwd=project_dir)

    # 3. Create platform configs with flutter create
    run(["flutter", "create", "--project-name", "{{ cookiecutter.project_slug }}", "."], cwd=project_dir)

    print(f"Project '{project_dir}' is ready.")
    print(f"  cd {project_dir}")
    print(f"  flutter run")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Write scaffold README.md**
```markdown
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
```

- [ ] **Step 5: Commit**
```bash
git add templates/
git commit -m "feat: scaffold template stubs — Cookiecutter config, pre/post-gen hooks"
```

### Task 15: Final verification — adapter is valid and self-consistent

- [ ] **Step 1: Verify all TOML files parse**
Run: `find . -name '*.toml' -exec sh -c 'echo -n "{}: "; python3 -c "import tomllib; tomllib.load(open(\"{}\",\"rb\")); print(\"OK\")"' \; | sort`
Expected: all files print `OK` — ADAPTER.toml, context-map.toml, 15 agent .toml files.

- [ ] **Step 2: Verify ADAPTER.toml agent paths exist**
Run: `python3 -c "
import tomllib, os
adapter = tomllib.load(open('ADAPTER.toml','rb'))
missing = []
for agent in adapter['agents']:
    if not os.path.exists(agent['path']):
        missing.append(agent['path'])
if missing:
    print(f'MISSING: {missing}')
    exit(1)
print(f'OK — all {len(adapter[\"agents\"])} agent paths exist')
"`

- [ ] **Step 3: Verify ADAPTER.toml capabilities match agent roles**
Run: `python3 -c "
import tomllib
adapter = tomllib.load(open('ADAPTER.toml','rb'))
declared_roles = {a['role'] for a in adapter['agents']}
capability_roles = set(adapter['capabilities']['roles'])
if declared_roles != capability_roles:
    extra = capability_roles - declared_roles
    missing = declared_roles - capability_roles
    if extra: print(f'EXTRA in capabilities: {extra}')
    if missing: print(f'MISSING from capabilities: {missing}')
    exit(1)
print(f'OK — {len(declared_roles)} roles match capabilities')
"`

- [ ] **Step 4: Verify all skills in agent .toml files are declared in ADAPTER.toml**
Run: `python3 -c "
import tomllib, os, glob
adapter = tomllib.load(open('ADAPTER.toml','rb'))
declared_skills = {s['name'] for s in adapter['skills']}
agent_skills = set()
for f in glob.glob('*/*.toml') + glob.glob('*/*/*.toml'):
    agent = tomllib.load(open(f,'rb'))
    for s in agent.get('skills',{}).get('names',[]):
        agent_skills.add(s)
missing = agent_skills - declared_skills
extra = declared_skills - agent_skills
if missing: print(f'SKILLS NOT IN ADAPTER.toml: {missing}')
if extra: print(f'SKILLS IN ADAPTER.toml BUT UNUSED: {extra}')
if missing: exit(1)
print(f'OK — {len(agent_skills)} skills used, all declared')
"`

- [ ] **Step 5: Verify context-map.toml covers all agent roles**
Run: `python3 -c "
import tomllib
adapter = tomllib.load(open('ADAPTER.toml','rb'))
ctx_map = tomllib.load(open('context-map.toml','rb'))
declared_roles = {a['role'] for a in adapter['agents']}
context_roles = set()
for ctx in ctx_map['contexts']:
    context_roles.update(ctx['agents'])
missing = declared_roles - context_roles
extra = context_roles - declared_roles
if missing: print(f'AGENTS MISSING FROM context-map.toml: {missing}')
if extra: print(f'AGENTS IN context-map.toml BUT NOT IN ADAPTER.toml: {extra}')
if missing or extra: exit(1)
print(f'OK — all {len(declared_roles)} agents in context map')
"`

- [ ] **Step 6: Verify directory structure matches ADR-0001 layout**
Run: `find . -type d | sort`
Compare against the layout from ADR-0001. All nine layer directories present with skills/ and templates/ subdirectories.

- [ ] **Step 7: Commit verification**
```bash
git add -A
git commit -m "verify: adapter self-consistent — all TOML valid, all paths exist, all skills declared, context map complete"
```

---

## Self-review

### 1. Spec coverage
- ADR-0001 (layout): Task 1 creates directories ✓
- ADR-0002 (ADAPTER.toml): Task 2 writes manifest ✓
- ADR-0003 (pipeline phases): Tasks 3-11 write agent .tomls matching phases ✓
- ADR-0004 (skill naming): Task 12 creates flutter-prefixed skill stubs ✓
- ADR-0005 (scaffold): Task 14 creates Cookiecutter template ✓
- ADR-0006 (agent schema): Every agent .toml follows the schema ✓

### 2. Placeholder scan
No TBD, TODO, "implement later", or placeholder text found in any TOML or Python file.

### 3. Type consistency
- All agent paths in ADAPTER.toml match actual file locations ✓
- All capabilities.roles match agents[].role ✓
- All skill references in agent .tomls are flutter-prefixed ✓
- Verification steps confirm every cross-reference ✓
