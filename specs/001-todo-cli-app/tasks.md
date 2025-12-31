---
description: "Task list for The Evolution of Todo – Phase I (In-Memory Python Console Application)"
---

# Tasks: The Evolution of Todo – Phase I (In-Memory Python Console Application)

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 [P] Create src directory structure: src/models/, src/services/, src/cli/
- [X] T003 [P] Create tests directory structure: tests/unit/, tests/integration/
- [X] T004 Initialize Python project with pyproject.toml (no external dependencies)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Create Task data model in src/models/task.py with id, title, description, completed fields
- [X] T006 Create TaskManager service in src/services/task_manager.py with in-memory storage dictionary
- [X] T007 [P] Create command-line interface framework in src/cli/main.py with argparse setup
- [X] T008 Add basic error handling infrastructure across all components
- [X] T009 Implement validation logic for Task creation (title length, description length)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with title and optional description

**Independent Test**: Can be fully tested by running the add command with title and description, then verifying the task appears in the task list with a unique ID and incomplete status.

### Implementation for User Story 1

- [X] T010 [P] [US1] Add Task creation method in src/services/task_manager.py with auto-generated ID
- [X] T011 [US1] Add 'add' command to CLI in src/cli/main.py that accepts title and optional description
- [X] T012 [US1] Implement validation for title (1-200 chars) and description (0-1000 chars) in src/models/task.py
- [X] T013 [US1] Add success message output when task is added: "Task added successfully with ID: {id}"
- [X] T014 [US1] Create unit test for Task creation in tests/unit/test_task.py
- [X] T015 [US1] Create unit test for TaskManager add functionality in tests/unit/test_task_manager.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P2)

**Goal**: Enable users to view all tasks in their todo list with ID, title, description, and completion status

**Independent Test**: Can be fully tested by adding some tasks, then running the view command and verifying that all tasks appear with correct ID, title, description, and completion status.

### Implementation for User Story 2

- [X] T016 [P] [US2] Add method to retrieve all tasks in src/services/task_manager.py
- [X] T017 [US2] Add 'view' command to CLI in src/cli/main.py that displays formatted task list
- [X] T018 [US2] Implement formatted display of tasks (ID, title, description, status) in src/cli/main.py
- [X] T019 [US2] Handle empty task list case with "No tasks found" message
- [X] T020 [US2] Create unit test for viewing all tasks in tests/unit/test_task_manager.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P3)

**Goal**: Enable users to update the completion status of a specific task by providing its ID

**Independent Test**: Can be fully tested by adding a task, marking it complete, then verifying its status has changed when viewing the task list.

### Implementation for User Story 3

- [X] T021 [P] [US3] Add methods to update task completion status in src/services/task_manager.py
- [X] T022 [US3] Add 'complete' command to CLI in src/cli/main.py that accepts task_id
- [X] T023 [US3] Add 'incomplete' command to CLI in src/cli/main.py that accepts task_id
- [X] T024 [US3] Implement ID validation to ensure task exists before updating status
- [X] T025 [US3] Add success messages for completion status updates
- [X] T026 [US3] Create unit test for completion status updates in tests/unit/test_task_manager.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task (Priority: P4)

**Goal**: Enable users to modify the title or description of an existing task by providing its ID

**Independent Test**: Can be fully tested by adding a task, updating its title/description, then verifying the changes appear when viewing the task list.

### Implementation for User Story 4

- [X] T027 [P] [US4] Add method to update task fields in src/services/task_manager.py
- [X] T028 [US4] Add 'update' command to CLI in src/cli/main.py that accepts task_id and optional title/description
- [X] T029 [US4] Implement validation for updated title (1-200 chars) and description (0-1000 chars)
- [X] T030 [US4] Add success message for task updates
- [X] T031 [US4] Create unit test for task updates in tests/unit/test_task_manager.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: Enable users to remove a task from their todo list by providing its ID

**Independent Test**: Can be fully tested by adding a task, deleting it, then verifying it no longer appears in the task list.

### Implementation for User Story 5

- [X] T032 [P] [US5] Add method to delete task in src/services/task_manager.py
- [X] T033 [US5] Add 'delete' command to CLI in src/cli/main.py that accepts task_id
- [X] T034 [US5] Implement ID validation to ensure task exists before deletion
- [X] T035 [US5] Add success message for task deletion
- [X] T036 [US5] Add appropriate error message for invalid task IDs
- [X] T037 [US5] Create unit test for task deletion in tests/unit/test_task_manager.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T038 [P] Add comprehensive error handling for all commands in src/cli/main.py
- [X] T039 Add documentation strings to all methods and classes
- [X] T040 [P] Add integration tests for CLI commands in tests/integration/test_cli.py
- [X] T041 Run quickstart.md validation to ensure all commands work as specified
- [X] T042 Perform code review and ensure PEP 8 compliance
- [X] T043 Update README.md with usage instructions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence