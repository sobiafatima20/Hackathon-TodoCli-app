# API Contracts: Intermediate Level – Organization & Usability

**Date**: 2025-12-31
**Feature**: Intermediate Level – Organization & Usability
**Branch**: 001-intermediate-features

## Task Model Contracts

### Contract: Task Priority
**Purpose**: Enable users to assign priority levels (high, medium, low) to tasks and view them clearly
**API**: `Task` model in `src/models/task.py`
**Input**:
- priority (optional): String, one of "high", "medium", "low"
- Default: "medium" when not specified
**Validation**:
- Must be one of the allowed values: "high", "medium", "low"
- Case-sensitive validation
- Raises `ValueError` for invalid priority values
**Output**:
- Task object with priority attribute set
- Priority accessible via `task.priority`
**Side Effects**: None (data modification is part of task creation/update)

### Contract: Task Tags
**Purpose**: Enable users to add tags to tasks for categorization and view them clearly
**API**: `Task` model in `src/models/task.py`
**Input**:
- tags (optional): List of strings, each tag must be non-empty
- Default: Empty list `[]` when not specified
**Validation**:
- Must be a list of strings
- Each tag string must be non-empty after stripping whitespace
- Empty tags are filtered out
- Raises `ValueError` for invalid tag formats
**Output**:
- Task object with tags attribute set as a list of strings
- Tags accessible via `task.tags`
**Side Effects**: None (data modification is part of task creation/update)

## Task Manager Service Contracts

### Contract: Add Task with Priority and Tags
**Purpose**: Add a new task to the todo list with priority and tags support
**API**: `add_task` method in `src/services/task_manager.py`
**Input**:
- title (required): String, 1-200 characters
- description (optional): String, 0-1000 characters
- priority (optional): String, one of "high", "medium", "low", defaults to "medium"
- tags (optional): List of strings, defaults to empty list
**Validation**:
- Title must be 1-200 characters
- Priority must be one of allowed values
- Tags must be a list of non-empty strings
**Output**:
- Success: Returns the created `Task` object with all attributes set
- Error: Raises `ValueError` with descriptive message
**Side Effects**: Creates a new task and adds to in-memory storage with unique ID

### Contract: Update Task with Priority and Tags
**Purpose**: Update the title, description, priority, or tags of an existing task
**API**: `update_task` method in `src/services/task_manager.py`
**Input**:
- task_id (required): Integer, existing task ID
- title (optional): String, 1-200 characters, or `None` to skip
- description (optional): String, 0-1000 characters, or `None` to skip
- priority (optional): String, one of "high", "medium", "low", or `None` to skip
- tags (optional): List of strings, or `None` to skip
**Validation**:
- Task with given ID must exist
- Priority must be one of allowed values (if provided)
- Tags must be a list of non-empty strings (if provided)
**Output**:
- Success: Returns the updated `Task` object with all attributes set
- Error: Returns `None` if task not found, or raises `ValueError` for invalid inputs
**Side Effects**: Updates specified fields of the existing task

### Contract: Search Tasks by Keyword
**Purpose**: Enable users to search tasks by keyword across title, description, and tags in a case-insensitive manner
**API**: `search_tasks` method in `src/services/task_manager.py`
**Input**:
- keyword (required): String, the search term to match
**Validation**:
- Keyword must be a non-empty string after stripping whitespace
**Output**:
- Success: Returns a list of `Task` objects that match the keyword
- Case-insensitive matching across title, description, and tags
- Empty list if no matches found
- Error: Raises `ValueError` for empty keyword
**Side Effects**: None (read-only operation)

### Contract: Filter Tasks by Criteria
**Purpose**: Enable users to filter tasks by completion status and priority with combinable filters
**API**: `filter_tasks` method in `src/services/task_manager.py`
**Input**:
- status (optional): Boolean (True for complete, False for incomplete) or `None` to skip
- priority (optional): String, one of "high", "medium", "low" or `None` to skip
- due_date (optional): Date object or `None` to skip (not yet implemented)
**Validation**:
- Priority must be one of allowed values (if provided)
**Output**:
- Success: Returns a list of `Task` objects that match all specified criteria
- Empty list if no matches found
- Returns all tasks if no filters specified
**Side Effects**: None (read-only operation)

### Contract: Sort Tasks by Criteria
**Purpose**: Enable users to sort tasks by various criteria (title, priority, due date) with temporary sorting
**API**: `sort_tasks` method in `src/services/task_manager.py`
**Input**:
- sort_by (required): String, one of "title", "priority", "due_date"
**Validation**:
- sort_by must be one of the allowed values
**Output**:
- Success: Returns a sorted list of `Task` objects based on the specified criteria
- Title: alphabetical order (A-Z)
- Priority: high, medium, low order
- Due date: earliest first (not yet implemented)
- Error: Raises `ValueError` for invalid sort_by value
**Side Effects**: None (read-only operation, original storage order unchanged)

## CLI Command Contracts (Interactive Mode)

### Contract: Add Task Command with Priority and Tags
**Purpose**: Interactive command to add a task with priority and tags support
**API**: `handle_add_task` function in `src/cli/main.py`
**Input**:
- Prompts user for: title, description, priority, tags
- Priority: high/medium/low, defaults to "medium"
- Tags: comma-separated string, converted to list of strings
**Validation**:
- Title is required (non-empty after stripping)
- Priority must be one of allowed values
- Tags are validated as non-empty strings after splitting
**Output**:
- Success: "✓ Task added successfully with ID: {id}" with priority and tags shown
- Error: Appropriate error message with "✗ Error:" prefix
**Side Effects**: Creates new task via TaskManager

### Contract: Update Task Command with Priority and Tags
**Purpose**: Interactive command to update a task including priority and tags
**API**: `handle_update_task` function in `src/cli/main.py`
**Input**:
- Prompts user for: task ID, new title, new description, new priority, new tags
- Shows current values and allows keeping with Enter
**Validation**:
- Task with given ID must exist
- Priority must be one of allowed values (if provided)
- Tags must be valid list of non-empty strings (if provided)
**Output**:
- Success: "✓ Task {id} updated successfully" with new priority and tags shown
- Error: Appropriate error message with "✗ Error:" prefix
**Side Effects**: Updates existing task via TaskManager

### Contract: View Tasks Command with Priority and Tags
**Purpose**: Display all tasks with priority and tags information
**API**: `handle_view_tasks` function in `src/cli/main.py`
**Input**: None
**Validation**: None
**Output**:
- Success: Formatted table with ID, Status, Priority, Title, Tags, Description columns
- Priority shown as single letter (H/M/L)
- Tags shown comma-separated (first 2 if more than 2)
- Shows total task count
- Empty state: "No tasks found."
**Side Effects**: None (read-only operation)

### Contract: Search Tasks Command
**Purpose**: Interactive command to search tasks by keyword
**API**: `handle_search_tasks` function in `src/cli/main.py`
**Input**:
- Prompts user for keyword to search
**Validation**:
- Keyword must be non-empty
**Output**:
- Success: Formatted table of matching tasks with same columns as view
- Shows count of matching tasks
- Empty state: "No tasks found containing '{keyword}'."
**Side Effects**: None (read-only operation)

### Contract: Filter Tasks Command
**Purpose**: Interactive command to filter tasks by various criteria
**API**: `handle_filter_tasks` function in `src/cli/main.py`
**Input**:
- Prompts user for status filter (complete/incomplete) and priority filter
**Validation**:
- Priority must be one of allowed values if provided
- Status must be valid selection
**Output**:
- Success: Formatted table of filtered tasks with same columns as view
- Shows count of matching tasks
- Empty state: "No tasks match the filter criteria."
**Side Effects**: None (read-only operation)

### Contract: Sort Tasks Command
**Purpose**: Interactive command to sort tasks by various criteria
**API**: `handle_sort_tasks` function in `src/cli/main.py`
**Input**:
- Prompts user for sort option (by title, priority, or due date)
**Validation**:
- Sort option must be valid selection (1-3)
**Output**:
- Success: Formatted table of sorted tasks with same columns as view
- Shows current sort criteria
- Empty state: "No tasks to display."
**Side Effects**: None (read-only operation, original storage unchanged)