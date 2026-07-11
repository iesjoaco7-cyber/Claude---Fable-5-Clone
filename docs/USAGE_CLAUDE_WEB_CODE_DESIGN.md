# Usage across Claude surfaces

## Claude.ai web

1. Package `.claude/skills/claude-fable-method-orchestrator/` as a ZIP.
2. Open Claude.ai.
3. Enable code execution/file creation if required by your plan/settings.
4. Go to Customize → Skills.
5. Upload the ZIP.
6. Enable the Skill.

Prompt example:

```txt
Usá claude-fable-method-orchestrator para resolver este problema con planificación, ejecución y verificación: ...
```

## Claude Code

Use project-level installation:

```bash
mkdir -p .claude/skills .claude/agents
cp -R .claude/skills/claude-fable-method-orchestrator /path/to/project/.claude/skills/
cp .claude/agents/claude-fable-method-orchestrator.md /path/to/project/.claude/agents/
```

Or user-level installation:

```bash
mkdir -p ~/.claude/skills ~/.claude/agents
cp -R .claude/skills/claude-fable-method-orchestrator ~/.claude/skills/
cp .claude/agents/claude-fable-method-orchestrator.md ~/.claude/agents/
```

## Claude Design

Use this package as:

- Project instructions.
- Design review checklist.
- Context document.
- Reusable workflow for UI/UX reasoning.

Prompt example:

```txt
Aplicá el módulo Design Critic de claude-fable-method-orchestrator a este diseño. Revisá jerarquía, accesibilidad, consistencia y pasos de implementación.
```

## GitHub workflow

```bash
git init
git add .
git commit -m "Initial reusable claude fable 5 clone"
git branch -M main
git remote add origin https://github.com/YOUR_USER/Claude---Fable-5-Clone.git
git push -u origin main
```
