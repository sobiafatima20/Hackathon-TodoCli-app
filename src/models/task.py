"""
Task model for the Todo CLI application.
Represents a single todo item with ID, title, description, completion status, priority, tags, and due date.
"""

from datetime import datetime
from typing import Optional, List


class Task:
    """
    Represents a single todo item with ID, title, description, completion status, priority, tags, and due date.
    """

    def __init__(self, task_id: int, title: str, description: Optional[str] = None, completed: bool = False,
                 priority: str = "medium", tags: List[str] = None, due_date: Optional[datetime] = None,
                 is_recurring: bool = False, recurrence_interval: Optional[int] = None, original_task_id: Optional[int] = None):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task (required)
            description (str, optional): Description of the task
            completed (bool): Completion status of the task (default: False)
            priority (str): Priority level of the task (default: "medium")
            tags (List[str], optional): List of tags associated with the task (default: [])
            due_date (datetime, optional): Due date of the task (default: None)
            is_recurring (bool): Whether the task repeats (default: False)
            recurrence_interval (int, optional): Interval in days between recurrences (default: None)
            original_task_id (int, optional): ID of the original task in recurrence chain (default: None)
        """
        self.id = task_id
        self.title = self._validate_title(title)
        self.description = self._validate_description(description) if description else ""
        self.completed = completed
        self.priority = self._validate_priority(priority)
        self.tags = self._validate_tags(tags if tags is not None else [])
        self.due_date = due_date
        self.is_recurring = is_recurring
        self.recurrence_interval = recurrence_interval
        self.original_task_id = original_task_id

    def _validate_title(self, title: str) -> str:
        """
        Validate the title according to the specification.

        Args:
            title (str): Title to validate

        Returns:
            str: Validated title

        Raises:
            ValueError: If title doesn't meet validation requirements
        """
        if not title:
            raise ValueError("Title must be provided and not empty")

        if len(title) < 1 or len(title) > 200:
            raise ValueError("Title length must be between 1 and 200 characters")

        return title

    def _validate_description(self, description: Optional[str]) -> str:
        """
        Validate the description according to the specification.

        Args:
            description (str, optional): Description to validate

        Returns:
            str: Validated description

        Raises:
            ValueError: If description doesn't meet validation requirements
        """
        if description and len(description) > 1000:
            raise ValueError("Description length must not exceed 1000 characters")

        return description if description else ""

    def _validate_priority(self, priority: str) -> str:
        """
        Validate the priority according to the specification.

        Args:
            priority (str): Priority level to validate

        Returns:
            str: Validated priority

        Raises:
            ValueError: If priority is not one of the allowed values
        """
        allowed_priorities = ["high", "medium", "low"]
        if priority not in allowed_priorities:
            raise ValueError(f"Priority must be one of: {', '.join(allowed_priorities)}")
        return priority

    def _validate_tags(self, tags: List[str]) -> List[str]:
        """
        Validate the tags according to the specification.

        Args:
            tags (List[str]): List of tags to validate

        Returns:
            List[str]: Validated tags

        Raises:
            ValueError: If tags is not a list of strings
        """
        if not isinstance(tags, list):
            raise ValueError("Tags must be a list of strings")

        for tag in tags:
            if not isinstance(tag, str):
                raise ValueError("Tags must be a list of strings")

        return tags

    def _validate_recurrence_interval(self, interval: Optional[int]) -> Optional[int]:
        """
        Validate the recurrence interval according to the specification.

        Args:
            interval (int, optional): Recurrence interval to validate

        Returns:
            int: Validated recurrence interval

        Raises:
            ValueError: If interval is not a positive integer when provided
        """
        if interval is not None and (not isinstance(interval, int) or interval <= 0):
            raise ValueError("Recurrence interval must be a positive integer")
        return interval

    def _validate_original_task_id(self, original_id: Optional[int]) -> Optional[int]:
        """
        Validate the original task ID according to the specification.

        Args:
            original_id (int, optional): Original task ID to validate

        Returns:
            int: Validated original task ID

        Raises:
            ValueError: If original_id is not a positive integer when provided
        """
        if original_id is not None and (not isinstance(original_id, int) or original_id <= 0):
            raise ValueError("Original task ID must be a positive integer")
        return original_id

    def _validate_due_date(self, due_date: Optional[datetime]) -> Optional[datetime]:
        """
        Validate the due date according to the specification.

        Args:
            due_date (datetime, optional): Due date to validate

        Returns:
            datetime: Validated due date

        Raises:
            ValueError: If due_date is not a datetime object or None
        """
        if due_date is not None and not isinstance(due_date, datetime):
            raise ValueError("Due date must be a datetime object or None")
        return due_date

    def mark_complete(self):
        """Mark the task as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False

    def update_title(self, new_title: str):
        """
        Update the task title with validation.

        Args:
            new_title (str): New title for the task
        """
        self.title = self._validate_title(new_title)

    def update_description(self, new_description: Optional[str]):
        """
        Update the task description with validation.

        Args:
            new_description (str, optional): New description for the task
        """
        self.description = self._validate_description(new_description) if new_description else ""

    def update_priority(self, new_priority: str):
        """
        Update the task priority with validation.

        Args:
            new_priority (str): New priority for the task
        """
        self.priority = self._validate_priority(new_priority)

    def update_tags(self, new_tags: List[str]):
        """
        Update the task tags with validation.

        Args:
            new_tags (List[str]): New tags for the task
        """
        self.tags = self._validate_tags(new_tags)

    def update_due_date(self, new_due_date: Optional[datetime]):
        """
        Update the task due date.

        Args:
            new_due_date (datetime, optional): New due date for the task
        """
        # For now, just update the due date without validation
        # In a real implementation, you might want to validate that due_date is a datetime object or None
        self.due_date = new_due_date

    def update_is_recurring(self, new_is_recurring: bool):
        """
        Update the task recurring status.

        Args:
            new_is_recurring (bool): New recurring status for the task
        """
        if not isinstance(new_is_recurring, bool):
            raise ValueError("is_recurring must be a boolean value")
        self.is_recurring = new_is_recurring

    def update_recurrence_interval(self, new_recurrence_interval: Optional[int]):
        """
        Update the task recurrence interval with validation.

        Args:
            new_recurrence_interval (int, optional): New recurrence interval for the task
        """
        self.recurrence_interval = self._validate_recurrence_interval(new_recurrence_interval)

    def update_original_task_id(self, new_original_task_id: Optional[int]):
        """
        Update the task original task ID with validation.

        Args:
            new_original_task_id (int, optional): New original task ID for the task
        """
        self.original_task_id = self._validate_original_task_id(new_original_task_id)

    def add_tag(self, tag: str):
        """
        Add a single tag to the task if it doesn't already exist.

        Args:
            tag (str): Tag to add to the task
        """
        if isinstance(tag, str) and tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        """
        Remove a single tag from the task if it exists.

        Args:
            tag (str): Tag to remove from the task
        """
        if tag in self.tags:
            self.tags.remove(tag)

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.

        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority,
            "tags": self.tags,
            "due_date": self.due_date,
            "is_recurring": self.is_recurring,
            "recurrence_interval": self.recurrence_interval,
            "original_task_id": self.original_task_id
        }

    def __str__(self) -> str:
        """
        String representation of the task.

        Returns:
            str: Formatted string representation of the task
        """
        status = "✓" if self.completed else "○"
        priority_indicator = self.priority[0].upper()  # H for high, M for medium, L for low
        tags_str = f" [{', '.join(self.tags)}]" if self.tags else ""
        due_date_str = f" (due: {self.due_date.strftime('%Y-%m-%d')})" if self.due_date else ""
        recurrence_str = " (recurring)" if self.is_recurring else ""
        return f"[{status}] {self.id}. {self.title} ({priority_indicator}) - {self.description}{tags_str}{due_date_str}{recurrence_str}"

    def __repr__(self) -> str:
        """
        Developer-friendly representation of the task.

        Returns:
            str: Developer-friendly string representation
        """
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed}, priority='{self.priority}', tags={self.tags}, due_date={self.due_date}, is_recurring={self.is_recurring}, recurrence_interval={self.recurrence_interval}, original_task_id={self.original_task_id})"