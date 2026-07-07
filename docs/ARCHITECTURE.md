# Architecture

## Concept

The Claude Fable 5 Clone is not a model clone. It is an operational layer that packages repeatable high-performance behavior into a Skill and subagent.

The architecture has four layers:

1. **Skill Layer**: `SKILL.md` provides reusable procedural knowledge.
2. **Subagent Layer**: Claude Code subagent isolates heavy repository analysis and verification.
3. **Prompt Pack Layer**: one-shot distillation prompt generates safe improvements from capable models.
4. **Evaluation Layer**: test cases validate behavior against expected outcomes.

## Execution flow

```txt
User request
  ↓
Intent Router
  ↓
Context Harvester
  ↓
Mode selection
  ↓
Plan Builder if complex
  ↓
Execution Engine
  ↓
Verifier
  ↓
Response Composer
```

## Safety boundary

The architecture refuses:

- Hidden prompt extraction.
- Proprietary model cloning.
- Weight extraction.
- Credential harvesting.
- Tool misuse.
- Unsupported claims.

It allows:

- Behavioral specifications.
- Skills.
- Subagents.
- Open workflows.
- Evaluation harnesses.
- Documentation.

## Surface adaptation

### Claude.ai
Upload the Skill as a ZIP through Customize → Skills. The Skill is private to the account unless sharing/provisioning is enabled by the organization.

### Claude Code
Place the Skill in `.claude/skills/` and the subagent in `.claude/agents/`. Commit both to version control for project-level reuse.

### Claude Design
Use the Skill as project instructions or design-system context. The Design Critic module helps with layout, hierarchy, consistency, accessibility, and implementation notes.
