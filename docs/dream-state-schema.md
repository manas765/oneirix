# Dream State Schema

Output of the Dream Parser (Person 1) after processing the player's raw
dream description. This is what everything downstream — the AI Director,
the environment loader (Person 3), the backend (Person 4) — is built on.

## Draft Shape

```json
{
  "dream_id": "dream_0001",
  "player_id": "player_0001",
  "raw_input": "I was sleeping in my hostel. Suddenly I heard someone crying outside...",
  "setting_category": "institutional",
  "location_name": "hostel_room",
  "scale": "small_interior",
  "time_of_day": "night",
  "characters": [],
  "objects": ["door"],
  "events": [
    "sleeping",
    "heard_crying",
    "opened_door"
  ],
  "atmosphere": ["calm", "strange"],
  "final_moment": "opened_door_corridor_empty",
  "unresolved_elements": ["source_of_crying"],
  "known_mysteries": []
}
```

## Why `setting_category` and `scale` matter

The dream can start **anywhere** — not just a hostel. `setting_category`
tells Person 3's environment system which modular kit to pull from
(Indoor / Institutional / Outdoor / Urban / Transit / Abstract), and
`scale` tells it roughly how large a space to assemble. This is what lets
one modular kit represent many different real dreams instead of needing
a bespoke environment per playthrough.

## Open Questions (fill in as a team)

- [ ] Full `setting_category` enum — must match Person 3's folder
  structure under `Assets/Environments/`
- [ ] How atmosphere tags map to P3's lighting/post-processing presets
- [ ] Minimum fields required before the engine can render a starting
  environment (fallback behavior if parsing is incomplete)
