# Security Policy

## Supported versions

This repository currently supports the latest `main` branch and tagged releases starting at `v0.1.0`.

| Version | Supported |
|---|---|
| `main` | Yes |
| `v0.1.x` | Yes |

## Reporting a vulnerability

Please do **not** open a public issue for secrets, credential leaks, prompt-injection findings, or unsafe behavior that could be abused.

Use GitHub private vulnerability reporting if it is enabled for the repository. If it is not enabled yet, contact the repository owner directly and include:

- A short description of the issue.
- Steps to reproduce.
- Impact and affected files.
- Suggested fix, if known.

## What counts as a security issue here

Examples:

- The Skill encourages revealing hidden prompts, secrets, credentials, or private policies.
- A workflow prints secrets to logs.
- A script packages files that should not be shipped.
- Documentation tells users to run destructive commands without warning.
- The agent claims unsafe equivalence with a proprietary model.

## Safe contribution rule

This project builds a behavioral methodology only. Reports or PRs that attempt to extract, reconstruct, or publish hidden proprietary model internals will be rejected.
