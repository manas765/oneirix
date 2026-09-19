import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

DREAM_STATE_SCHEMA = {
    "type": "object",
    "properties": {
        "dream_id": {"type": "string"},
        "player_id": {"type": "string"},
        "raw_input": {"type": "string"},
        "setting_category": {
            "type": "string",
            "enum": ["indoor", "institutional", "outdoor", "urban", "transit", "abstract"]
        },
        "location_name": {"type": "string"},
        "scale": {"type": "string"},
        "time_of_day": {"type": "string"},
        "characters": {"type": "array", "items": {"type": "string"}},
        "objects": {"type": "array", "items": {"type": "string"}},
        "events": {"type": "array", "items": {"type": "string"}},
        "atmosphere": {"type": "array", "items": {"type": "string"}},
        "final_moment": {"type": "string"},
        "unresolved_elements": {"type": "array", "items": {"type": "string"}},
        "known_mysteries": {"type": "array", "items": {"type": "string"}}
    },
    "required": [
        "dream_id", "player_id", "raw_input", "setting_category",
        "location_name", "scale", "time_of_day", "characters",
        "objects", "events", "atmosphere", "final_moment",
        "unresolved_elements", "known_mysteries"
    ]
}

def parse_dream(dream_text: str, dream_id: str, player_id: str) -> dict:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=f"""You are a dream parser. Extract structured information from this dream description.
Identify the exact final moment the dreamer remembers before waking up.
Flag any unresolved elements (things mentioned but never explained) and any
mysteries the dream implies but doesn't resolve.

raw_input to use verbatim: {dream_text}
dream_id to use: {dream_id}
player_id to use: {player_id}

Dream: {dream_text}""",
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": DREAM_STATE_SCHEMA
        }
    )
    return json.loads(interaction.output_text)

if __name__ == "__main__":
    test_dream = "I was sleeping in my hostel. Suddenly I heard someone crying outside. I opened the door and the corridor was empty."
    result = parse_dream(test_dream, dream_id="dream_0001", player_id="player_0001")
    print(json.dumps(result, indent=2))