# ONEIRIX — AI CONTINUATION OF UNFINISHED DREAMS

## 1. Project Identity

**Project Name:** ONEIRIX  
**Category:** AI-powered 3D interactive narrative / dream-continuation game  
**Core Concept:** Continue an unfinished dream as an interactive 3D story.

### Tagline
> I dreamt it. I woke up. ONEIRIX tells me what happened next.

---

# 2. Core Concept

ONEIRIX is a 3D AI-powered narrative game where a user describes an unfinished dream they experienced in real life.

The user does NOT need to write a complete storyline.

They provide only the dream they remember, including the point where they woke up.

ONEIRIX identifies the final known moment of the dream, reconstructs the setting as a 3D environment, and begins the interactive game from that exact point.

From there, an AI Story Engine autonomously continues the narrative.

The continuation is not restricted to one genre. The AI may evolve the story into:

- Mystery
- Thriller
- Horror
- Crime investigation
- Adventure
- Science fiction
- Alien encounters
- Cosmic / astronomical exploration
- Time travel
- Alternate realities
- Simulation / Matrix-like worlds
- Fantasy
- Psychological mystery
- Cyberpunk
- Surreal dream worlds
- Or a completely new combination

The player controls a 3D character and actively explores, investigates, interacts, solves riddles, discovers clues, and makes decisions.

The AI remembers the evolving story and generates future events based on what has already happened.

---

# 3. Example

### User's real dream

> "I was sleeping peacefully in my hostel. Suddenly I heard someone crying outside. I ignored it for a while, but eventually got up to check. When I opened the door, nobody was there. Then I woke up."

The dream ends.

ONEIRIX takes over from here.

### Game begins

The player appears in a 3D version of the hostel room.

The player opens the door.

The corridor is empty.

This is the exact point where the original dream ended.

The AI now decides the continuation.

It might create:

- Another occurrence of the crying
- A strange clue
- An unexplained room
- A mysterious character
- A crime mystery
- A reality distortion
- An alien signal
- A portal to another world
- A time anomaly
- A completely unexpected storyline

The user does not know what comes next.

---

# 4. Fundamental Design Principle

## The dream is the seed, not the story.

The user supplies:

**Dream → AI continuation → Interactive 3D experience**

The AI supplies:

**Mystery + Story + World + Characters + Events + Puzzles + Continuation**

The player supplies:

**Exploration + Decisions + Actions**

Together:

```text
REAL UNFINISHED DREAM
        ↓
DREAM PARSING
        ↓
DREAM STATE
        ↓
AI STORY ENGINE
        ↓
3D WORLD GENERATION
        ↓
PLAYER EXPLORATION
        ↓
PLAYER ACTIONS
        ↓
AI REASONING
        ↓
NEW STORY EVENT
        ↓
STORY MEMORY
        ↓
CONTINUATION
        ↺
```

---

# 5. Problem Statement

Dreams often contain incomplete narratives that end abruptly when a person wakes up.

There is no interactive system that allows a user to take an unfinished dream and transform it into a persistent 3D experience where AI continues the narrative dynamically from the exact point where the dream ended.

Traditional games provide developer-created stories and fixed worlds.

Traditional AI story generators primarily produce text.

Traditional VR experiences generally provide pre-designed environments.

ONEIRIX aims to combine these into a single system:

> An AI that takes an unfinished dream as input, reconstructs its context into an interactive 3D world, and autonomously continues the narrative while adapting to player actions.

---

# 6. Main Objectives

1. Accept unfinished dreams as natural-language or voice input.
2. Identify the final point of the dream.
3. Extract characters, locations, objects, events, atmosphere, and unresolved elements.
4. Convert the dream into a structured Dream State.
5. Reconstruct the starting environment in 3D.
6. Continue the story using an AI Story Engine.
7. Allow the AI to dynamically select or combine genres.
8. Provide a controllable 3D player character.
9. Allow exploration and interaction.
10. Generate mysteries, clues, riddles, and adventures.
11. Maintain story continuity.
12. Remember important previous events.
13. Allow player decisions to influence future events.
14. Generate new worlds and environments as the story expands.
15. Allow the player to continue the dream across multiple sessions.
16. Provide a persistent Dream Journal and Mystery Board.

---

# 7. Complete Feature Set

## A. Dream Input System

### 1. Natural Language Dream Input
The user can describe the dream in normal language.

### 2. Voice Dream Input
The user can narrate the dream instead of typing it.

### 3. Dream Segmentation
AI identifies:
- Beginning
- Events
- Characters
- Locations
- Objects
- Actions
- Final moment

### 4. Unfinished Point Detection
AI determines exactly where the dream stopped.

### 5. Dream Atmosphere Extraction
AI identifies the remembered mood and environment, such as:
- Calm
- Strange
- Mysterious
- Dark
- Exciting
- Surreal

The system should use this only as narrative context, not as a psychological diagnosis.

---

# B. Dream Reconstruction

### 6. Dream State Representation

```text
DREAM STATE
├── Location
├── Time
├── Characters
├── Objects
├── Events
├── Environment
├── Atmosphere
├── Player State
├── Known Mysteries
└── Unresolved Elements
```

### 7. 3D Environment Reconstruction
Convert important dream settings into explorable environments.

### 8. Reality-to-Dream Transformation
Start close to the remembered dream and gradually allow the AI to transform the world.

### 9. Dynamic Environment Generation
New environments can appear as the story progresses.

### 10. Procedural / AI-Assisted World Expansion
Generate additional locations without requiring every possible location to be manually built.

---

# C. AI Story Engine

### 11. AI Dream Continuation
The AI continues the story from the unfinished point.

### 12. Genre Selection Engine
AI may choose any suitable narrative direction.

Possible genres:
- Mystery
- Thriller
- Horror
- Crime
- Adventure
- Sci-fi
- Cosmic
- Alien
- Fantasy
- Time travel
- Simulation
- Alternate reality
- Cyberpunk
- Surreal

### 13. Genre Fusion
The AI can combine genres.

Example:

```text
Mystery
   ↓
Thriller
   ↓
Reality Anomaly
   ↓
Science Fiction
   ↓
Cosmic Adventure
```

### 14. Dynamic Plot Generation
AI creates new plot events while maintaining continuity.

### 15. Story Arc Generation
AI maintains:
- Introduction
- Rising mystery
- Investigation
- Major discovery
- Escalation
- Revelation
- Continuation

### 16. Hidden Story Planning
The AI can maintain information that the player has not discovered yet.

### 17. Dynamic Story Continuation
The next event is generated after the player's meaningful actions.

---

# D. Mystery & Riddle System

### 18. Mystery Engine
AI generates central and secondary mysteries.

### 19. Riddle Generator
AI creates contextual riddles rather than generic puzzles.

### 20. Clue Generation
Clues can appear through:
- Objects
- Dialogues
- Locations
- Sounds
- Documents
- Environmental details
- Symbols

### 21. Recurring Symbols
Objects or symbols can return later.

Examples:
- Black door
- Clock
- Mirror
- Radio
- Key
- Strange photograph

### 22. Hidden Connections
AI can connect events or objects from different parts of the story.

### 23. Unresolved Mysteries
Some mysteries can remain unanswered for several chapters.

### 24. Mystery Chains

```text
CLUE
 ↓
DISCOVERY
 ↓
NEW MYSTERY
 ↓
NEW CLUE
 ↓
REVELATION
 ↓
LARGER MYSTERY
```

### 25. Mystery Board

The player can visually connect:

```text
CHARACTER
   │
   ├── OBJECT
   │      │
   │      └── LOCATION
   │
   └── EVENT
```

---

# E. 3D Gameplay

### 26. Player Character

The player controls a 3D character.

### 27. Camera / Cursor Control
Mouse controls camera direction in desktop mode.

### 28. Movement

- W/A/S/D movement
- Walk
- Run
- Jump

### 29. Interaction

- Open doors
- Pick up objects
- Inspect objects
- Activate mechanisms
- Read clues
- Interact with environments

### 30. Investigation Mode
Objects can be inspected for hidden clues.

### 31. Exploration
The player can freely explore available environments.

### 32. Environmental Interaction
The world reacts to the player's actions.

### 33. Collectable Clues / Items
Important items can be stored in the player's inventory.

### 34. Player Decisions
The player can make meaningful choices through actual gameplay.

---

# F. AI Characters

### 35. AI-Generated Characters
AI can create characters dynamically.

### 36. Character Personality
Characters can have:
- Personality
- Goals
- Knowledge
- Secrets
- Relationships

### 37. Dynamic Dialogue
Characters respond contextually.

### 38. Character Memory
Important characters can remember relevant player interactions.

### 39. Mysterious Characters
AI can introduce unknown or unexplained characters.

### 40. Character Transformation
Characters can change roles or appearances as the dream evolves.

---

# G. Dream Exploration

### 41. Hidden Dream Paths
Secret routes can be discovered through exploration.

### 42. Unlockable Dream Worlds
New environments can become accessible.

### 43. Surreal Environmental Puzzles
Dream-like puzzles can use:
- Impossible architecture
- Time loops
- Reflections
- Sound
- Spatial changes
- Object transformations

### 44. Dream Secrets
Rare events can appear unexpectedly.

### 45. Easter Eggs
The AI can generate unusual optional discoveries.

### 46. Rare Dream Events
Low-frequency events can surprise the player.

### 47. Dream Butterfly Effect
Small player actions can influence later events.

---

# H. Persistent Story System

### 48. Story Memory
AI remembers important story events.

### 49. Dream Memory
Previous dreams can influence future sessions.

### 50. Chapter System
A long-running dream story can be divided into chapters.

### 51. Story Branching
Different player decisions can create different paths.

### 52. Branch Reconnection
Different paths may eventually converge while retaining consequences.

### 53. Multi-Session Continuation
Players can leave and return later.

### 54. Dream Replay
Replay previous experiences.

### 55. Regenerated Replay
Replay the same starting context with a different AI continuation.

### 56. Continue Previous Dream
Resume from where the previous game session ended.

---

# I. Dream Journal & Discovery

### 57. Dream Journal

Stores:
- Dreams
- Chapters
- Locations
- Characters
- Symbols
- Mysteries
- Clues
- Decisions

### 58. Dream Map
Visual map of discovered worlds.

### 59. Dream Timeline
Chronological history of the story.

### 60. Discovery Tracker
Tracks:
- Discovered locations
- Symbols
- Characters
- Mysteries
- Hidden paths

### 61. Unresolved Mystery Tracker
Shows mysteries that remain unsolved without revealing their answers.

### 62. Dream Universe Graph
Visual representation of connections between dreams, locations, characters, objects, and events.

---

# J. Advanced AI Features

### 63. AI Director

The AI acts as the invisible director of the experience.

It decides:
- What happens next
- When a clue appears
- When a mystery escalates
- When the environment changes
- When a character appears
- When a new world is introduced

### 64. Context-Based Discovery Engine
AI creates connections based on what has already happened in the current and previous dreams.

### 65. Adaptive Difficulty
Puzzle complexity can adapt to the player's progress.

### 66. Adaptive Story Pacing
The AI can slow down exploration or increase narrative intensity.

### 67. Controlled Randomness
The story contains unexpected events while preserving narrative coherence.

### 68. AI World Rule Generation
Different dream worlds can have different rules.

Example:

```text
WORLD A:
Normal gravity

WORLD B:
Gravity changes every few minutes

WORLD C:
Time moves backward

WORLD D:
Doors lead to unexpected locations
```

### 69. Reality Consistency Manager
AI maintains internal rules so that the generated story does not become completely incoherent.

### 70. Story State Validation
Before generating major events, the system checks:
- Previous events
- Known clues
- Character states
- Current location
- Player inventory
- Unresolved mysteries

---

# K. Optional Future Features

### 71. VR Mode
Support VR headsets after the desktop prototype is stable.

### 72. Shared Dream
Multiple players could eventually enter a common generated dream.

### 73. Dream-to-Dream Linking
Different real dreams can potentially become connected.

### 74. User-Created Dream Worlds
Advanced users can define custom rules, characters, and objects.

### 75. Dream Universe Expansion
The system can continue expanding a user's story over many sessions.

---

# 8. Core Gameplay Loop

```text
USER DESCRIBES DREAM
        ↓
AI IDENTIFIES LAST MOMENT
        ↓
3D WORLD RECREATES THAT MOMENT
        ↓
PLAYER ENTERS THE DREAM
        ↓
EXPLORE
        ↓
INVESTIGATE
        ↓
DISCOVER CLUE
        ↓
SOLVE RIDDLE
        ↓
MAKE DECISION
        ↓
AI ANALYZES PLAYER ACTION
        ↓
AI GENERATES NEXT EVENT
        ↓
WORLD TRANSFORMS
        ↓
NEW MYSTERY
        ↓
NEW LOCATION
        ↓
STORY CONTINUES
        ↺
```

---

# 9. AI Story Continuation Architecture

```text
                    USER DREAM
                        │
                        ▼
               DREAM INPUT LAYER
                        │
                        ▼
                DREAM PARSER
                        │
                        ▼
                 DREAM STATE
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
      LOCATIONS      CHARACTERS     EVENTS
          │             │             │
          └─────────────┼─────────────┘
                        ▼
               STORY KNOWLEDGE GRAPH
                        │
                        ▼
                 AI STORY DIRECTOR
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       PLOT          GENRE          WORLD
     ENGINE         ENGINE         ENGINE
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                EVENT GENERATOR
                        │
                        ▼
                  3D GAME ENGINE
                        │
                        ▼
                    PLAYER
                        │
                 ACTION / CHOICE
                        │
                        ▼
                  STORY MEMORY
                        │
                        └───────────→ AI DIRECTOR
```

---

# 10. Important AI Design Rule

ONEIRIX should NOT use pure randomness.

Instead:

```text
                 POSSIBLE FUTURES
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      HORROR         SCI-FI        MYSTERY
        │              │              │
        ▼              ▼              ▼
      CRIME          COSMIC        FANTASY
        │              │              │
        └──────────────┼──────────────┘
                       ▼
              AI STORY EVALUATION
                       │
                       ▼
               BEST-FIT DIRECTION
                       │
                       ▼
                  NEW EVENT
```

The AI can surprise the player, but the continuation should remain connected to the existing story.

**Goal: unpredictable but coherent.**

---

# 11. Example Story Progression

### Original Dream

Hostel → Crying → Door → Empty Corridor → Wake up

### ONEIRIX

```text
CHAPTER 1
THE EMPTY CORRIDOR
       ↓
CHAPTER 2
THE SOUND RETURNS
       ↓
CHAPTER 3
THE ROOM THAT DOESN'T EXIST
       ↓
CHAPTER 4
THE UNKNOWN MESSAGE
       ↓
CHAPTER 5
REALITY BREAK
       ↓
CHAPTER 6
THE OTHER SIDE
       ↓
CHAPTER 7
COSMIC / SCI-FI EXPANSION
       ↓
AI-GENERATED CONTINUATION
```

This is only an example. The actual AI should generate a different continuation depending on the dream and player actions.

---

# 12. The Player Experience

The intended emotional progression is:

```text
CURIOUS
   ↓
CONFUSED
   ↓
SUSPICIOUS
   ↓
INVESTIGATING
   ↓
DISCOVERING
   ↓
SURPRISED
   ↓
EXPLORING
   ↓
UNDERSTANDING
   ↓
NEW MYSTERY
   ↓
CURIOUS AGAIN
```

The player should constantly wonder:

- What is happening?
- Why am I here?
- What does this object mean?
- Who is this character?
- Why did this location change?
- What is the connection?
- What happens if I go there?
- What will the AI generate next?

---

# 13. What Makes ONEIRIX Different

### Traditional Game

Developer → Story → Levels → Player

### AI Story Game

Developer → AI → Story → Player

### ONEIRIX

```text
REAL DREAM
    ↓
AI
    ↓
3D WORLD
    ↓
PLAYER
    ↓
PLAYER ACTIONS
    ↓
AI
    ↓
NEW STORY
    ↓
NEW WORLD
    ↓
PLAYER
    ↺
```

The key difference is that the **starting narrative originates from a real unfinished dream**, while the continuation is dynamically generated.

---

# 14. Recommended MVP

Do NOT attempt all 75 features immediately.

The first working version should prove the central concept.

## MVP Features

1. Dream text input
2. Dream parsing
3. Last-moment detection
4. Dream State generation
5. One 3D environment
6. Third-person or first-person character
7. Walk
8. Run
9. Jump
10. Camera/mouse control
11. Basic interaction
12. AI story continuation
13. AI-generated mystery
14. AI-generated clues
15. AI-generated riddles
16. One dynamic story branch
17. AI character dialogue
18. Story memory
19. Dream Journal
20. Save/resume

### MVP Demonstration

```text
USER ENTERS DREAM
        ↓
AI PARSES DREAM
        ↓
AI FINDS ENDING
        ↓
3D HOSTEL CREATED
        ↓
PLAYER APPEARS
        ↓
PLAYER OPENS DOOR
        ↓
AI CONTINUES STORY
        ↓
MYSTERY APPEARS
        ↓
PLAYER INVESTIGATES
        ↓
CLUE FOUND
        ↓
RIDDLE
        ↓
PLAYER SOLVES IT
        ↓
NEW AREA OPENS
        ↓
STORY CONTINUES
```

---

# 15. Long-Term Vision

ONEIRIX eventually becomes a persistent **AI-generated Dream Universe**.

Every unfinished dream can become the beginning of a new interactive story.

```text
REAL DREAM #1
      ↓
STORY A
      ↓
DREAM UNIVERSE A

REAL DREAM #2
      ↓
STORY B
      ↓
DREAM UNIVERSE B

         ↓
   AI DISCOVERS POSSIBLE
   CONNECTIONS

         ↓

PERSISTENT PERSONAL
DREAM UNIVERSE
```

The player can return weeks later and continue the same narrative.

---

# 16. One-Line Definition

> **ONEIRIX is a 3D AI-powered interactive game that takes an unfinished real dream and continues it from the exact point where the player woke up, dynamically generating an unpredictable but coherent story that can evolve into mystery, thriller, horror, crime, adventure, science fiction, cosmic exploration, aliens, alternate realities, or entirely new genres.**

---

# 17. Core Philosophy

> **The user provides the beginning.**
>
> **AI creates what happens next.**
>
> **The player decides what to do.**
>
> **The AI remembers.**
>
> **The dream evolves.**

---

# 18. Development Direction

Recommended initial technology exploration:

### 3D Engine
- Unity OR Unreal Engine

### AI Layer
- LLM for narrative reasoning
- Structured JSON story state
- Story memory
- Retrieval / knowledge graph

### Backend
- Python / FastAPI or Node.js
- Database for dream/story state

### AI Pipeline

```text
Dream Text
   ↓
LLM
   ↓
Structured Dream State
   ↓
Story State
   ↓
AI Director
   ↓
Event JSON
   ↓
Game Engine
   ↓
3D Event
```

The AI should output structured game events rather than directly controlling the entire game.

Example conceptual event:

```json
{
  "event_type": "mystery_trigger",
  "location": "hostel_corridor",
  "description": "A distant sound is heard again.",
  "clue": "wet_footprints",
  "next_possible_events": [
    "follow_footprints",
    "return_to_room",
    "inspect_door"
  ]
}
```

The game engine interprets these events and performs the actual gameplay.

---

# 19. Core Success Criterion

ONEIRIX succeeds if a user can say:

> **“I had this strange unfinished dream last night…”**

enter it into the system,

walk into a 3D recreation of the dream,

reach the exact point where they woke up,

and then think:

> **“Wait... what happens next?”**

and ONEIRIX gives them an interactive answer.

---

## FINAL PROJECT VISION

**ONEIRIX is not simply a horror game.**

**It is not simply a VR application.**

**It is not simply an AI story generator.**

It is a **Dream Continuation Engine + AI Narrative Director + 3D Interactive Game**.

The dream provides the seed.

AI writes the continuation.

The player explores it.

The player's actions change it.

The AI remembers it.

And the story keeps evolving.
