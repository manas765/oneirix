# Setup

## Engine

**Decision: Unreal Engine** (locked in)

Engine version: 5.8.2

Install via the [Epic Games Launcher](https://www.unrealengine.com/en-US/download).

**Scripting approach:** Start with Blueprints (visual scripting) for
gameplay logic — faster to learn, capable enough for this scope. Use C++
only where needed for performance or for the backend/Event JSON
integration layer (Person 1 & Person 4). Mixing both is normal and fine.

## Required per role

| Role | Tools |
|---|---|
| P1 — AI & Narrative | Python (or Node) for the AI service, an LLM API key, JSON schema validator of choice |
| P2 — Gameplay | Unreal Engine (Epic Games Launcher), Git LFS |
| P3 — Environment Art | Unreal Engine, Blender or equivalent for props, Git LFS |
| P4 — Backend | Python/FastAPI or Node, a database (start with SQLite/Postgres locally) |

## Git LFS

Unreal projects generate large binary files (`.uasset`, `.umap`, meshes,
textures, audio). Set up [Git LFS](https://git-lfs.com/) **before**
anyone commits these, or the repo will bloat fast and become painful to
clone.

```
git lfs install
git lfs track "*.uasset" "*.umap" "*.fbx" "*.png" "*.wav" "*.mp3"
git add .gitattributes
git commit -m "Set up Git LFS for Unreal binary assets"
git push
```

## Backend/AI Integration Note (Unreal-specific)

Unreal's HTTP/JSON handling (via its `HttpModule` and `Json` modules) is
more verbose than a typical web-dev workflow. Person 1 and Person 4
should build one clean, reusable pattern early for calling the backend
and parsing Event JSON (`docs/event-schema.md`) — this gets reused
constantly, so it's worth getting right up front rather than repeating
boilerplate per feature.

## Hardware Note

Unreal is heavier to run/compile than some alternatives. Confirm
everyone's machine can handle it reasonably (a recent GPU helps) before
getting deep into environment work — flag it now if anyone's on
lower-spec hardware.

## Branching

- `main` — always playable
- Feature branches per person/task, PR into `main`
- Agree on a lightweight PR review habit early (even a quick sanity check
  from one other person) so schema changes in `docs/` don't silently
  diverge from what people are building against