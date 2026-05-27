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
