# Claude---Fable-5-Clone

**Nombre público del repositorio:** `Claude---Fable-5-Clone`

**Nombre interno de Skill/agent:** `claude-fable-5-clone`

> Skill + subagent + prompt-pack para construir un **agente LLM reutilizable inspirado en la metodología de trabajo de Claude Fable 5**, sin intentar copiar pesos, sistema interno, prompts privados ni herramientas propietarias.

## Qué es este proyecto

Este repositorio usa el nombre que elegiste, `Claude---Fable-5-Clone`, pero mantiene una frontera ética y técnica: no intenta copiar secretos internos, pesos, prompts ocultos ni herramientas privadas de Claude/Fable. Su objetivo es crear un **clon funcional de metodología**: una Skill portable, un subagente y un prompt pack para reproducir flujos de trabajo avanzados y verificables.

`claude-fable-5-clone` es un repositorio listo para GitHub que contiene:

- Una **Claude Skill** portable para Claude.ai y Claude Code.
- Un **subagente de Claude Code** para análisis, planificación, implementación y verificación.
- Un **prompt único seguro** para pedirle a Fable 5 que genere una especificación de agente basada en comportamientos observables, no en secretos internos.
- Documentación de arquitectura, herramientas conceptuales y flujo de uso.
- Scripts para validar y empaquetar la Skill.

Este proyecto no entrena ni clona un modelo fundacional. En lugar de eso, crea una capa reutilizable de instrucciones, checklists, herramientas conceptuales, rutinas de verificación y plantillas para que cualquier modelo capaz pueda responder con un estilo de trabajo más sistemático, profundo y agentivo.

## Lo que sí hace

- Estandariza cómo el agente entiende preguntas, consultas, problemas, análisis y tareas de código.
- Aplica un flujo tipo: **intención → contexto → plan → ejecución → verificación → respuesta final**.
- Divide tareas grandes en módulos: investigación, planificación, código, debugging, diseño, documentación y control de calidad.
- Permite usarlo en distintos proyectos mediante GitHub.
- Se puede subir como Skill a Claude.ai o usar dentro de `.claude/skills/` en Claude Code.
- Incluye un subagente para Claude Code dentro de `.claude/agents/`.

## Lo que no hace

- No extrae el system prompt de Fable 5.
- No copia pesos, parámetros ni arquitectura privada.
- No intenta saltar políticas de seguridad.
- No promete una copia exacta de Fable 5.
- No convierte una Skill en un modelo entrenado “de por vida”. Una Skill persiste como archivo reutilizable; el comportamiento final depende del modelo donde la uses.

## Estructura del repositorio

```txt
Claude---Fable-5-Clone/
├─ README.md
├─ CLAUDE.md
├─ LICENSE
├─ .gitignore
├─ .claude/
│  ├─ skills/
│  │  └─ claude-fable-5-clone/
│  │     ├─ SKILL.md
│  │     └─ references/
│  │        └─ agent-prompt-agent-creation-architect.md
│  └─ agents/
│     └─ claude-fable-5-orchestrator.md
├─ agents/
│  └─ claude-fable-5-clone.json
├─ prompts/
│  └─ one-shot-claude-fable-5-distillation.md
├─ docs/
│  ├─ ARCHITECTURE.md
│  ├─ TOOLS.md
│  ├─ USAGE_CLAUDE_WEB_CODE_DESIGN.md
│  └─ agent-prompt-agent-creation-architect.md
├─ examples/
│  └─ example-requests.md
├─ evals/
│  └─ test-cases.yaml
└─ scripts/
   ├─ package_skill.py
   └─ validate_skill.py
```

## Instalación rápida en Claude.ai versión web

1. Activá **Code execution and file creation** en la configuración de Claude.
2. Entrá a **Customize → Skills**.
3. Subí el ZIP de la Skill: `claude-fable-5-clone-skill.zip`.
4. Activá la Skill.
5. En un chat nuevo, probá:

```txt
Usá la skill claude-fable-5-clone para analizar este problema como un agente de alto rendimiento: [pegá tu tarea]
```

## Instalación rápida en Claude Code

Dentro de cualquier proyecto:

```bash
mkdir -p .claude/skills .claude/agents
cp -R Claude---Fable-5-Clone/.claude/skills/claude-fable-5-clone .claude/skills/
cp Claude---Fable-5-Clone/.claude/agents/claude-fable-5-orchestrator.md .claude/agents/
```

Luego, en Claude Code:

```txt
Usá la skill claude-fable-5-clone para planificar, implementar y verificar esta tarea.
```

O invocá el subagente:

```txt
Use the claude-fable-5-orchestrator agent to analyze this codebase and produce a safe implementation plan.
```

## Uso en Claude Design

Claude Design puede aprovechar este repositorio como contexto del proyecto:

1. Subí `CLAUDE.md`, `docs/ARCHITECTURE.md`, `docs/TOOLS.md` y el `SKILL.md` al proyecto o espacio de diseño.
2. Usá el prompt de `prompts/one-shot-claude-fable-5-distillation.md` para generar un “Design Agent Profile”.
3. Pedile a Claude Design que actúe con el protocolo de diseño visual incluido en la Skill.

## Herramientas implementadas dentro del agente

Estas herramientas son **módulos de razonamiento y trabajo**, no herramientas privadas de Fable 5:

| Herramienta | Función |
|---|---|
| Intent Router | Clasifica si la tarea es pregunta, código, investigación, diseño, documento, debugging o análisis. |
| Context Harvester | Extrae requisitos, restricciones, archivos, objetivos y supuestos. |
| Plan Builder | Divide tareas complejas en fases ejecutables. |
| Research Synthesizer | Organiza información y separa hechos, inferencias y dudas. |
| Code Operator | Lee, modifica y explica código cuando el entorno lo permite. |
| Test & Verify Loop | Define pruebas, criterios de aceptación y verificación. |
| Design Critic | Revisa UX/UI, consistencia visual y fidelidad de diseño. |
| Safety Boundary | Evita extracción de secretos, abuso, acciones peligrosas o afirmaciones falsas. |
| Response Composer | Entrega respuestas claras, accionables y adaptadas al usuario. |
| Memory Packager | Convierte aprendizajes del proyecto en reglas reutilizables. |

## Flujo principal del agente

```txt
1. Entender la tarea.
2. Detectar restricciones y riesgos.
3. Elegir modo de trabajo.
4. Crear plan breve si la tarea es compleja.
5. Ejecutar por pasos.
6. Verificar con criterios concretos.
7. Entregar resultado final con próximos pasos.
```

## Prompt único para pedirle a Fable 5 una especificación segura

El prompt está en:

```txt
prompts/one-shot-claude-fable-5-distillation.md
```

Ese prompt está diseñado para obtener una **especificación operacional reutilizable**: flujos, criterios, módulos, formatos, tests y hábitos de respuesta. No solicita prompts ocultos, políticas internas, datos privados, pesos ni arquitectura propietaria.

## Crear el ZIP de la Skill

```bash
python scripts/package_skill.py
```

Resultado:

```txt
dist/claude-fable-5-clone-skill.zip
```

## Validar la Skill

```bash
python scripts/validate_skill.py .claude/skills/claude-fable-5-clone
```

## Subir a GitHub desde cero

```bash
git init
git add .
git commit -m "Initial claude fable 5 clone skill"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/Claude---Fable-5-Clone.git
git push -u origin main
```

## Licencia

MIT. Usalo, modificalo y adaptalo para tus proyectos.
