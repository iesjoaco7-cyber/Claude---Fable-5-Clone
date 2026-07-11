#!/usr/bin/env python3
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "claude-fable-method-orchestrator"

REQUIRED_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    "CLAUDE.md",
    ".github/workflows/validate.yml",
    ".github/workflows/release.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/good_first_issue.yml",
    "docs/INSTALLATION.md",
    "docs/USAGE.md",
    "docs/ARCHITECTURE.md",
    "docs/GOOD_FIRST_ISSUES.md",
    "docs/RELEASE.md",
    "docs/COLLABORATION.md",
    "examples/README.md",
    f".claude/skills/{SKILL_NAME}/SKILL.md",
    f".claude/skills/{SKILL_NAME}/references/modules.md",
    f".claude/agents/{SKILL_NAME}.md",
    f"agents/{SKILL_NAME}.json",
    "evals/test-cases.yaml",
    "scripts/validate_skill.py",
    "scripts/package_skill.py",
]

LEGACY_PATHS = [
    ".claude/skills/claude-fable-5-clone",
    ".claude/agents/claude-fable-5-orchestrator.md",
    "agents/claude-fable-5-clone.json",
]

README_LINKS = [
    "docs/INSTALLATION.md",
    "docs/USAGE.md",
    "docs/ARCHITECTURE.md",
    "examples/README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            fail(f"missing required file: {rel}")

    for rel in LEGACY_PATHS:
        if (ROOT / rel).exists():
            fail(f"legacy artifact should be removed or moved to legacy/: {rel}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for rel in README_LINKS:
        if rel not in readme:
            fail(f"README.md does not link to {rel}")

    package = ROOT / "dist" / f"{SKILL_NAME}-skill.zip"
    if package.exists():
        with zipfile.ZipFile(package) as z:
            names = set(z.namelist())
        expected = f"{SKILL_NAME}/SKILL.md"
        if expected not in names:
            fail(f"skill zip does not contain {expected}")

    print("OK: repository consistency checks passed")


if __name__ == "__main__":
    main()
