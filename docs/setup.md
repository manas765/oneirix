# Setup

## Engine

- [ ] **Decide: Unity or Unreal** — write the decision here once made, and
  the version to standardize on. Everyone must use the same version to
  avoid file/asset conflicts.

Engine version: _TBD_

## Required per role

| Role | Tools |
|---|---|
| P1 — AI & Narrative | Python (or Node) for the AI service, an LLM API key, JSON schema validator of choice |
| P2 — Gameplay | Unity/Unreal (see above), Git LFS for scene files |
| P3 — Environment Art | Unity/Unreal (see above), Blender or equivalent for props, Git LFS for meshes/textures/audio |
| P4 — Backend | Python/FastAPI or Node, a database (start with SQLite/Postgres locally) |

## Git LFS

3D projects generate large binary files (meshes, textures, audio, scenes).
Set up [Git LFS](https://git-lfs.com/) **before** anyone commits binary
assets, or the repo will bloat fast and become painful to clone.

```
git lfs install
git lfs track "*.fbx" "*.png" "*.wav" "*.mp3" "*.uasset" "*.unity" "*.blend"
git add .gitattributes
```

## Branching

- `main` — always playable
- Feature branches per person/task, PR into `main`
- Agree on a lightweight PR review habit early (even a quick sanity check
  from one other person) so schema changes in `docs/` don't silently
  diverge from what people are building against
