#!/usr/bin/env python3
from pathlib import Path
import re
import sys

NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
REF_RE = re.compile(r"`([^`]+\.(?:md|yaml|yml|json|txt))`")


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter delimited by ---")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter closing delimiter not found")
    raw = text[4:end].strip().splitlines()
    data = {}
    for line in raw:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        raise FileNotFoundError(f"Missing {skill_md}")
    text = skill_md.read_text(encoding="utf-8")
    data = parse_frontmatter(text)
    name = data.get("name", "")
    description = data.get("description", "")
    if not name:
        raise ValueError("Missing required frontmatter field: name")
    if not description:
        raise ValueError("Missing required frontmatter field: description")
    if not NAME_RE.match(name):
        raise ValueError("name must use only lowercase letters, numbers, and hyphens, max 64 chars")
    if name != skill_dir.name:
        raise ValueError(f"frontmatter name '{name}' must match skill folder '{skill_dir.name}'")
    if len(description) > 1024:
        raise ValueError("description should be <= 1024 characters")
    if "<" in name or ">" in name or "<" in description or ">" in description:
        raise ValueError("name and description must not contain XML-like tags")

    missing = []
    for ref in sorted(set(REF_RE.findall(text))):
        if ref.startswith(("http://", "https://")):
            continue
        candidate = skill_dir / ref
        if ref.startswith("references/") and not candidate.exists():
            missing.append(ref)
    if missing:
        raise FileNotFoundError("Missing referenced files: " + ", ".join(missing))

    print(f"OK: {skill_md} is valid")


if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".claude/skills/claude-fable-method-orchestrator")
    validate(path)
