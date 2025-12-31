# Data Model: Advanced Level – Intelligent Features

## Task Model Extensions

### Extended Task Entity

The Task entity will be extended to support recurring tasks and due dates while maintaining backward compatibility.

#### Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| id | int | N/A | Unique identifier for the task |
| title | str | N/A | Title of the task (1-200 characters) |
| description | str | "" | Description of the task (0-1000 characters) |
| completed | bool | False | Completion status of the task |
| priority | str | "medium" | Priority level ("high", "medium", "low") |
| tags | List[str] | [] | List of tags associated with the task |
| due_date | Optional[datetime] | None | Due date and time for the task |
| is_recurring | bool | False | Whether the task repeats |
| recurrence_interval | Optional[int] | None | Interval in days between recurrences (for recurring tasks) |
| original_task_id | Optional[int] | None | ID of the original task in recurrence chain (for recurring task instances) |

#### Validation Rules

1. **Title**: Must be 1-200 characters, not empty
2. **Description**: Must be 0-1000 characters
3. **Priority**: Must be one of "high", "medium", "low"
4. **Tags**: Must be a list of strings, each tag must be non-empty
5. **Due Date**: If present, must be a valid datetime object
6. **Recurrence Interval**: If task is recurring, must be a positive integer
7. **Original Task ID**: If present, must reference an existing task

#### Relationships

- **Recurrence Chain**: A recurring task creates new instances linked by `original_task_id` to track the recurrence chain
- **Original Task**: All instances of a recurring task reference the original task that defines the recurrence pattern

## Task Manager Extensions

### Enhanced Task Manager

The TaskManager will be extended to handle the new functionality while maintaining all existing operations.

#### New Methods

| Method | Parameters | Return Type | Description |
|--------|------------|-------------|-------------|
| `get_overdue_tasks()` | None | List[Task] | Returns all tasks past their due date |
| `get_upcoming_tasks(days_ahead: int)` | int | List[Task] | Returns tasks due within specified number of days |
| `get_todays_tasks()` | None | List[Task] | Returns tasks due today |
| `handle_recurring_task_completion(task_id: int)` | int | bool | Handles completion of recurring task by creating new instance |
| `get_recurring_tasks()` | None | List[Task] | Returns all recurring tasks |

#### Modified Methods

| Method | Modified Parameters | Description |
|--------|-------------------|-------------|
| `add_task()` | Added `due_date`, `is_recurring`, `recurrence_interval` parameters | Creates tasks with optional due date and recurrence settings |
| `update_task()` | Added `due_date`, `is_recurring`, `recurrence_interval` parameters | Updates tasks with optional due date and recurrence settings |

## CLI Command Extensions

### Extended CLI Commands

The CLI will be extended with new commands and parameters while maintaining all existing functionality.

#### New Commands

| Command | Parameters | Description |
|---------|------------|-------------|
| `recurring` | `--list`, `--task-id`, `--new-interval` | Manage recurring tasks |
| `reminders` | `--overdue`, `--upcoming`, `--days` | View reminders for overdue or upcoming tasks |

#### Extended Commands

| Command | New Parameters | Description |
|---------|----------------|-------------|
| `add` | `--due-date`, `--recurring`, `--interval` | Add task with due date and recurrence settings |
| `update` | `--due-date`, `--recurring`, `--interval` | Update task with due date and recurrence settings |
| `view` | `--overdue`, `--upcoming`, `--recurring` | Filter tasks by due date or recurrence status |

## Data Flow

### Recurrence Flow

1. User creates a recurring task with interval
2. When recurring task is marked complete:
   - New task is created with same properties
   - New task gets next due date based on recurrence interval
   - New task has reference to original task ID
3. Original recurring task remains in system to maintain recurrence pattern

### Due Date Flow

1. Tasks may optionally include due dates
2. System checks for overdue tasks when viewing tasks
3. System highlights upcoming due dates
4. Due dates are displayed in all task listings

## Backward Compatibility

### Existing Data Compatibility

- All existing tasks will have `is_recurring=False` by default
- All existing tasks will have `due_date=None` by default
- All existing tasks will have `recurrence_interval=None` by default
- All existing tasks will have `original_task_id=None` by default
- All existing functionality remains unchanged

### API Compatibility

- All existing method signatures remain compatible
- New parameters are optional with sensible defaults
- All existing return types remain the same
- All existing error handling remains the same