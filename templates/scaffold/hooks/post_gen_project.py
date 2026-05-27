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

    if not run(["flutter", "pub", "get"], cwd=project_dir):
        print("WARNING: flutter pub get failed. Run it manually.", file=sys.stderr)

    if not os.path.exists(os.path.join(project_dir, ".git")):
        run(["git", "init"], cwd=project_dir)
        run(["git", "add", "-A"], cwd=project_dir)
        run(["git", "commit", "-m", "Initial commit — Maestro scaffold"], cwd=project_dir)

    run(["flutter", "create", "--project-name", "{{ cookiecutter.project_slug }}", "."], cwd=project_dir)

    print(f"Project '{project_dir}' is ready.")
    print(f"  cd {project_dir}")
    print(f"  flutter run")


if __name__ == "__main__":
    main()
