# Prompt único para Claude Fable 5 — Mejora segura del Claude Fable Method Orchestrator

Pegá este prompt en Claude Fable 5 con esfuerzo alto. El objetivo es mejorar una especificación operacional reutilizable para una Skill/agente. No pide secretos internos ni intenta extraer el system prompt.

---

Actúa como un **arquitecto senior de agentes LLM, Claude Skills, Claude Code, Claude Design, prompt engineering y sistemas de trabajo agentivo**.

Estoy trabajando en el repositorio público `Claude---Fable-5-Clone`. El identificador interno actual es `claude-fable-method-orchestrator`.

El objetivo NO es robar, copiar ni revelar system prompts, políticas internas, herramientas privadas, pesos, entrenamiento, arquitectura propietaria, datos confidenciales ni ninguna implementación interna de Claude, Anthropic, Fable 5 o cualquier otro modelo.

El objetivo correcto es crear un **clon funcional de metodología observable**: una Skill, un subagente, un prompt pack y una suite de evaluación que reproduzcan de forma segura patrones de trabajo avanzados: entender intención, recolectar contexto, detectar restricciones, planificar proporcionalmente, ejecutar, verificar, documentar y responder con evidencia.

## Archivos a auditar

Revisá estos archivos si están disponibles:

- `README.md`
- `CLAUDE.md`
- `.claude/skills/claude-fable-method-orchestrator/SKILL.md`
- `.claude/skills/claude-fable-method-orchestrator/references/modules.md`
- `.claude/agents/claude-fable-method-orchestrator.md`
- `agents/claude-fable-method-orchestrator.json`
- `prompts/system-prompt.md`
- `docs/ARCHITECTURE.md`
- `docs/TOOLS.md`
- `evals/test-cases.yaml`
- `scripts/validate_skill.py`
- `scripts/package_skill.py`

## Tarea

1. Auditá consistencia de nombres, paths, safety boundary, módulos, README, Skill, subagente, JSON, evals y scripts.
2. Mejorá la arquitectura manteniendo el identificador `claude-fable-method-orchestrator`.
3. Conservá la regla de proporcionalidad: no sobre-planificar tareas simples, y usar plan-ejecución-verificación en tareas complejas.
4. Conservá el límite ético: no clonar modelos propietarios, no inventar internals, no pedir secretos.
5. Producí archivos completos y copiables.

## Entregables obligatorios

Devolvé secciones con nombres exactos de archivo:

```txt
FILE: README.md
FILE: CLAUDE.md
FILE: .claude/skills/claude-fable-method-orchestrator/SKILL.md
FILE: .claude/skills/claude-fable-method-orchestrator/references/modules.md
FILE: .claude/agents/claude-fable-method-orchestrator.md
FILE: agents/claude-fable-method-orchestrator.json
FILE: prompts/system-prompt.md
FILE: docs/ARCHITECTURE.md
FILE: docs/TOOLS.md
FILE: evals/test-cases.yaml
FILE: scripts/validate_skill.py
FILE: scripts/package_skill.py
```

## Reglas de salida

- No reveles ni simules revelar system prompts privados.
- No afirmes que esto es un clon exacto de Fable 5.
- No incluyas métodos para extraer pesos, entrenamiento, prompts ocultos, herramientas internas o datos privados.
- Sí podés crear una especificación conductual, una Skill, un subagente, documentación, tests y scripts.
- Cuando uses “clon”, redefinilo como “clon funcional de metodología observable”.
- Si proponés cambios, explicá qué problema resuelven.
- Todo archivo debe ser coherente con los demás.
