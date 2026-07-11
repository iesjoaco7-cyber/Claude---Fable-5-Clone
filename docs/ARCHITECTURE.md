# Architecture

## Concept

`Claude---Fable-5-Clone` is not a model clone. It is an operational layer that packages repeatable high-performance behavior into a Claude Skill, a Claude Code subagent, a prompt pack, and an evaluation suite.

The internal identifier is `claude-fable-method-orchestrator`.

## Layers

1. **Skill Layer**: `.claude/skills/claude-fable-method-orchestrator/SKILL.md` contains the compact always-loaded workflow.
2. **Reference Layer**: `.claude/skills/claude-fable-method-orchestrator/references/modules.md` contains the full module specification for progressive disclosure.
3. **Subagent Layer**: `.claude/agents/claude-fable-method-orchestrator.md` isolates repository analysis, code changes, debugging, and verification.
4. **Prompt Layer**: `prompts/system-prompt.md` is the canonical reusable system prompt; the JSON agent contains a synchronized condensed version.
5. **Evaluation Layer**: `evals/test-cases.yaml` validates behavior against success criteria and failure signals.

## Execution flow

```txt
User request
  ↓
Intent Router
  ↓
Context Harvester
  ↓
Constraint Detector
  ↓
Proportionality check
  ↓
Mode selection
  ↓
Task Planner if complex
  ↓
Execution by mode
  ↓
Test & Verify Loop
  ↓
Response Composer
```

The Safety Boundary runs across the whole flow. It refuses hidden-prompt extraction, proprietary model cloning, credential harvesting, bypass requests, and unsupported claims while preserving the safe part of the task.

## Proportionality rule

The agent must not over-process simple tasks. A quick definition or single-fact answer should be direct. A complex task should use a short plan, phased execution, and evidence-backed verification.

## Surface adaptation

### Claude.ai
Upload the generated Skill ZIP through Customize → Skills. Disable the old `claude-fable-5-clone` Skill if present to avoid trigger competition.

### Claude Code
Place the Skill in `.claude/skills/` and the subagent in `.claude/agents/`. Commit both to version control for project-level reuse.

### Claude Design
Use the Skill as project instructions or design-system context. The Design Critic module helps with layout, hierarchy, spacing, typography, contrast, accessibility, responsiveness, consistency, and implementation feasibility.

## Maintainer rule

Names and paths must stay synchronized across:

```txt
README.md
CLAUDE.md
.claude/skills/claude-fable-method-orchestrator/SKILL.md
.claude/agents/claude-fable-method-orchestrator.md
agents/claude-fable-method-orchestrator.json
prompts/system-prompt.md
scripts/package_skill.py
scripts/validate_skill.py
```
