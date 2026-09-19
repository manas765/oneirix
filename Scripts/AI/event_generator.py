import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

EVENT_SCHEMA = {
    "type": "object",
    "properties": {
        "event_id": {"type": "string"},
        "event_type": {
            "type": "string",
            "enum": ["mystery_trigger", "character_appear", "environment_shift", "dialogue"]
        },
        "setting_category": {
            "type": "string",
            "enum": ["indoor", "institutional", "outdoor", "urban", "transit", "abstract"]
        },
        "location": {"type": "string"},
        "description": {"type": "string"},
        "atmosphere_tags": {"type": "array", "items": {"type": "string"}},
        "clue": {"type": "string"},
        "requires_items": {"type": "array", "items": {"type": "string"}},
        "grants_items": {"type": "array", "items": {"type": "string"}},
        "characters_involved": {"type": "array", "items": {"type": "string"}},
        "next_possible_events": {"type": "array", "items": {"type": "string"}}
    },
    "required": [
        "event_id", "event_type", "setting_category", "location", "description",
        "atmosphere_tags", "clue", "requires_items", "grants_items",
        "characters_involved", "next_possible_events"
    ]
}

def generate_event(dream_state: dict, event_id: str) -> dict:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=f"""You are the AI Story Director for a dream-continuation game.
Given this Dream State, generate ONE next Event that continues the story.
The event must stay logically connected to the dream's unresolved elements
and known mysteries. Include exactly one clue.

IMPORTANT: The "location" field must be copied EXACTLY from the Dream
State's location_name field below — do not paraphrase, shorten, or
reword it in any way.

event_id to use: {event_id}

Dream State:
{json.dumps(dream_state, indent=2)}""",
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": EVENT_SCHEMA
        }
    )
    return json.loads(interaction.output_text)

if __name__ == "__main__":
    from dream_parser import parse_dream

    dream_state = parse_dream(
        "I was sleeping in my hostel. Suddenly I heard someone crying outside. I opened the door and the corridor was empty.",
        dream_id="dream_0001",
        player_id="player_0001"
    )
    event = generate_event(dream_state, event_id="evt_0001")
    print(json.dumps(event, indent=2))