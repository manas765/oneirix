import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

DREAM_STATE_SCHEMA = {
    "type": "object",
    "properties": {
        "location": {"type": "string"},
        "setting_category": {
            "type": "string",
            "enum": ["Indoor", "Institutional", "Outdoor", "Urban", "Transit", "Abstract"]
        },
        "characters": {"type": "array", "items": {"type": "string"}},
        "objects": {"type": "array", "items": {"type": "string"}},
        "atmosphere": {"type": "string"},
        "last_moment": {"type": "string"}
    },
    "required": ["location", "setting_category", "characters", "objects", "atmosphere", "last_moment"]
}

def parse_dream(dream_text: str) -> dict:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=f"""You are a dream parser. Extract structured information from this dream description.
Identify the exact last moment the dreamer remembers before waking up.

Dream: {dream_text}""",
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": DREAM_STATE_SCHEMA
        }
    )
    return interaction.output_text

if __name__ == "__main__":
    test_dream = "I was walking through my old school hallway at night, and the lights kept flickering. I saw a door at the end that I'd never noticed before. I opened it and there was just darkness. Then I woke up."
    result = parse_dream(test_dream)
    print(result)