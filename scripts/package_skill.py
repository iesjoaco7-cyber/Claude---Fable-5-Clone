#!/usr/bin/env python3
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / ".claude" / "skills" / "claude-fable-5-clone"
DIST = ROOT / "dist"
OUT = DIST / "claude-fable-5-clone-skill.zip"


def main() -> None:
    if not (SKILL_DIR / "SKILL.md").exists():
        raise FileNotFoundError(f"Missing SKILL.md in {SKILL_DIR}")
    DIST.mkdir(exist_ok=True)
    if OUT.exists():
        OUT.unlink()
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for file in SKILL_DIR.rglob("*"):
            if file.is_file():
                arcname = file.relative_to(SKILL_DIR.parent)
                z.write(file, arcname)
    print(f"Created {OUT}")


if __name__ == "__main__":
    main()
