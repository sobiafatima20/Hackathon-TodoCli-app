"""
TaskManager service for the Todo CLI application.
Handles in-memory storage and management of tasks with priority and tags support.
"""

import sys
import os
from datetime import datetime
from typing import Dict, List, Optional

# Add the project root to the path to allow absolute imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.task import Task


class TaskManager:
    """
    Manages tasks in-memory storage and business logic with support for priority and tags.
    """

    def __init__(self):
        """Initialize the TaskManager with an empty task dictionary and ID counter."""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def add_task(self, title: str, description: Optional[str] = None, priority: str = "medium",
                 tags: List[str] = None, due_date: Optional[datetime] = None,
                 is_recurring: bool = False, recurrence_interval: Optional[int] = None,
                 original_task_id: Optional[int] = None) -> Task:
        """
        Add a new task to the collection with priority, tags, due date, and recurrence support.

        Args:
            title (str): Title of the task
            description (str, optional): Description of the task
            priority (str): Priority level of the task (default: "medium")
            tags (List[str], optional): List of tags for the task (default: [])
            due_date (datetime, optional): Due date of the task (default: None)
            is_recurring (bool): Whether the task repeats (default: False)
            recurrence_interval (int, optional): Interval in days between recurrences (default: None)
            original_task_id (int, optional): ID of the original task in recurrence chain (default: None)

        Returns:
            Task: The newly created task
        """
        # Validate recurrence settings
        if is_recurring and recurrence_interval is None:
            raise ValueError("Recurrence interval must be provided for recurring tasks")
        if is_recurring and recurrence_interval is not None and recurrence_interval <= 0:
            raise ValueError("Recurrence interval must be a positive integer")

        # Validate recurrence chain integrity
        if original_task_id is not None and original_task_id not in self._tasks:
            raise ValueError(f"Original task ID {original_task_id} does not exist for recurrence chain")

        task_id = self._next_id
        self._next_id += 1
        task = Task(task_id, title, description, completed=False, priority=priority, tags=tags,
                   due_date=due_date, is_recurring=is_recurring, recurrence_interval=recurrence_interval,
                   original_task_id=original_task_id)
        self._tasks[task_id] = task
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Task or None: The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the collection.

        Returns:
            List[Task]: List of all tasks
        """
        return list(self._tasks.values())

    def update_task(self, task_id: int, title=..., description=..., priority=..., tags=..., due_date=...,
                   is_recurring=..., recurrence_interval=..., original_task_id=...) -> Optional[Task]:
        """
        Update a task's title, description, priority, tags, due date, or recurrence settings.

        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            priority (str, optional): New priority for the task
            tags (List[str], optional): New tags for the task
            due_date (datetime, optional): New due date for the task
            is_recurring (bool, optional): New recurring status for the task
            recurrence_interval (int, optional): New recurrence interval for the task
            original_task_id (int, optional): New original task ID for the task

        Returns:
            Task or None: Updated task if successful, None if task not found
        """
        task = self.get_task(task_id)
        if not task:
            return None

        # Validate the new values before updating
        if title is not ...:
            if title is not None:
                # Validate title using the same validation as in Task constructor
                task._validate_title(title)

        if description is not ...:
            if description is not None:
                # Validate description using the same validation as in Task constructor
                task._validate_description(description)

        if priority is not ...:
            if priority is not None:
                # Validate priority using the same validation as in Task constructor
                task._validate_priority(priority)

        if tags is not ...:
            if tags is not None:
                # Validate tags using the same validation as in Task constructor
                task._validate_tags(tags)

        if recurrence_interval is not ...:
            if recurrence_interval is not None:
                # Validate recurrence interval using the same validation as in Task constructor
                task._validate_recurrence_interval(recurrence_interval)

        if due_date is not ...:
            if due_date is not None:
                # Validate due date using the same validation as in Task constructor
                task._validate_due_date(due_date)

        if original_task_id is not ...:
            if original_task_id is not None:
                # Validate original task ID using the same validation as in Task constructor
                task._validate_original_task_id(original_task_id)

        # Update the task if validation passes
        if title is not ...:
            if title is not None:
                task.update_title(title)
            elif title is None:
                # If title is explicitly set to None, set it to empty string
                # Actually, this doesn't make sense for title. Title should not be None.
                # Let's just not change title if it's None.
                pass

        if description is not ...:
            if description is not None:
                task.update_description(description)
            elif description is None:
                # If description is explicitly set to None, set it to empty string
                task.update_description("")

        if priority is not ...:
            if priority is not None:
                task.update_priority(priority)

        if tags is not ...:
            if tags is not None:
                task.update_tags(tags)

        if due_date is not ...:
            if due_date is not None or due_date is None:  # Allow setting to None
                task.update_due_date(due_date)

        if is_recurring is not ...:
            if is_recurring is not None:
                task.update_is_recurring(is_recurring)

        if recurrence_interval is not ...:
            if recurrence_interval is not None or recurrence_interval is None:  # Allow setting to None
                task.update_recurrence_interval(recurrence_interval)

        if original_task_id is not ...:
            if original_task_id is not None or original_task_id is None:  # Allow setting to None
                task.update_original_task_id(original_task_id)

        return task

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id (int): ID of the task to mark complete

        Returns:
            bool: True if successful, False if task not found
        """
        task = self.get_task(task_id)
        if task:
            # Check if the task is recurring
            if task.is_recurring:
                # Handle recurring task completion by creating a new instance
                return self.handle_recurring_task_completion(task_id)
            else:
                # For non-recurring tasks, just mark as complete
                task.mark_complete()
                return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id (int): ID of the task to mark incomplete

        Returns:
            bool: True if successful, False if task not found
        """
        task = self.get_task(task_id)
        if task:
            task.mark_incomplete()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if successful, False if task not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            int: The next available ID
        """
        return self._next_id

    def validate_task_exists(self, task_id: int) -> bool:
        """
        Check if a task exists by its ID.

        Args:
            task_id (int): ID to check

        Returns:
            bool: True if task exists, False otherwise
        """
        return task_id in self._tasks

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword across title, description, and tags (case-insensitive).

        Args:
            keyword (str): Keyword to search for

        Returns:
            List[Task]: List of tasks that match the search criteria
        """
        if not keyword:
            return []

        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self._tasks.values():
            # Check if keyword matches in title (case-insensitive)
            if keyword_lower in task.title.lower():
                matching_tasks.append(task)
                continue

            # Check if keyword matches in description (case-insensitive)
            if keyword_lower in task.description.lower():
                matching_tasks.append(task)
                continue

            # Check if keyword matches in any of the tags (case-insensitive)
            for tag in task.tags:
                if keyword_lower in tag.lower():
                    matching_tasks.append(task)
                    break

        return matching_tasks

    def filter_tasks(self, status: Optional[bool] = None, priority: Optional[str] = None,
                    due_date: Optional[datetime] = None) -> List[Task]:
        """
        Filter tasks by status, priority, and due date.

        Args:
            status (bool, optional): Filter by completion status
            priority (str, optional): Filter by priority level
            due_date (datetime, optional): Filter by due date

        Returns:
            List[Task]: List of tasks that match the filter criteria
        """
        filtered_tasks = list(self._tasks.values())

        # Filter by status (completed/incomplete)
        if status is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed == status]

        # Filter by priority
        if priority is not None:
            filtered_tasks = [task for task in filtered_tasks if task.priority == priority]

        # Filter by due date
        if due_date is not None:
            # Filter tasks that have the same due date (comparing just the date part)
            filtered_tasks = [task for task in filtered_tasks
                             if task.due_date and task.due_date.date() == due_date.date()]

        return filtered_tasks

    def sort_tasks(self, sort_by: str) -> List[Task]:
        """
        Sort tasks by specified criteria (title, priority, due_date).
        Note: This returns a sorted list without modifying the original storage order.

        Args:
            sort_by (str): Criteria to sort by ('title', 'priority', 'due_date')

        Returns:
            List[Task]: List of tasks sorted by the specified criteria
        """
        if sort_by == 'title':
            # Sort by title alphabetically
            return sorted(self._tasks.values(), key=lambda task: task.title.lower())
        elif sort_by == 'priority':
            # Sort by priority: high, medium, low
            priority_order = {'high': 0, 'medium': 1, 'low': 2}
            return sorted(self._tasks.values(), key=lambda task: priority_order[task.priority])
        elif sort_by == 'due_date':
            # Sort by due date: earliest first
            # Tasks without due dates will be placed at the end
            def due_date_key(task):
                if task.due_date is None:
                    # Use a far future date to push tasks without due dates to the end
                    return datetime.max
                return task.due_date
            return sorted(self._tasks.values(), key=due_date_key)
        else:
            # Default to sorting by ID if invalid sort_by parameter
            return sorted(self._tasks.values(), key=lambda task: task.id)

    def handle_recurring_task_completion(self, task_id: int) -> bool:
        """
        Handle completion of a recurring task by creating a new instance.

        Args:
            task_id (int): ID of the recurring task to complete

        Returns:
            bool: True if recurring task was handled correctly, False if task not found or not recurring
        """
        task = self.get_task(task_id)
        if not task or not task.is_recurring:
            return False

        # Mark the original task as complete
        task.mark_complete()

        # Calculate the next due date based on the recurrence interval
        next_due_date = None
        if task.due_date and task.recurrence_interval:
            from datetime import timedelta
            next_due_date = task.due_date + timedelta(days=task.recurrence_interval)

        # Create a new task with the same properties but new ID and due date
        new_task = Task(
            task_id=self._next_id,
            title=task.title,
            description=task.description,
            completed=False,
            priority=task.priority,
            tags=task.tags.copy(),  # Copy the tags list
            due_date=next_due_date,
            is_recurring=task.is_recurring,
            recurrence_interval=task.recurrence_interval,
            original_task_id=task.id  # Reference to the original task
        )

        # Add the new task to the collection
        self._tasks[self._next_id] = new_task
        self._next_id += 1

        return True

    def get_recurring_tasks(self) -> List[Task]:
        """
        Get all recurring tasks.

        Returns:
            List[Task]: List of all recurring tasks
        """
        return [task for task in self._tasks.values() if task.is_recurring]

    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all tasks that are past their due date.

        Returns:
            List[Task]: List of all overdue tasks
        """
        from datetime import datetime
        today = datetime.now().date()
        return [task for task in self._tasks.values()
                if task.due_date and task.due_date.date() < today and not task.completed]

    def get_upcoming_tasks(self, days_ahead: int) -> List[Task]:
        """
        Get tasks due within the specified number of days.

        Args:
            days_ahead (int): Number of days to look ahead

        Returns:
            List[Task]: List of tasks due within the specified number of days
        """
        from datetime import datetime, timedelta
        if days_ahead <= 0:
            raise ValueError("days_ahead must be a positive integer")

        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=days_ahead)
        return [task for task in self._tasks.values()
                if task.due_date and start_date <= task.due_date.date() <= end_date and not task.completed]

    def get_todays_tasks(self) -> List[Task]:
        """
        Get all tasks due today.

        Returns:
            List[Task]: List of tasks due today
        """
        from datetime import datetime
        today = datetime.now().date()
        return [task for task in self._tasks.values()
                if task.due_date and task.due_date.date() == today and not task.completed]