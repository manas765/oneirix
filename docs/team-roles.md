# Team Roles

## Person 1 — AI & Narrative Systems
- Dream input parsing (text → Dream State JSON)
- Last-moment / unfinished-point detection
- AI Story Director: genre selection, genre fusion, plot generation
- Event JSON generation (`docs/event-schema.md`)
- Story memory, story-state validation, repetition guard
- Content moderation on dream input

## Person 2 — 3D Game Engine & Gameplay
- Character controller: walk, run, jump, camera/mouse control
- Interaction system: open, pick up, inspect, activate
- Investigation mode + inventory
- Consuming Event JSON (from P1) and driving actual gameplay
- Controller support, motion-sickness / comfort options

## Person 3 — Environment Art & Atmosphere
- Modular environment kit organized by `setting_category`
  (Indoor, Institutional, Outdoor, Urban, Transit, Abstract)
- Starter templates for common dream settings
- Lighting / post-processing rules for the reality-to-dream visual language
- Audio design — ambient sound, dream-logic sfx
- Recurring symbol/object visuals
- Dream Journal art (diegetic in-world if possible)

## Person 4 — Backend & Persistence
- Backend service (FastAPI or Node) + database for Dream State & Story Memory
- Save/resume, cloud save
- Dream Journal data layer
- API layer connecting P1's AI output to P2's game client

## Shared / Team Decisions
- Engine choice (Unity vs Unreal) — lock before P2/P3 start building
- Event JSON schema — P1 + P2, updated as a team
- Dream State schema — P1 + P3, updated as a team
- `setting_category` enum — must stay in sync between P1's parser output
  and P3's folder structure

## Build Order

1. Lock Event JSON + Dream State schemas together
2. Parallel: P1 builds parsing + one hardcoded branch; P2 builds greybox
   character controller; P3 builds the first real environment; P4 stands
   up backend + save/resume
3. Integrate: swap greybox for real environment, wire AI output through
   backend into engine
4. Polish pass: audio, transitions, journal UI, playtest the MVP loop end to end
