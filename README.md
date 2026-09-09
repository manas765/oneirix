# ONEIRIX — AI Continuation of Unfinished Dreams

> "I dreamt it. I woke up. ONEIRIX tells me what happened next."

A 3D AI-powered narrative game. The player describes a real unfinished dream;
ONEIRIX reconstructs the last remembered moment as an explorable 3D
environment, then an AI Story Engine takes over and continues the story
based on player actions.

Full concept & feature spec: [`docs/spec.md`](docs/spec.md)

---

## Team & Ownership

| Person | Area | Owns |
|---|---|---|
| **P1** | AI & Narrative Systems | Dream parsing, Dream State JSON, AI Story Director, Event JSON generation, story memory, content moderation |
| **P2** | 3D Game Engine & Gameplay | Character controller, interaction system, investigation mode, consuming Event JSON into gameplay |
| **P3** | Environment Art & Atmosphere | Modular environment kit, lighting/post-processing, audio design, Dream Journal art |
| **P4** | Backend & Persistence | Backend API, database, save/resume, connecting AI output to game client |

See [`docs/team-roles.md`](docs/team-roles.md) for the full breakdown.

## The Shared Contract

Everything P1 (AI) and P2 (game engine) build depends on one shared data
format — the **Event JSON schema**. Lock this early; don't build gameplay
or AI logic against a schema that isn't agreed on yet.

See [`docs/event-schema.md`](docs/event-schema.md) and
[`docs/dream-state-schema.md`](docs/dream-state-schema.md).

## Repo Structure

```
oneirix/
├── docs/                   # Specs, schemas, design docs
├── Assets/
│   ├── Environments/       # Modular kit, organized by setting category
│   │   ├── Indoor/
│   │   ├── Institutional/
│   │   ├── Outdoor/
│   │   ├── Urban/
│   │   ├── Transit/
│   │   └── Abstract/       # Liminal / dream-logic spaces
│   ├── Prefabs/
│   ├── Materials/
│   └── Audio/
├── Scripts/
│   ├── AI/                 # Dream parsing, Story Director integration
│   ├── Gameplay/           # Character controller, interaction
│   ├── Backend/            # API client, save/resume
│   └── Environment/        # Procedural dressing, template loader
└── Scenes/
```

## MVP Scope (current target)

1. Dream text input → parsing → Dream State
2. One fully polished starter environment (built from the modular kit)
3. Character movement (walk/run/jump) + camera + basic interaction
4. AI-generated story continuation, one mystery, one clue, one riddle
5. Save/resume

Full MVP list: see `docs/spec.md` section 14.

## Getting Started

1. Clone the repo
2. See `docs/setup.md` for engine version and required software per role
3. Check `docs/event-schema.md` before writing any AI-output or gameplay-input code
4. Open an issue or claim a task before starting new work, to avoid overlap

## Engine

Unity **or** Unreal Engine (decide and lock in `docs/setup.md` before Person 2/3 start building — this affects everyone's file formats).

## License

TBD.
