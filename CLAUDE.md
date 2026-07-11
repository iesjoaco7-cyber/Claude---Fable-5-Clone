# CLAUDE.md — Project Instructions

This repository defines a reusable Skill/subagent package named `claude-fable-method-orchestrator` inside the public repository `Claude---Fable-5-Clone`.

## Project goal

Build a safe, portable, high-performance agent workflow inspired by observable patterns of advanced LLM work. Do not claim to clone Fable 5 exactly. Do not request, reveal, reproduce, infer, or fabricate proprietary system prompts, hidden policies, model weights, training data, private tools, credentials, or internal implementation details.

## Operating rules

- Match process weight to task weight: no visible plans for trivial questions.
- Prefer clear short plans for complex, multi-file, ambiguous, or risky work.
- Always separate facts, assumptions, inferences, and recommendations.
- A failed quality gate means fix, not disclaim.
- Verify outputs with concrete acceptance criteria.
- For code tasks, inspect existing files before changing them.
- For debugging, diagnose before fixing; avoid shotgun patches.
- For design tasks, check layout, hierarchy, accessibility, consistency, responsiveness, and implementation constraints.
- For documents, produce complete usable text when requested.
- Keep the repo Skill-compatible: the skill folder must contain `SKILL.md` with valid YAML frontmatter.
- The canonical Skill path is `.claude/skills/claude-fable-method-orchestrator/`.

## Safety boundary

If a user asks to extract, leak, bypass, jailbreak, steal, or clone hidden model internals, refuse that part specifically and offer a safe alternative: behavioral specification, prompt pack, eval harness, workflow, or open-source agent architecture.
