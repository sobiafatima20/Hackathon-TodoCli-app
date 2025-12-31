---
id: 0002
title: Update Constitution for Python Todo App
stage: constitution
date: 2025-12-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: sobiafatima
command: /sp.constitution
labels: ["constitution", "python", "todoapp", "cli", "spec-driven"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

Project: The Evolution of Todo – Phase I (In-Memory Python Console App)

Core principles:
- Spec-driven development: no code may be written without an approved specification
- Simplicity and clarity suitable for a beginner-friendly CLI application
- Clean code practices with readable, maintainable Python
- Deterministic behavior with in-memory state only (no persistence)

Key standards:
- Each feature must be introduced via a separate specification file
- All functionality must align exactly with the written spec (no extra features)
- Python code must follow PEP 8 conventions
- Clear separation of concerns (task model, task manager, CLI interface)

Constraints:
- Language: Python 3.13+
- Environment management: UV
- Storage: In-memory only (no database, no files)
- Interface: Console / command-line only
- No external frameworks beyond standard library unless explicitly specified

Success criteria:
- All 5 basic features implemented: Add, Delete, Update, View, Mark Complete
- Application runs successfully from the command line
- Task list displays IDs, titles, descriptions, and completion status
- Repository contains constitution file, specs history, src folder, README.md, and CLAUDE.md
- Code strictly reflects the specifications with no undocumented behavior

## Response snapshot

Updated the constitution for the Python console Todo app with principles for spec-driven development, simplicity, clean code, in-memory behavior, and minimal dependencies, bumping version from 1.0.0 to 2.0.0.

## Outcome

- ✅ Impact: Updated constitution to reflect Python console app requirements with major version bump to 2.0.0
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md updated with new Python CLI-focused principles
- 🔁 Next prompts: none
- 🧠 Reflection: Major version bump appropriate for fundamental project direction change from web to CLI Python app

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
