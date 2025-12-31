# Data Model: Intermediate Level – Organization & Usability

## Task Entity

### Attributes
- **id**: int - Unique identifier for the task (auto-incremented)
- **title**: str - Title of the task (required)
- **description**: str - Detailed description of the task (optional, default: "")
- **completed**: bool - Completion status (default: False)
- **priority**: str - Priority level (values: "high", "medium", "low", default: "medium")
- **tags**: list[str] - List of tags associated with the task (default: [])
- **due_date**: datetime or None - Due date and time for the task (optional, default: None)

### Validation Rules
- priority must be one of: "high", "medium", "low"
- tags must be a list of strings
- title must not be empty

### State Transitions
- completed can transition from False to True (mark complete) or True to False (mark incomplete)
- priority can be updated at any time
- tags can be added, removed, or modified at any time

## TaskManager Entity

### Methods Related to Intermediate Features
- **add_task(title, description="", priority="medium", tags=[], due_date=None)**: Creates a new task with specified attributes
- **update_task(task_id, title=None, description=None, priority=None, tags=None, due_date=None)**: Updates task attributes
- **search_tasks(keyword)**: Returns list of tasks matching the keyword in title, description, or tags
- **filter_tasks(status=None, priority=None, due_date=None)**: Returns list of tasks matching the specified criteria
- **sort_tasks(sort_by)**: Returns sorted list of tasks based on specified criteria (title, priority, due_date)

### Relationships
- TaskManager maintains a collection of Task objects in memory
- Each Task is uniquely identified by its id within the TaskManager