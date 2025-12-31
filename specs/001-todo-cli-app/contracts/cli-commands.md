# API Contracts: The Evolution of Todo – Phase I (In-Memory Python Console Application)

**Date**: 2025-12-28
**Feature**: The Evolution of Todo – Phase I (In-Memory Python Console Application)
**Branch**: 001-todo-cli-app

## CLI Command Contracts

### Command: `add`
**Purpose**: Add a new task to the todo list
**Syntax**: `python main.py add --title "Task Title" [--description "Task Description"]`
**Alternative Syntax**: `python main.py add "Task Title" ["Task Description"]`
**Input**:
- title (required): String, 1-200 characters
- description (optional): String, 0-1000 characters
**Output**:
- Success: "Task added successfully with ID: {id}"
- Error: Appropriate error message
**Side Effects**: Creates a new task with completed=False, adds to in-memory storage

### Command: `view`
**Purpose**: Display all tasks in the todo list
**Syntax**: `python main.py view`
**Input**: None
**Output**:
- Success: Formatted table/list of all tasks with ID, title, description, and completion status
- Empty state: "No tasks found"
**Side Effects**: None (read-only operation)

### Command: `complete`
**Purpose**: Mark a specific task as complete
**Syntax**: `python main.py complete <task_id>`
**Input**:
- task_id (required): Integer, existing task ID
**Output**:
- Success: "Task {id} marked as complete"
- Error: Appropriate error message
**Side Effects**: Updates task's completed status to True

### Command: `incomplete`
**Purpose**: Mark a specific task as incomplete
**Syntax**: `python main.py incomplete <task_id>`
**Input**:
- task_id (required): Integer, existing task ID
**Output**:
- Success: "Task {id} marked as incomplete"
- Error: Appropriate error message
**Side Effects**: Updates task's completed status to False

### Command: `update`
**Purpose**: Update the title or description of an existing task
**Syntax**: `python main.py update <task_id> [--title "New Title"] [--description "New Description"]`
**Input**:
- task_id (required): Integer, existing task ID
- title (optional): String, 1-200 characters
- description (optional): String, 0-1000 characters
**Output**:
- Success: "Task {id} updated successfully"
- Error: Appropriate error message
**Side Effects**: Updates specified fields of the task

### Command: `delete`
**Purpose**: Remove a task from the todo list
**Syntax**: `python main.py delete <task_id>`
**Input**:
- task_id (required): Integer, existing task ID
**Output**:
- Success: "Task {id} deleted successfully"
- Error: Appropriate error message
**Side Effects**: Removes task from in-memory storage