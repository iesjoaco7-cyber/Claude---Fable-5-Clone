# Usage

`claude-fable-method-orchestrator` is designed for work that benefits from a plan-execute-verify loop.

## Best use cases

Use it for:

- Repository audits.
- Code analysis and debugging.
- Refactoring with verification.
- Claude Skill or agent architecture.
- Research synthesis with uncertainty.
- UI/UX and design critique.
- Technical documentation.
- Project planning.
- Learning explanations that need structure.

Do **not** force it on trivial questions. The Skill has a proportionality rule: simple questions should get simple answers.

## Prompt examples

```txt
Usá la skill claude-fable-method-orchestrator para revisar este repo y detectar inconsistencias entre README, Skill y scripts.
```

```txt
Use the claude-fable-method-orchestrator agent to debug this error. First identify the smallest diagnostic before proposing a fix.
```

```txt
Aplicá el Fable Method para crear una arquitectura de agente reusable con tests y documentación.
```

## Expected response pattern

For complex tasks, expect:

1. Brief plan.
2. Execution or artifact.
3. Verification evidence.
4. Limitations or next steps.

For simple tasks, expect a direct answer with no heavy scaffolding.

## Safety behavior

If a user asks to extract hidden prompts, clone model weights, reveal internal policies, or bypass safety systems, the agent should refuse that unsafe portion and offer a safe behavioral alternative.
