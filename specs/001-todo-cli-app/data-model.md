# Data Model: The Evolution of Todo – Phase I (In-Memory Python Console Application)

**Date**: 2025-12-28
**Feature**: The Evolution of Todo – Phase I (In-Memory Python Console Application)
**Branch**: 001-todo-cli-app

## Entity: Task

### Fields

- **id**: Integer (unique identifier, auto-generated)
  - Auto-incremented for each new task
  - Used as primary key for lookups
  - Never changes once assigned

- **title**: String (required)
  - Required field when creating a task
  - Minimum length: 1 character
  - Maximum length: 200 characters

- **description**: String (optional)
  - Optional field when creating a task
  - Can be empty or None
  - Maximum length: 1000 characters

- **completed**: Boolean
  - Default value: False
  - Indicates whether the task is complete (True) or incomplete (False)
  - Can be toggled between states

### Validation Rules

- Title must be provided and not empty
- Title length must be between 1 and 200 characters
- Description length must not exceed 1000 characters if provided
- ID must be unique within the application session
- ID must be a positive integer

### State Transitions

- **Initial State**: completed = False (default when task is created)
- **Transition 1**: completed = False → completed = True (when task is marked complete)
- **Transition 2**: completed = True → completed = False (when task is marked incomplete)

### Relationships

- None (standalone entity with no relationships to other entities)

## In-Memory Storage Structure

Tasks will be stored in a Python dictionary where:
- Key: task ID (integer)
- Value: Task object instance

This provides O(1) lookup time for operations based on task ID.