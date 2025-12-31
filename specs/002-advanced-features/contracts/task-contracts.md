# API Contracts: Advanced Level – Intelligent Features

**Date**: 2025-12-31
**Feature**: Advanced Level – Intelligent Features
**Branch**: 002-advanced-features

## Task Model Contracts

### Contract: Task Recurrence and Due Date Fields
**Purpose**: Extend Task model with recurrence and due date functionality
**API**: `Task` model in `src/models/task.py`
**Input**:
- due_date (optional): datetime object or None, defaults to None
- is_recurring (optional): boolean, defaults to False
- recurrence_interval (optional): integer (days), defaults to None
- original_task_id (optional): integer, defaults to None
**Validation**:
- due_date must be a valid datetime object or None
- is_recurring must be a boolean value
- recurrence_interval must be a positive integer if is_recurring is True
- original_task_id must be a valid task ID if specified
**Output**:
- Task object with new recurrence and due date attributes set
- Attributes accessible via `task.due_date`, `task.is_recurring`, etc.
**Side Effects**: None (data modification is part of task creation/update)

## Task Manager Service Contracts

### Contract: Add Task with Recurrence and Due Date
**Purpose**: Add a new task to the todo list with recurrence and due date support
**API**: `add_task` method in `src/services/task_manager.py`
**Input**:
- title (required): String, 1-200 characters
- description (optional): String, 0-1000 characters
- priority (optional): String, one of "high", "medium", "low", defaults to "medium"
- tags (optional): List of strings, defaults to empty list
- due_date (optional): datetime object, defaults to None
- is_recurring (optional): boolean, defaults to False
- recurrence_interval (optional): integer (days), required if is_recurring is True
**Validation**:
- Title must be 1-200 characters
- Priority must be one of allowed values
- Tags must be a list of non-empty strings
- Due date must be a valid datetime object if provided
- Recurrence interval must be positive if task is recurring
**Output**:
- Success: Returns the created `Task` object with all attributes set
- Error: Raises `ValueError` with descriptive message
**Side Effects**: Creates a new task and adds to in-memory storage with unique ID

### Contract: Update Task with Recurrence and Due Date
**Purpose**: Update the title, description, priority, tags, due date, or recurrence settings of an existing task
**API**: `update_task` method in `src/services/task_manager.py`
**Input**:
- task_id (required): Integer, existing task ID
- title (optional): String, 1-200 characters, or `None` to skip
- description (optional): String, 0-1000 characters, or `None` to skip
- priority (optional): String, one of "high", "medium", "low", or `None` to skip
- tags (optional): List of strings, or `None` to skip
- due_date (optional): datetime object or `None` to skip/clear
- is_recurring (optional): boolean or `None` to skip
- recurrence_interval (optional): integer or `None` to skip/clear
**Validation**:
- Task with given ID must exist
- Due date must be a valid datetime object if provided
- Recurrence interval must be positive if task is recurring
**Output**:
- Success: Returns the updated `Task` object with all attributes set
- Error: Returns `None` if task not found, or raises `ValueError` for invalid inputs
**Side Effects**: Updates specified fields of the existing task

### Contract: Handle Recurring Task Completion
**Purpose**: Handle completion of a recurring task by creating a new instance
**API**: `handle_recurring_task_completion` method in `src/services/task_manager.py`
**Input**:
- task_id (required): Integer, ID of the recurring task to complete
**Validation**:
- Task must exist and be marked as recurring
- Task must have a valid recurrence interval
**Output**:
- Success: Returns True if recurring task was handled correctly
- Error: Returns False if task not found or not recurring
**Side Effects**: Marks original task as complete and creates a new instance with updated due date

### Contract: Get Overdue Tasks
**Purpose**: Retrieve all tasks that are past their due date
**API**: `get_overdue_tasks` method in `src/services/task_manager.py`
**Input**: None
**Validation**: None (read-only operation)
**Output**:
- Success: Returns a list of `Task` objects with due dates in the past
- Empty list if no overdue tasks found
**Side Effects**: None (read-only operation)

### Contract: Get Upcoming Tasks
**Purpose**: Retrieve tasks due within a specified number of days
**API**: `get_upcoming_tasks` method in `src/services/task_manager.py`
**Input**:
- days_ahead (required): Integer, number of days to look ahead
**Validation**:
- days_ahead must be a positive integer
**Output**:
- Success: Returns a list of `Task` objects with due dates within the specified range
- Empty list if no upcoming tasks found
**Side Effects**: None (read-only operation)

### Contract: Get Today's Tasks
**Purpose**: Retrieve tasks due today
**API**: `get_todays_tasks` method in `src/services/task_manager.py`
**Input**: None
**Validation**: None (read-only operation)
**Output**:
- Success: Returns a list of `Task` objects with due dates set to today
- Empty list if no tasks due today
**Side Effects**: None (read-only operation)

### Contract: Get Recurring Tasks
**Purpose**: Retrieve all recurring tasks
**API**: `get_recurring_tasks` method in `src/services/task_manager.py`
**Input**: None
**Validation**: None (read-only operation)
**Output**:
- Success: Returns a list of `Task` objects marked as recurring
- Empty list if no recurring tasks found
**Side Effects**: None (read-only operation)

## CLI Command Contracts (Interactive Mode)

### Contract: Add Task Command with Recurrence and Due Date
**Purpose**: Interactive command to add a task with recurrence and due date support
**API**: `handle_add_task` function in `src/cli/main.py`
**Input**:
- Prompts user for: title, description, priority, tags, due date, recurrence settings
- Due date: Date in YYYY-MM-DD format or skip
- Recurrence: Boolean (yes/no) for whether task repeats
- Interval: Number of days between recurrences if recurring
**Validation**:
- Title is required (non-empty after stripping)
- Due date must be in valid format if provided
- Recurrence interval must be positive if task is recurring
**Output**:
- Success: "✓ Task added successfully with ID: {id}" with all details shown
- Error: Appropriate error message with "✗ Error:" prefix
**Side Effects**: Creates new task via TaskManager

### Contract: Update Task Command with Recurrence and Due Date
**Purpose**: Interactive command to update a task including recurrence and due date settings
**API**: `handle_update_task` function in `src/cli/main.py`
**Input**:
- Prompts user for: task ID, new title, new description, new priority, new tags, new due date, new recurrence settings
- Shows current values and allows keeping with Enter
**Validation**:
- Task with given ID must exist
- Due date must be in valid format if provided
- Recurrence interval must be positive if task is recurring
**Output**:
- Success: "✓ Task {id} updated successfully" with all new details shown
- Error: Appropriate error message with "✗ Error:" prefix
**Side Effects**: Updates existing task via TaskManager

### Contract: View Tasks Command with Due Date and Recurrence Info
**Purpose**: Display all tasks with due date and recurrence information
**API**: `handle_view_tasks` function in `src/cli/main.py`
**Input**: None
**Validation**: None
**Output**:
- Success: Formatted table with ID, Status, Priority, Title, Due Date, Recurrence, Tags, Description columns
- Priority shown as single letter (H/M/L)
- Due date shown in YYYY-MM-DD format or blank
- Recurrence shown as "Yes" or blank
- Shows total task count
- Empty state: "No tasks found."
**Side Effects**: None (read-only operation)

### Contract: Recurring Tasks Command
**Purpose**: Interactive command to manage recurring tasks
**API**: New function in `src/cli/main.py`
**Input**:
- Prompts user for options: list all recurring tasks, modify specific task, change interval
**Validation**:
- Task ID must be valid if modifying specific task
- Interval must be positive if changing recurrence interval
**Output**:
- Success: Appropriate output based on selected action
- Error: Appropriate error message with "✗ Error:" prefix
**Side Effects**: Updates task recurrence settings via TaskManager

### Contract: Reminders Command
**Purpose**: Interactive command to view overdue and upcoming tasks
**API**: New function in `src/cli/main.py`
**Input**:
- Prompts user for options: view overdue tasks, view upcoming tasks, specify days ahead
**Validation**:
- Days ahead must be positive if specified
**Output**:
- Success: Formatted list of overdue or upcoming tasks based on selection
- Error: Appropriate error message with "✗ Error:" prefix
**Side Effects**: None (read-only operation)