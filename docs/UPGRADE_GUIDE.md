# Upgrade Guide — Claude---Fable-5-Clone → Fable Method Orchestrator v2

Cómo aplicar la mejora al repositorio existente, archivo por archivo, sin romper la estructura actual.

## 0. Decisión de nombres

- **Repo público:** se mantiene `Claude---Fable-5-Clone` (no hace falta renombrar en GitHub).
- **Identificador interno nuevo:** `claude-fable-method-orchestrator` reemplaza a `claude-fable-5-clone` como nombre de Skill, subagente y agent JSON. Un solo identificador para los tres artefactos elimina la inconsistencia actual (skill=`claude-fable-5-clone`, subagent=`claude-fable-5-orchestrator`).
- Mantené la carpeta vieja durante una versión como alias deprecado o borrala directamente; no tengas ambas Skills activas al mismo tiempo (competirían por triggering).

## 1. Cambios por archivo

### README.md
- Actualizar identificador interno a `claude-fable-method-orchestrator` en toda referencia (estructura, comandos cp, prompts de ejemplo, nombre del ZIP).
- Reemplazar la tabla de herramientas: agregar Constraint Detector, Debugging Loop, Repo Maintainer, Skill Packager, Evaluation Runner (15 módulos, ver `references/modules.md`).
- Agregar sección "Regla de proporcionalidad" al flujo principal (evita que el agente sobre-planifique tareas simples).
- Reemplazar la sección de licencia/estructura según el nuevo árbol (SKILL.md ahora tiene `references/modules.md`).
- Usar la "Versión final resumida para README" entregada en la respuesta del asistente.

### CLAUDE.md
- Agregar dos reglas: (1) "Match process weight to task weight — no plans for trivial questions"; (2) "A failed quality gate means fix, not disclaim".
- Actualizar el nombre de la Skill requerida a `claude-fable-method-orchestrator`.
- El resto se mantiene: ya es conciso y correcto.

### .claude/skills/claude-fable-5-clone/SKILL.md
- **Reemplazar por completo** con `.claude/skills/claude-fable-method-orchestrator/SKILL.md` (nuevo folder, nuevo name en frontmatter — folder y `name` deben coincidir).
- Agregar `references/modules.md` (progressive disclosure: el detalle de módulos sale del SKILL.md).
- Cambios clave vs. versión anterior: descripción "pushy" con triggers concretos; regla de proporcionalidad; safety boundary canónico único; quality gates con remediación; formatos de salida independientes del idioma.

### .claude/agents/claude-fable-5-orchestrator.md
- **Reemplazar** por `.claude/agents/claude-fable-method-orchestrator.md`.
- Nota: los campos `effort:` y `skills:` del frontmatter original no están en el set básico documentado (`name`, `description`, `tools`, `model`). Verificalos contra https://docs.claude.com/en/docs/claude-code/ antes de re-agregarlos; si tu versión de Claude Code los soporta, podés sumarlos de nuevo.

### agents/claude-fable-5-clone.json
- **Reemplazar** por `agents/claude-fable-method-orchestrator.json`.
- Mejoras: identifier nuevo, whenToUse con 4 ejemplos (incluye debugging y el caso inseguro), systemPrompt sincronizado con `prompts/system-prompt.md` (una sola fuente de verdad).

### prompts/one-shot-claude-fable-5-distillation.md
- Mantener, pero actualizar los nombres de archivos objetivo (`claude-fable-method-orchestrator`) y agregar a los entregables: regla de proporcionalidad, failure signals en evals, y remediación en quality gates.

### docs/ARCHITECTURE.md
- Actualizar el flujo de ejecución: insertar "Constraint Detector" entre Context Harvester y Mode selection, y "Proportionality check" antes de Plan Builder.
- Actualizar nombres de artefactos.

### docs/TOOLS.md
- Reemplazar contenido por un puntero a `.claude/skills/claude-fable-method-orchestrator/references/modules.md` (o copiar ese archivo aquí). Evitá mantener dos listas de módulos divergentes — era una de las fallas de la v1.

### evals/test-cases.yaml
- **Reemplazar** por la versión nueva: 12 casos, cada uno con `failure_signals` y `pass_criterion` (la v1 solo tenía expected_behavior vagos).

### scripts/validate_skill.py
- Agregar dos validaciones: (1) el `name` del frontmatter coincide con el nombre de la carpeta; (2) todos los archivos referenciados en SKILL.md (p.ej. `references/modules.md`) existen.

## 2. Aplicar los archivos

```bash
# desde la raíz del repo, con los archivos nuevos en ./upgrade/
mkdir -p .claude/skills/claude-fable-method-orchestrator/references
cp upgrade/.claude/skills/claude-fable-method-orchestrator/SKILL.md .claude/skills/claude-fable-method-orchestrator/
cp upgrade/.claude/skills/claude-fable-method-orchestrator/references/modules.md .claude/skills/claude-fable-method-orchestrator/references/
cp upgrade/.claude/agents/claude-fable-method-orchestrator.md .claude/agents/
cp upgrade/agents/claude-fable-method-orchestrator.json agents/
cp upgrade/prompts/system-prompt.md prompts/
cp upgrade/evals/test-cases.yaml evals/

# retirar los artefactos viejos (o moverlos a legacy/)
git rm -r .claude/skills/claude-fable-5-clone
git rm .claude/agents/claude-fable-5-orchestrator.md
git rm agents/claude-fable-5-clone.json
```

## 3. Validar y empaquetar

```bash
python scripts/validate_skill.py .claude/skills/claude-fable-method-orchestrator
python scripts/package_skill.py   # ajustar el script al nuevo path/nombre de ZIP
```

## 4. Guardar en Git

```bash
git status
git add .
git commit -m "Improve fable method orchestrator: unified identifier, proportionality rule, canonical safety boundary, module reference, evals with failure signals"
git push
```

## 5. Verificación post-upgrade

- [ ] `validate_skill.py` pasa sobre la carpeta nueva.
- [ ] No queda ninguna referencia a `claude-fable-5-clone` fuera de la sección "historial" del README (`grep -rn "fable-5-clone" .` debe devolver solo lo esperado).
- [ ] En Claude.ai: subir el ZIP nuevo, desactivar/borrar la Skill vieja, probar con el caso `simple_question` (no debe planificar) y con `unsafe_extraction` (debe rechazar + ofrecer alternativa).
- [ ] En Claude Code: `Use the claude-fable-method-orchestrator agent to audit this repo` produce el formato Summary/Evidence/Result/Risks.
