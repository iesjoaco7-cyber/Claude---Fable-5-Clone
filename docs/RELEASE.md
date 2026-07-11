# Release Guide

This repo is prepared for a public `v0.1.0` release.

## Before release

Run:

```bash
python scripts/validate_skill.py .claude/skills/claude-fable-method-orchestrator
python scripts/package_skill.py
python scripts/check_repo.py
```

Check:

- [ ] `CHANGELOG.md` has the release notes.
- [ ] `dist/claude-fable-method-orchestrator-skill.zip` exists.
- [ ] README links are correct.
- [ ] GitHub Actions are passing on `main`.

## Create the release from terminal

```bash
git status
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

The `Release` GitHub Action will build the Skill package and attach it to a GitHub Release.

## Create the release manually on GitHub

1. Go to **Releases**.
2. Click **Draft a new release**.
3. Tag: `v0.1.0`.
4. Title: `v0.1.0 — Claude Fable Method Orchestrator`.
5. Copy the notes from `CHANGELOG.md`.
6. Attach `dist/claude-fable-method-orchestrator-skill.zip`.
7. Publish.
