# Claude---Fable-5-Clone

**Nombre público del repositorio:** `Claude---Fable-5-Clone`  
**Nombre interno actual de Skill/agent:** `claude-fable-method-orchestrator`  
**Nombre público del agente:** `Claude Fable Method Orchestrator`

> Skill + subagent + prompt-pack para construir un **agente LLM reutilizable inspirado en una metodología observable de trabajo avanzado**, sin intentar copiar pesos, sistema interno, prompts privados, herramientas propietarias ni políticas internas de ningún modelo.

## Qué es este proyecto

`Claude---Fable-5-Clone` es un repositorio para usar una metodología agentiva reutilizable en Claude.ai, Claude Code y Claude Design. Aunque el nombre público conserva la idea original de “Fable 5 Clone”, el proyecto no intenta clonar un modelo propietario. El objetivo es crear un **clon funcional de metodología observable**: una capa de instrucciones, módulos, verificaciones y plantillas para trabajar de forma más sistemática.

El agente nuevo se llama `claude-fable-method-orchestrator` y trabaja con este flujo:

```txt
intención → contexto → restricciones → plan proporcional → ejecución → verificación → entrega
```

## Qué problema resuelve

Los modelos suelen fallar cuando una tarea es larga, ambigua o técnica: empiezan a responder antes de entender el contexto, planifican demasiado para preguntas simples, hacen cambios sin verificar o mezclan hechos con suposiciones. Este repo convierte ese trabajo en una metodología explícita y reutilizable.

## Lo que sí hace

- Estandariza cómo responder preguntas, consultas, problemas, análisis, debugging, código, investigación, diseño y documentación.
- Usa una **regla de proporcionalidad**: tareas simples reciben respuestas simples; tareas complejas reciben plan, ejecución y verificación.
- Incluye una **Claude Skill** portable para Claude.ai y Claude Code.
- Incluye un **subagente de Claude Code** para repositorios, debugging, auditorías, refactors y documentación.
- Incluye un **prompt canónico** reutilizable en `prompts/system-prompt.md`.
- Incluye **15 módulos conceptuales** documentados en `references/modules.md`.
- Incluye **12 casos de evaluación** con señales de fallo y criterios de aprobación.
- Puede versionarse en GitHub y reutilizarse en cualquier proyecto.

## Lo que no hace

- No extrae system prompts ocultos.
- No copia pesos, parámetros, arquitectura privada ni entrenamiento de modelos.
- No reproduce herramientas internas ni políticas privadas.
- No intenta saltar restricciones de seguridad.
- No promete una copia exacta de Fable 5 ni de ningún modelo propietario.
- No entrena un modelo “de por vida”; una Skill es una capa reusable de instrucciones y archivos.

## Regla central de proporcionalidad

```txt
Tarea trivial → respuesta directa, sin plan ni bloques pesados.
Tarea moderada → plan interno, ejecución y nota breve de verificación.
Tarea compleja → plan visible breve, ejecución por fases, verificación con evidencia.
```

Ejemplo: para “¿qué es una subconsulta SQL?” el agente debe responder directo. Para “auditá este repo y mejorá la Skill”, debe inspeccionar archivos, planificar, proponer cambios y verificar.

## Estructura del repositorio

```txt
Claude---Fable-5-Clone/
├─ README.md
├─ CLAUDE.md
├─ LICENSE
├─ .gitignore
├─ .claude/
│  ├─ skills/
│  │  └─ claude-fable-method-orchestrator/
│  │     ├─ SKILL.md
│  │     └─ references/
│  │        └─ modules.md
│  └─ agents/
│     └─ claude-fable-method-orchestrator.md
├─ agents/
│  └─ claude-fable-method-orchestrator.json
├─ prompts/
│  ├─ system-prompt.md
│  └─ one-shot-claude-fable-5-distillation.md
├─ docs/
│  ├─ ARCHITECTURE.md
│  ├─ TOOLS.md
│  ├─ USAGE_CLAUDE_WEB_CODE_DESIGN.md
│  ├─ UPGRADE_GUIDE.md
│  └─ agent-prompt-agent-creation-architect.md
├─ examples/
│  └─ example-requests.md
├─ evals/
│  └─ test-cases.yaml
├─ scripts/
│  ├─ package_skill.py
│  └─ validate_skill.py
└─ dist/
   └─ claude-fable-method-orchestrator-skill.zip
```

## Instalación rápida en Claude.ai versión web

1. Entrá a Claude.ai.
2. Abrí **Customize → Skills**.
3. Subí el ZIP generado:

```txt
dist/claude-fable-method-orchestrator-skill.zip
```

4. Activá la Skill.
5. En un chat nuevo, probá:

```txt
Usá la skill claude-fable-method-orchestrator para analizar este problema como un agente de alto rendimiento: [pegá tu tarea]
```

Importante: no tengas activas a la vez la Skill vieja `claude-fable-5-clone` y la nueva `claude-fable-method-orchestrator`, porque competirían por activación.

## Instalación rápida en Claude Code

Dentro de cualquier proyecto:

```bash
mkdir -p .claude/skills .claude/agents
cp -R Claude---Fable-5-Clone/.claude/skills/claude-fable-method-orchestrator .claude/skills/
cp Claude---Fable-5-Clone/.claude/agents/claude-fable-method-orchestrator.md .claude/agents/
```

Luego, en Claude Code:

```txt
Use the claude-fable-method-orchestrator agent to audit this repo and produce a safe implementation plan.
```

## Uso en Claude Design

Claude Design puede usar el repo como contexto de diseño:

1. Subí `CLAUDE.md`, `docs/ARCHITECTURE.md`, `docs/TOOLS.md`, `prompts/system-prompt.md` y el `SKILL.md`.
2. Pedile que aplique el modo **Design Critic**.
3. Usalo para revisar jerarquía visual, espaciado, tipografía, contraste, accesibilidad, responsive y consistencia de componentes.

## Herramientas/módulos internos

Los módulos son conceptuales; no son herramientas privadas de ningún modelo. La especificación completa está en:

```txt
.claude/skills/claude-fable-method-orchestrator/references/modules.md
```

Módulos incluidos:

```txt
Intent Router
Context Harvester
Constraint Detector
Task Planner
Research Synthesizer
Code Operator
Debugging Loop
Design Critic
Test & Verify Loop
Safety Boundary
Response Composer
Memory Packager
Repo Maintainer
Skill Packager
Evaluation Runner
```

## Validar la Skill

```bash
python scripts/validate_skill.py .claude/skills/claude-fable-method-orchestrator
```

## Crear el ZIP de la Skill

```bash
python scripts/package_skill.py
```

Resultado:

```txt
dist/claude-fable-method-orchestrator-skill.zip
```

## Ejecutar evaluación manual

Los casos están en:

```txt
evals/test-cases.yaml
```

Incluyen pruebas para consulta simple, problema técnico, debugging, análisis de código, planificación, diseño UI/UX, investigación con incertidumbre, documentación, refactorización, explicación educativa, tarea ambigua y solicitud insegura de extracción.

## Comandos Git para actualizar

```bash
git status
git add .
git commit -m "Improve fable method orchestrator"
git push
```

## Licencia

MIT. Usalo, modificalo y adaptalo para tus proyectos.
