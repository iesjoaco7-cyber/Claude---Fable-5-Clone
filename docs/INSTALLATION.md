# Installation

This guide explains how to install `claude-fable-method-orchestrator` in Claude.ai and Claude Code.

## Claude.ai web

1. Download or generate the Skill ZIP:

```bash
python scripts/package_skill.py
```

2. Use the generated file:

```txt
dist/claude-fable-method-orchestrator-skill.zip
```

3. In Claude.ai, open:

```txt
Customize → Skills → Upload skill
```

4. Upload the ZIP and enable the Skill.

5. Test it with:

```txt
Usá la skill claude-fable-method-orchestrator para auditar este problema y darme una respuesta verificada: [tu tarea]
```

## Claude Code

From a target project, copy the Skill and subagent:

```bash
mkdir -p .claude/skills .claude/agents
cp -R /path/to/Claude---Fable-5-Clone/.claude/skills/claude-fable-method-orchestrator .claude/skills/
cp /path/to/Claude---Fable-5-Clone/.claude/agents/claude-fable-method-orchestrator.md .claude/agents/
```

Then ask Claude Code:

```txt
Use the claude-fable-method-orchestrator agent to audit this repo and produce a safe implementation plan.
```

## Do not activate duplicate Skills

Do not keep the old `claude-fable-5-clone` Skill enabled together with `claude-fable-method-orchestrator`. They may compete for activation.

## Validate locally

```bash
python scripts/validate_skill.py .claude/skills/claude-fable-method-orchestrator
python scripts/package_skill.py
python scripts/check_repo.py
```
