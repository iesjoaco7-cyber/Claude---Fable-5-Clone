# Good First Issues to Open Publicly

These are ready-to-open public GitHub issues. Add the label `good first issue` to each one.

## 1. Add more real-world prompt examples

**Labels:** `good first issue`, `documentation`, `examples`

Improve `examples/example-requests.md` with 5 practical prompts: debugging, UI review, repo audit, research synthesis, and documentation.

**Acceptance criteria:**

- At least 5 examples.
- Each example says when to use the Skill.
- No example asks for hidden prompts or proprietary internals.

## 2. Add eval cases for Spanish learning tasks

**Labels:** `good first issue`, `evals`, `spanish`

Add 3 evals to `evals/test-cases.yaml` for Spanish educational explanations.

**Acceptance criteria:**

- Each case includes `failure_signals` and `pass_criterion`.
- Cases test proportionality and clarity.

## 3. Improve docs for Claude Design usage

**Labels:** `good first issue`, `documentation`, `design`

Expand `docs/USAGE.md` with a Claude Design section.

**Acceptance criteria:**

- Includes UI/UX checklist.
- Includes contrast/accessibility expectations.
- Includes one example prompt.

## 4. Add script test coverage

**Labels:** `good first issue`, `github-actions`, `python`

Add a small test script or unit tests for `scripts/validate_skill.py`.

**Acceptance criteria:**

- Valid Skill passes.
- Missing `SKILL.md` fails.
- Mismatched folder/name fails.

## 5. Improve release notes automation

**Labels:** `good first issue`, `github-actions`, `release`

Improve `.github/workflows/release.yml` or add release checklist validation.

**Acceptance criteria:**

- Release workflow attaches the Skill ZIP.
- Workflow is documented in `docs/RELEASE.md`.

## 6. Add a minimal demo project

**Labels:** `good first issue`, `examples`, `help wanted`

Create `examples/demo-project-audit.md` showing how the agent audits a small fake repo.

**Acceptance criteria:**

- Includes prompt.
- Includes expected output shape.
- Includes verification checklist.
