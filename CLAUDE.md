# CLAUDE.md — Project Instructions

This repository defines a reusable Skill/subagent package named `claude-fable-5-clone`.

## Project goal

Build a safe, portable, high-performance agent workflow inspired by the observable working style of Claude Fable 5. Do not claim to clone Fable 5 exactly. Do not request or reproduce proprietary system prompts, hidden policies, model weights, training data, private tools, or internal implementation details.

## Operating rules

- Prefer clear plans for complex work.
- Always separate facts, assumptions, and recommendations.
- Verify outputs with concrete acceptance criteria.
- For code tasks, inspect existing files before changing them.
- For design tasks, check layout, hierarchy, accessibility, consistency, and implementation constraints.
- For documents, produce complete usable text when requested.
- Keep the repo Skill-compatible: the skill folder must contain `SKILL.md` with valid YAML frontmatter.

## Safety boundary

If a user asks to extract, leak, bypass, jailbreak, steal, or clone hidden model internals, refuse that part and offer a safe alternative: behavioral specification, prompt pack, eval harness, workflow, or open-source agent architecture.
