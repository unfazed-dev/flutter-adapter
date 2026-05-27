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
