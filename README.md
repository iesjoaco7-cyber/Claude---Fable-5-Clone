# Claude---Fable-5-Clone

[![Validate Repository](https://github.com/iesjoaco7-cyber/Claude---Fable-5-Clone/actions/workflows/validate.yml/badge.svg)](https://github.com/iesjoaco7-cyber/Claude---Fable-5-Clone/actions/workflows/validate.yml)

**Nombre público del repositorio:** `Claude---Fable-5-Clone`  
**Nombre interno de Skill/agent:** `claude-fable-method-orchestrator`  
**Nombre público del agente:** `Claude Fable Method Orchestrator`

> Claude Skill + Claude Code subagent + prompt pack para trabajar con una metodología agentiva reutilizable: intención → contexto → restricciones → plan proporcional → ejecución → verificación → entrega.

Este proyecto conserva el nombre público original, pero **no clona ningún modelo propietario**. No extrae system prompts ocultos, pesos, parámetros, herramientas internas ni políticas privadas. Construye una capa segura de comportamiento observable, documentación, módulos conceptuales y evaluación.

## Documentación rápida

| Tema | Archivo |
|---|---|
| Instalación | [`docs/INSTALLATION.md`](docs/INSTALLATION.md) |
| Uso | [`docs/USAGE.md`](docs/USAGE.md) |
| Arquitectura | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| Herramientas/módulos | [`docs/TOOLS.md`](docs/TOOLS.md) |
| Ejemplos | [`examples/README.md`](examples/README.md) |
| Contribuir | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Seguridad | [`SECURITY.md`](SECURITY.md) |
| Cambios y release | [`CHANGELOG.md`](CHANGELOG.md) |
| Cómo publicar release | [`docs/RELEASE.md`](docs/RELEASE.md) |
| Good first issues | [`docs/GOOD_FIRST_ISSUES.md`](docs/GOOD_FIRST_ISSUES.md) |
| Plan para colaboradores | [`docs/COLLABORATION.md`](docs/COLLABORATION.md) |

## Qué incluye

- Claude Skill portable: `.claude/skills/claude-fable-method-orchestrator/`.
- Claude Code subagent: `.claude/agents/claude-fable-method-orchestrator.md`.
- Agent JSON reusable: `agents/claude-fable-method-orchestrator.json`.
- Prompt canónico: `prompts/system-prompt.md`.
- 15 módulos conceptuales documentados en `references/modules.md`.
- 12 casos de evaluación en `evals/test-cases.yaml`.
- GitHub Actions para validar scripts, Skill, paquete ZIP y consistencia del repo.
- Templates de issues, PR template, `CONTRIBUTING.md`, `SECURITY.md` y `CHANGELOG.md`.

## Instalación rápida

```bash
python scripts/validate_skill.py .claude/skills/claude-fable-method-orchestrator
python scripts/package_skill.py
python scripts/check_repo.py
```

Luego subí este ZIP a Claude.ai:

```txt
dist/claude-fable-method-orchestrator-skill.zip
```

Guía completa: [`docs/INSTALLATION.md`](docs/INSTALLATION.md).

## Regla central

```txt
Tarea trivial → respuesta directa, sin plan pesado.
Tarea moderada → plan interno, ejecución y nota breve de verificación.
Tarea compleja → plan visible breve, ejecución por fases y verificación con evidencia.
```

Esto evita dos errores comunes: responder sin contexto en tareas complejas y sobre-planificar preguntas simples.

## Uso rápido

```txt
Usá la skill claude-fable-method-orchestrator para auditar este repo y detectar inconsistencias entre README, Skill, scripts y evals.
```

```txt
Use the claude-fable-method-orchestrator agent to debug this error. First identify the smallest diagnostic before proposing a fix.
```

Más ejemplos: [`examples/README.md`](examples/README.md) y [`examples/example-requests.md`](examples/example-requests.md).

## Estructura

```txt
Claude---Fable-5-Clone/
├─ README.md
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ CHANGELOG.md
├─ CLAUDE.md
├─ .claude/
│  ├─ skills/claude-fable-method-orchestrator/
│  │  ├─ SKILL.md
│  │  └─ references/modules.md
│  └─ agents/claude-fable-method-orchestrator.md
├─ .github/
│  ├─ workflows/validate.yml
│  ├─ workflows/release.yml
│  ├─ ISSUE_TEMPLATE/
│  └─ PULL_REQUEST_TEMPLATE.md
├─ agents/claude-fable-method-orchestrator.json
├─ docs/
├─ examples/
├─ evals/test-cases.yaml
├─ prompts/
├─ scripts/
└─ dist/
```

## Release v0.1.0

El repo está preparado para publicar `v0.1.0`.

```bash
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

La guía completa está en [`docs/RELEASE.md`](docs/RELEASE.md).

## Contribuciones externas

Para subir señales públicas del repo:

1. Abrí issues usando [`docs/GOOD_FIRST_ISSUES.md`](docs/GOOD_FIRST_ISSUES.md).
2. Invitá 1–2 personas reales con el mensaje de [`docs/COLLABORATION.md`](docs/COLLABORATION.md).
3. Pediles PRs chicos y revisables.
4. Sumá sus nombres o usuarios a las notas de release cuando merges sus PRs.

## Límites éticos y técnicos

Este proyecto:

- No clona pesos ni parámetros.
- No reconstruye prompts ocultos.
- No simula herramientas privadas.
- No promete equivalencia exacta con Claude, Fable 5 ni ningún modelo propietario.
- Sí empaqueta una metodología conductual segura, reusable y verificable.

## Licencia

MIT. Ver [`LICENSE`](LICENSE).
