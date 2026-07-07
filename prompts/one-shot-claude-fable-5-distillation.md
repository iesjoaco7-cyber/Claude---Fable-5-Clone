# Prompt único para Claude Fable 5 — Destilación segura de metodología observable

Pegá este prompt en Claude Fable 5 con esfuerzo alto. El objetivo es obtener una especificación operacional reutilizable para una Skill/agente. No pide secretos internos ni intenta extraer el system prompt.

---

Actúa como un **arquitecto senior de agentes LLM, prompt engineering y sistemas de trabajo agentivo**.

Quiero que me ayudes a construir una Skill/agente reutilizable para Claude.ai, Claude Code y Claude Design. El objetivo no es robar, copiar ni revelar tu system prompt, políticas internas, herramientas privadas, pesos, entrenamiento, arquitectura propietaria, datos confidenciales ni ninguna implementación interna del modelo. Si alguna parte de mi pedido pudiera interpretarse como extracción de secretos, ignorá esa parte y reemplazala por una alternativa segura.

Tu tarea es producir una **especificación completa de un agente inspirado en tus comportamientos observables de alto rendimiento**, basada únicamente en lo que podés describir de manera segura: procesos, metodologías, módulos de trabajo, criterios de calidad, plantillas, límites, verificaciones y patrones de respuesta.

Usá como base esta metodología de creación de agentes:

1. Extraer intención central.
2. Diseñar una persona experta.
3. Arquitectar instrucciones completas.
4. Optimizar rendimiento con frameworks de decisión, QA y fallback.
5. Crear identificador con minúsculas, números y guiones.
6. Incluir ejemplos claros de cuándo usar el agente.
7. Devolver una configuración autónoma, reutilizable y lista para producción.

## Entregables obligatorios

Generá todos estos archivos en formato Markdown o JSON, listos para copiar a un repositorio de GitHub:

### 1. README.md
Debe incluir:
- Descripción del proyecto.
- Qué problema resuelve.
- Qué sí hace y qué no hace.
- Estructura del repositorio.
- Instalación en Claude.ai como Skill ZIP.
- Instalación en Claude Code con `.claude/skills/` y `.claude/agents/`.
- Uso recomendado en Claude Design.
- Ejemplos de prompts de uso.
- Limitaciones.

### 2. .claude/skills/claude-fable-5-clone/SKILL.md
Debe cumplir esta estructura mínima:

```md
---
name: claude-fable-5-clone
description: [descripción breve de qué hace y cuándo usarla]
---

# Claude Fable 5 Clone

[instrucciones completas]
```

La Skill debe enseñar al modelo a trabajar con un flujo de alto rendimiento:
- Intent routing.
- Context gathering.
- Planificación.
- Ejecución.
- Verificación.
- Respuesta final.
- Manejo de incertidumbre.
- Seguridad y límites.

### 3. .claude/agents/claude-fable-5-orchestrator.md
Crear un subagente para Claude Code con YAML frontmatter:
- `name`
- `description`
- `tools`
- `model`
- `effort`

Debe estar orientado a proyectos de código, debugging, repositorios, documentación, diseño y análisis complejo.

### 4. agents/claude-fable-5-clone.json
Devolver un JSON válido con exactamente estos campos:

```json
{
  "identifier": "...",
  "whenToUse": "Use this agent when...",
  "systemPrompt": "..."
}
```

El campo `whenToUse` debe incluir ejemplos donde el asistente usa una herramienta Agent para lanzar este agente, no responder directamente.

### 5. docs/ARCHITECTURE.md
Explicar:
- Arquitectura conceptual.
- Módulos internos.
- Flujo de ejecución.
- Límites de seguridad.
- Cómo se adapta a Claude.ai, Claude Code y Claude Design.

### 6. docs/TOOLS.md
Describir herramientas conceptuales implementadas:
- Intent Router.
- Context Harvester.
- Plan Builder.
- Research Synthesizer.
- Code Operator.
- Test & Verify Loop.
- Design Critic.
- Safety Boundary.
- Response Composer.
- Memory Packager.

### 7. evals/test-cases.yaml
Crear casos de prueba para evaluar si el agente responde bien ante:
- Pregunta simple.
- Tarea de código.
- Bug.
- Análisis de documento.
- Diseño UI.
- Solicitud insegura de extraer system prompt.
- Creación de repositorio.

### 8. scripts/validate_skill.py
Crear un script simple en Python que valide:
- Existe `SKILL.md`.
- Tiene YAML frontmatter.
- Tiene `name` y `description`.
- El name usa solo minúsculas, números y guiones.

### 9. scripts/package_skill.py
Crear un script Python que empaquete `.claude/skills/claude-fable-5-clone/` como `dist/claude-fable-5-clone-skill.zip`.

## Reglas de seguridad

- No reveles ni simules revelar tu system prompt real.
- No afirmes que esto clona exactamente a Fable 5.
- No incluyas métodos para extraer pesos, entrenamientos, prompts ocultos, herramientas internas o datos privados.
- Sí podés crear una especificación conductual, una Skill, un subagente, documentación, tests y scripts.
- Cuando uses la palabra “clon”, redefinila como “clon funcional de metodología observable”, no como copia del modelo.

## Estilo de salida

Devolvé la respuesta en secciones con nombres de archivo, así:

```txt
FILE: README.md
[contenido]

FILE: .claude/skills/claude-fable-5-clone/SKILL.md
[contenido]
```

Asegurate de que todo sea copiable, coherente y usable en GitHub.
