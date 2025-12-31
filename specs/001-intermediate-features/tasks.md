# Implementation Tasks: Intermediate Level – Organization & Usability

**Feature**: Intermediate Level – Organization & Usability
**Branch**: 001-intermediate-features
**Created**: 2025-12-31
**Status**: Ready for Implementation

## Implementation Strategy

This document outlines the implementation tasks for the Intermediate Level features of the CLI Todo application. The approach follows an incremental delivery model with the following phases:
1. Setup and foundational tasks
2. User story implementation in priority order (P1, P2, P3)
3. Polish and cross-cutting concerns

Each user story is designed to be independently testable and deliver value to users.

## Dependencies

- User Story 1 (Priorities) and User Story 2 (Tags) can be implemented in parallel as they modify the same Task model but have independent functionality
- User Stories 3-5 (Search, Filter, Sort) depend on completion of Stories 1-2 as they operate on the extended Task model

## Parallel Execution Examples

- Tasks T005-T008 (Task model extension) can be done in parallel with unit test creation
- Tasks T015-T020 (Service methods) can be implemented in parallel once the Task model is updated
- Tasks T025-T030 (CLI commands) can be implemented in parallel once service methods are available

---

## Phase 1: Setup

**Goal**: Prepare project structure and foundational components

- [ ] T001 Create src/models directory if it doesn't exist
- [ ] T002 Create src/services directory if it doesn't exist
- [ ] T003 Create src/cli directory if it doesn't exist
- [ ] T004 Create tests/unit directory if it doesn't exist
- [ ] T005 Create tests/integration directory if it doesn't exist

---

## Phase 2: Foundational

**Goal**: Implement core Task model with priority and tags support

- [x] T006 [P] Update Task model in src/models/task.py with priority and tags attributes
- [x] T007 [P] Update Task constructor to accept priority and tags parameters with defaults
- [x] T008 [P] Update Task string representation to include priority and tags
- [x] T009 [P] Add validation for priority attribute ("high", "medium", "low")
- [x] T010 [P] Add validation for tags attribute (list of strings)
- [x] T011 [P] [US1] Create unit tests for Task model with priority in tests/unit/test_task.py
- [x] T012 [P] [US2] Create unit tests for Task model with tags in tests/unit/test_task.py
- [x] T013 [P] Update TaskManager to support new Task attributes in src/services/task_manager.py
- [x] T014 [P] Update TaskManager constructor to maintain existing functionality

---

## Phase 3: User Story 1 - Set and View Task Priorities (Priority: P1)

**Goal**: Enable users to assign priority levels (high, medium, low) to tasks and view them clearly

**Independent Test Criteria**: Users can create tasks with different priority levels and view them in the task list, with priority information clearly visible. Default priority is "medium" when not specified.

- [x] T015 [US1] Update add_task method to accept priority parameter in src/services/task_manager.py
- [x] T016 [US1] Update add_task to assign default "medium" priority when not specified in src/services/task_manager.py
- [x] T017 [US1] Update update_task method to handle priority updates in src/services/task_manager.py
- [x] T018 [US1] Update CLI add command to accept --priority flag in src/cli/main.py
- [x] T019 [US1] Update CLI update command to accept --priority flag in src/cli/main.py
- [x] T020 [US1] Update CLI list command to display priority information in src/cli/main.py
- [x] T021 [US1] Create unit tests for priority functionality in tests/unit/test_task_manager.py
- [x] T022 [US1] Create integration tests for priority CLI commands in tests/integration/test_cli.py

---

## Phase 4: User Story 2 - Add and View Task Tags (Priority: P1)

**Goal**: Enable users to add tags to tasks for categorization and view them clearly

**Independent Test Criteria**: Users can create tasks with tags and view them in the task list, with tags clearly visible. Users can add, modify, or remove tags when updating tasks.

- [x] T023 [US2] Update add_task method to accept tags parameter in src/services/task_manager.py
- [x] T024 [US2] Update add_task to assign empty list as default for tags in src/services/task_manager.py
- [x] T025 [US2] Update update_task method to handle tags updates in src/services/task_manager.py
- [x] T026 [US2] Update CLI add command to accept --tags flag in src/cli/main.py
- [x] T027 [US2] Update CLI update command to accept --tags flag in src/cli/main.py
- [x] T028 [US2] Update CLI list command to display tags information in src/cli/main.py
- [x] T029 [US2] Create unit tests for tags functionality in tests/unit/test_task_manager.py
- [x] T030 [US2] Create integration tests for tags CLI commands in tests/integration/test_cli.py

---

## Phase 5: User Story 3 - Search Tasks by Keyword (Priority: P2)

**Goal**: Enable users to search tasks by keyword across title, description, and tags in a case-insensitive manner

**Independent Test Criteria**: Users can search for keywords that appear in task titles, descriptions, or tags and see all matching tasks displayed in the results.

- [x] T031 [US3] Implement search_tasks method in src/services/task_manager.py
- [x] T032 [US3] Add case-insensitive matching for title, description, and tags in search_tasks
- [x] T033 [US3] Create CLI search command in src/cli/main.py
- [x] T034 [US3] Add --keyword parameter to CLI search command in src/cli/main.py
- [x] T035 [US3] Create unit tests for search functionality in tests/unit/test_task_manager.py
- [x] T036 [US3] Create integration tests for search CLI command in tests/integration/test_cli.py
- [x] T037 [US3] Handle edge case: return empty results when no matches found

---

## Phase 6: User Story 4 - Filter Tasks by Status and Priority (Priority: P2)

**Goal**: Enable users to filter tasks by completion status and priority with combinable filters

**Independent Test Criteria**: Users can filter tasks by status, priority, or due date, and can combine multiple filters simultaneously while the underlying task list remains unchanged.

- [x] T038 [US4] Implement filter_tasks method in src/services/task_manager.py
- [x] T039 [US4] Add filtering by completion status in filter_tasks method
- [x] T040 [US4] Add filtering by priority level in filter_tasks method
- [x] T041 [US4] Add filtering by due date in filter_tasks method
- [x] T042 [US4] Support combining multiple filters in filter_tasks method
- [x] T043 [US4] Create CLI filter command in src/cli/main.py
- [x] T044 [US4] Add filter parameters (--status, --priority, --due-date) to CLI filter command
- [x] T045 [US4] Create unit tests for filter functionality in tests/unit/test_task_manager.py
- [x] T046 [US4] Create integration tests for filter CLI command in tests/integration/test_cli.py

---

## Phase 7: User Story 5 - Sort Tasks by Various Criteria (Priority: P3)

**Goal**: Enable users to sort tasks by alphabetical order, priority, or due date with temporary sorting

**Independent Test Criteria**: Users can sort tasks by title, priority, or due date with results displayed in the correct order while maintaining original storage order.

- [x] T047 [US5] Implement sort_tasks method in src/services/task_manager.py
- [x] T048 [US5] Add sorting by title (alphabetical) in sort_tasks method
- [x] T049 [US5] Add sorting by priority (high to low) in sort_tasks method
- [x] T050 [US5] Add sorting by due date (earliest first) in sort_tasks method
- [x] T051 [US5] Ensure sorting is temporary and doesn't modify original storage
- [x] T052 [US5] Create CLI sort command in src/cli/main.py
- [x] T053 [US5] Add sort parameter (--by) to CLI sort command
- [x] T054 [US5] Create unit tests for sort functionality in tests/unit/test_task_manager.py
- [x] T055 [US5] Create integration tests for sort CLI command in tests/integration/test_cli.py

---

## Phase 8: Polish & Cross-Cutting Concerns

**Goal**: Complete implementation with documentation, error handling, and quality assurance

- [x] T056 Update CLI help text to include new commands and flags in src/cli/main.py
- [x] T057 Add error handling for invalid priority values in src/services/task_manager.py
- [x] T058 Add error handling for invalid tag formats in src/services/task_manager.py
- [x] T059 Add performance validation for search operations (under 10 seconds)
- [x] T060 Add performance validation for sort operations (under 2 seconds)
- [x] T061 Update README or documentation with new features
- [x] T062 Run all existing Basic Level tests to ensure no regression
- [x] T063 Perform end-to-end testing of all Intermediate Level features
- [x] T064 Update version or changelog to reflect new features
- [x] T065 Code review and cleanup of all new implementation files