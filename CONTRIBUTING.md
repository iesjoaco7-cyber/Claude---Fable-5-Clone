# Contributing

Thanks for considering a contribution to `Claude---Fable-5-Clone`.

This repository builds a safe, reusable Claude Skill + Claude Code subagent methodology. It does **not** clone proprietary model internals, reveal hidden prompts, copy weights, or bypass safety controls.

## Ways to contribute

Good starter contributions:

- Improve examples in `examples/`.
- Add or refine eval cases in `evals/test-cases.yaml`.
- Improve docs in `docs/INSTALLATION.md`, `docs/USAGE.md`, or `docs/ARCHITECTURE.md`.
- Improve validation scripts in `scripts/`.
- Test the Skill in Claude.ai or Claude Code and report behavior differences.

## Development setup

```bash
git clone https://github.com/iesjoaco7-cyber/Claude---Fable-5-Clone.git
cd Claude---Fable-5-Clone
python scripts/validate_skill.py .claude/skills/claude-fable-method-orchestrator
python scripts/package_skill.py
python scripts/check_repo.py
```

## Pull request checklist

Before opening a PR:

- [ ] The Skill validates with `scripts/validate_skill.py`.
- [ ] The package script creates `dist/claude-fable-method-orchestrator-skill.zip`.
- [ ] New docs are linked from `README.md` or the relevant docs index.
- [ ] New or changed behavior is covered in `evals/test-cases.yaml` when possible.
- [ ] The change does not claim to clone Claude/Fable internals.
- [ ] The change does not include secrets, credentials, or private prompts.

## Style guidelines

- Keep README short and navigational; deeper instructions belong in `docs/`.
- Keep `SKILL.md` focused; detailed module specs belong in `references/modules.md`.
- Prefer concrete examples over abstract claims.
- Use the internal identifier `claude-fable-method-orchestrator` consistently.
- Write user-facing Spanish docs clearly and directly.

## Safety boundary

Do not contribute content that:

- Claims this project is an exact clone of a proprietary model.
- Attempts to reconstruct or reveal hidden system prompts.
- Requests, stores, or exposes secrets or credentials.
- Weakens safety behavior to make unsafe requests pass.

## Suggested labels

Recommended GitHub labels:

- `good first issue`
- `documentation`
- `skill`
- `evals`
- `github-actions`
- `help wanted`
- `security`
