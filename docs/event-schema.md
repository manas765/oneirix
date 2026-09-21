# Event JSON Schema

The AI Story Director never controls the game directly. It outputs
structured **events**. The 3D Game Engine (Person 2) interprets these
events and performs the actual gameplay.

This is the contract between P1 (AI) and P2 (engine) — agree on changes
to this file as a team before implementing against it.

**Decision (locked in): `next_possible_events` uses semantic string
keys, not opaque IDs.** Earlier drafts used meaningless placeholders like
`evt_0002` — P2 flagged that these can't be turned into UI (a button
needs to say "follow the footprints," not show a random ID). Fixed below.

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

- `event_id` — still a unique identifier (e.g. `evt_0001`), used
  internally for story memory / save tracking. This is NOT what P2
  displays to the player — it's just this event's own ID, not an action.
- `event_type` — enum, defined by P1 & P2 together (e.g. `mystery_trigger`,
  `character_appear`, `environment_shift`, `dialogue`, `world_rule_change`)
- `setting_category` — matches the categories P3's environment kit is
  organized by (`indoor`, `institutional`, `outdoor`, `urban`, `transit`,
  `abstract`) so the engine knows which modular pieces are relevant
- `location` — references a named location in the current Dream State,
  not a free-text description
- `next_possible_events` — **a menu of semantic action keys** (snake_case
  strings like `follow_footprints`, `return_to_room`, `inspect_door`),
  not free-form text and not opaque IDs. P2 turns each key into a
  player-facing choice (button/prompt text) using a lookup table (see
  below). Keeps the AI's output inside a space the engine already knows
  how to render (see spec section 18).

## Action Key → Display Text

P2 maintains a lookup table mapping each semantic action key to the text
shown to the player, e.g.:

```json
{
  "follow_footprints": "Follow the footprints",
  "return_to_room": "Return to the room",
  "inspect_door": "Inspect the door"
}
```

P1 and P2 both write against this shared list of valid action keys — if
P1 introduces a new key, it needs a matching entry added to this lookup
table, or P2 has nothing to display for it.

## Open Questions (fill in as a team)

- [ ] Full `event_type` enum
- [ ] The full list of valid action keys (grows as P1 designs more
  events) — kept in sync with P2's lookup table above
- [ ] Naming convention for action keys to avoid collisions (e.g. if two
  different rooms both have a "door" — `inspect_door_bedroom` vs
  `inspect_door_corridor`, or scope keys by location some other way)
- [ ] How `world_rule_change` events describe physics/rule changes
  (see spec section 68 — gravity, time, spatial anomalies)
- [ ] Versioning strategy for this schema as it grows