# Quickstart Guide: Intermediate Level Features

## New Features Overview

The Intermediate Level adds these organizational features to your CLI Todo application:

1. **Task Priorities**: Assign high/medium/low priority levels to tasks
2. **Tags**: Add categorization tags to tasks (e.g., work, personal, home)
3. **Search**: Find tasks by keyword across title, description, and tags
4. **Filter**: Show only tasks matching specific criteria
5. **Sort**: Arrange tasks by priority, title, or due date

## Using Priority Levels

```bash
# Add a task with high priority
python todo.py add "Important meeting" --priority high

# Update an existing task's priority
python todo.py update 1 --priority low

# View tasks with priority indicators
python todo.py list
```

## Using Tags

```bash
# Add a task with tags
python todo.py add "Prepare presentation" --tags work,important

# Update a task with tags
python todo.py update 1 --tags personal,home

# View tasks with tags displayed
python todo.py list
```

## Search Functionality

```bash
# Search for tasks containing a keyword
python todo.py search "meeting"

# Search is case-insensitive and matches title, description, and tags
python todo.py search "WORK"
```

## Filter Functionality

```bash
# Filter tasks by completion status
python todo.py filter --status incomplete

# Filter by priority
python todo.py filter --priority high

# Combine multiple filters
python todo.py filter --status incomplete --priority high
```

## Sort Functionality

```bash
# Sort tasks by priority (high to low)
python todo.py sort --by priority

# Sort by title alphabetically
python todo.py sort --by title

# Sort by due date (earliest first)
python todo.py sort --by due_date
```

## Combined Usage

You can chain these features together:

```bash
# Add a high priority work task with due date
python todo.py add "Project deadline" --priority high --tags work --due-date 2025-01-15

# Search for high priority work tasks
python todo.py search "project" --priority high --tags work

# Filter and sort results
python todo.py filter --status incomplete --priority high | python todo.py sort --by due_date
```