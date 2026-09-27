import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
STORY_FILE = "story_history.json"
DREAM_STATE_FILE = "dream_state.json"

def save_json(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def load_json(filepath, default):
    if os.path.exists(filepath):
        with open(filepath) as f:
            return json.load(f)
    return default

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

def generate_event(dream_state: dict, story_history: list, chosen_action: str, event_id: str) -> dict:
    history_text = "\n".join(
        f"- {e['event_id']}: {e['description']} (clue: {e['clue']})"
        for e in story_history
    ) if story_history else "None yet — this is the first event."

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=f"""You are the AI Story Director for a dream-continuation game set
in Indian folklore. Ground descriptions, objects, and atmosphere in Indian
haveli architecture (courtyards, jharokha balconies, jaali lattice screens,
carved wooden doors) and Indian folklore entities (e.g. Vetal, Churail,
Bhoot/Pret) rather than generic Western horror imagery.

Dream State:
{json.dumps(dream_state, indent=2)}

Story so far:
{history_text}

The player just chose: "{chosen_action}"

Generate the NEXT Event that results from this choice. It must stay
logically connected to everything above, resolve or build on the chosen
action specifically, and not repeat a clue or event already given.

IMPORTANT: The "location" field must be copied EXACTLY from the Dream
State's location_name field, unless the story has clearly moved the
player to a different named location already established in the
story so far.

IMPORTANT: "next_possible_events" must be simple, human-readable action
labels in snake_case (e.g. "follow_footprints", "inspect_door") — never
numeric IDs.

event_id to use: {event_id}""",
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": EVENT_SCHEMA
        }
    )
    return json.loads(interaction.output_text)


if __name__ == "__main__":
    from dream_parser import parse_dream

    story_history = load_json(STORY_FILE, [])
    dream_state = load_json(DREAM_STATE_FILE, None)

    if dream_state is None:
        dream_state = parse_dream(
            "I was sleeping in my hostel. Suddenly I heard someone crying outside. I opened the door and the corridor was empty.",
            dream_id="dream_0001",
            player_id="player_0001"
        )
        save_json(dream_state, DREAM_STATE_FILE)

    event_count = len(story_history) + 1
    chosen_action = None
    valid_choices = None

    if story_history:
        valid_choices = story_history[-1]["next_possible_events"]
        print("Resuming story. Last choices were:", valid_choices)
        chosen_action = input("Pick one (or type 'quit'): ")
        while chosen_action != "quit" and chosen_action not in valid_choices:
            print(f"Invalid choice. Pick one of: {valid_choices}")
            chosen_action = input("Pick one (or type 'quit'): ")
        if chosen_action == "quit":
            exit()

    while True:
        event = generate_event(
            dream_state, story_history, chosen_action,
            event_id=f"evt_{event_count:04d}"
        )
        print(json.dumps(event, indent=2))
        story_history.append(event)
        save_json(story_history, STORY_FILE)
        event_count += 1

        valid_choices = event["next_possible_events"]
        print("\nChoices:", valid_choices)
        chosen_action = input("Pick one (or type 'quit'): ")
        while chosen_action != "quit" and chosen_action not in valid_choices:
            print(f"Invalid choice. Pick one of: {valid_choices}")
            chosen_action = input("Pick one (or type 'quit'): ")
        if chosen_action == "quit":
            break