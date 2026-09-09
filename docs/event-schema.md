# Event JSON Schema

The AI Story Director never controls the game directly. It outputs
structured **events**. The 3D Game Engine (Person 2) interprets these
events and performs the actual gameplay.

This is the contract between P1 (AI) and P2 (engine) — agree on changes
to this file as a team before implementing against it.

## Base Event Shape

```json
{
  "event_id": "evt_0001",
  "event_type": "mystery_trigger",
  "setting_category": "institutional",
  "location": "hostel_corridor",
  "description": "A distant sound is heard again.",
  "atmosphere_tags": ["tense", "quiet"],
  "clue": "wet_footprints",
  "requires_items": [],
  "grants_items": ["wet_footprints"],
  "characters_involved": [],
  "next_possible_events": [
    "follow_footprints",
    "return_to_room",
    "inspect_door"
  ]
}
```

## Field Notes

- `event_type` — enum, defined by P1 & P2 together (e.g. `mystery_trigger`,
  `character_appear`, `environment_shift`, `dialogue`, `world_rule_change`)
- `setting_category` — matches the categories P3's environment kit is
  organized by (`indoor`, `institutional`, `outdoor`, `urban`, `transit`,
  `abstract`) so the engine knows which modular pieces are relevant
- `location` — references a named location in the current Dream State,
  not a free-text description
- `next_possible_events` — a menu, not a free choice; keeps AI output
  inside a space the engine already knows how to render (see spec section 18)

## Open Questions (fill in as a team)

- [ ] Full `event_type` enum
- [ ] How `world_rule_change` events describe physics/rule changes
  (see spec section 68 — gravity, time, spatial anomalies)
- [ ] Versioning strategy for this schema as it grows
