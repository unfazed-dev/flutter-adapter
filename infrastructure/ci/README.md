# infrastructure/ci/

Reserved subdirectory for CI/CD-specific agents (not yet implemented).

The infrastructure layer is partitioned per ADR-0001:
- `persistence/` — infra-builder (database, storage, config)
- `ci/` — reserved for future CI pipeline agents (GitHub Actions, GitLab CI, Fastlane)

Currently no agent is assigned to this subdirectory.
