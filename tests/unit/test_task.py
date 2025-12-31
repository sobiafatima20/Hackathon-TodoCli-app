"""
Unit tests for the Task model in the Todo CLI application with priority and tags support.
"""

import unittest
import sys
import os

# Add the project root to the path to allow absolute imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.task import Task


class TestTask(unittest.TestCase):
    """
    Unit tests for the Task model with priority and tags support.
    """

    def test_task_creation_with_valid_data(self):
        """Test creating a task with valid data."""
        task = Task(1, "Test Title", "Test Description", False)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertEqual(task.priority, "medium")  # Default priority
        self.assertEqual(task.tags, [])  # Default tags

    def test_task_creation_with_minimum_title_length(self):
        """Test creating a task with the minimum title length."""
        task = Task(1, "A", "Test Description", False)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "A")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)

    def test_task_creation_with_empty_description(self):
        """Test creating a task with an empty description."""
        task = Task(1, "Test Title", "", False)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "")
        self.assertFalse(task.completed)

    def test_task_creation_with_none_description(self):
        """Test creating a task with a None description."""
        task = Task(1, "Test Title", None, False)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "")
        self.assertFalse(task.completed)

    def test_task_creation_defaults_completed_false(self):
        """Test that a task defaults to incomplete."""
        task = Task(1, "Test Title")
        self.assertFalse(task.completed)

    def test_title_validation_empty(self):
        """Test that creating a task with an empty title raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Task(1, "", "Test Description", False)
        self.assertIn("not empty", str(context.exception))

    def test_title_validation_none(self):
        """Test that creating a task with a None title raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Task(1, None, "Test Description", False)
        self.assertIn("not empty", str(context.exception))

    def test_title_validation_too_long(self):
        """Test that creating a task with a title longer than 200 chars raises ValueError."""
        long_title = "A" * 201
        with self.assertRaises(ValueError) as context:
            Task(1, long_title, "Test Description", False)
        self.assertIn("200 characters", str(context.exception))

    def test_description_validation_too_long(self):
        """Test that creating a task with a description longer than 1000 chars raises ValueError."""
        long_description = "A" * 1001
        with self.assertRaises(ValueError) as context:
            Task(1, "Test Title", long_description, False)
        self.assertIn("1000 characters", str(context.exception))

    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = Task(1, "Test Title", "Test Description", False)
        task.mark_complete()
        self.assertTrue(task.completed)

    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task = Task(1, "Test Title", "Test Description", True)
        task.mark_incomplete()
        self.assertFalse(task.completed)

    def test_update_title_valid(self):
        """Test updating a task's title with valid data."""
        task = Task(1, "Old Title", "Test Description", False)
        task.update_title("New Title")
        self.assertEqual(task.title, "New Title")

    def test_update_title_invalid_empty(self):
        """Test updating a task's title with an empty title."""
        task = Task(1, "Old Title", "Test Description", False)
        with self.assertRaises(ValueError) as context:
            task.update_title("")
        self.assertIn("not empty", str(context.exception))

    def test_update_title_invalid_too_long(self):
        """Test updating a task's title with a title longer than 200 chars."""
        task = Task(1, "Old Title", "Test Description", False)
        long_title = "A" * 201
        with self.assertRaises(ValueError) as context:
            task.update_title(long_title)
        self.assertIn("200 characters", str(context.exception))

    def test_update_description_valid(self):
        """Test updating a task's description with valid data."""
        task = Task(1, "Test Title", "Old Description", False)
        task.update_description("New Description")
        self.assertEqual(task.description, "New Description")

    def test_update_description_none(self):
        """Test updating a task's description to None."""
        task = Task(1, "Test Title", "Old Description", False)
        task.update_description(None)
        self.assertEqual(task.description, "")

    def test_update_description_invalid_too_long(self):
        """Test updating a task's description with a description longer than 1000 chars."""
        task = Task(1, "Test Title", "Old Description", False)
        long_description = "A" * 1001
        with self.assertRaises(ValueError) as context:
            task.update_description(long_description)
        self.assertIn("1000 characters", str(context.exception))

    def test_to_dict(self):
        """Test converting a task to a dictionary."""
        task = Task(1, "Test Title", "Test Description", True)
        task_dict = task.to_dict()
        expected = {
            "id": 1,
            "title": "Test Title",
            "description": "Test Description",
            "completed": True,
            "priority": "medium",  # Default priority
            "tags": [],  # Default tags
            "due_date": None,
            "is_recurring": False,
            "recurrence_interval": None,
            "original_task_id": None
        }
        self.assertEqual(task_dict, expected)

    def test_str_representation(self):
        """Test the string representation of a task."""
        task = Task(1, "Test Title", "Test Description", True)
        expected = "[✓] 1. Test Title (M) - Test Description"
        self.assertEqual(str(task), expected)

        # Test with incomplete task
        task_incomplete = Task(2, "Test Title", "Test Description", False)
        expected_incomplete = "[○] 2. Test Title (M) - Test Description"
        self.assertEqual(str(task_incomplete), expected_incomplete)

    def test_task_creation_with_priority_and_tags(self):
        """Test creating a task with priority and tags."""
        task = Task(1, "Test Title", "Test Description", False, "high", ["work", "urgent"])
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, ["work", "urgent"])

    def test_task_creation_with_default_priority(self):
        """Test creating a task with default priority when not specified."""
        task = Task(1, "Test Title")
        self.assertEqual(task.priority, "medium")

    def test_task_creation_with_default_tags(self):
        """Test creating a task with default empty tags when not specified."""
        task = Task(1, "Test Title")
        self.assertEqual(task.tags, [])

    def test_priority_validation_valid_values(self):
        """Test that valid priority values are accepted."""
        for priority in ["high", "medium", "low"]:
            task = Task(1, "Test Title", priority=priority)
            self.assertEqual(task.priority, priority)

    def test_priority_validation_invalid_value(self):
        """Test that invalid priority values raise ValueError."""
        with self.assertRaises(ValueError) as context:
            Task(1, "Test Title", priority="invalid")
        self.assertIn("Priority must be one of", str(context.exception))

    def test_tags_validation_valid_list(self):
        """Test that valid tag lists are accepted."""
        task = Task(1, "Test Title", tags=["work", "personal"])
        self.assertEqual(task.tags, ["work", "personal"])

    def test_tags_validation_empty_list(self):
        """Test that empty tag list is accepted."""
        task = Task(1, "Test Title", tags=[])
        self.assertEqual(task.tags, [])

    def test_tags_validation_not_list(self):
        """Test that non-list tags raise ValueError."""
        with self.assertRaises(ValueError) as context:
            Task(1, "Test Title", tags="not_a_list")
        self.assertIn("Tags must be a list", str(context.exception))

    def test_tags_validation_non_string_elements(self):
        """Test that non-string elements in tags list raise ValueError."""
        with self.assertRaises(ValueError) as context:
            Task(1, "Test Title", tags=["valid", 123, "also_valid"])
        self.assertIn("Tags must be a list of strings", str(context.exception))

    def test_update_priority_valid(self):
        """Test updating a task's priority with valid value."""
        task = Task(1, "Test Title", priority="low")
        task.update_priority("high")
        self.assertEqual(task.priority, "high")

    def test_update_priority_invalid(self):
        """Test updating a task's priority with invalid value."""
        task = Task(1, "Test Title", priority="low")
        with self.assertRaises(ValueError) as context:
            task.update_priority("invalid")
        self.assertIn("Priority must be one of", str(context.exception))

    def test_update_tags_valid(self):
        """Test updating a task's tags with valid list."""
        task = Task(1, "Test Title", tags=["old"])
        task.update_tags(["new", "tags"])
        self.assertEqual(task.tags, ["new", "tags"])

    def test_update_tags_invalid(self):
        """Test updating a task's tags with invalid value."""
        task = Task(1, "Test Title", tags=["old"])
        with self.assertRaises(ValueError) as context:
            task.update_tags("not_a_list")
        self.assertIn("Tags must be a list", str(context.exception))

    def test_add_tag(self):
        """Test adding a single tag to a task."""
        task = Task(1, "Test Title", tags=["existing"])
        task.add_tag("new_tag")
        self.assertIn("new_tag", task.tags)
        self.assertIn("existing", task.tags)

    def test_add_tag_duplicate(self):
        """Test adding a duplicate tag to a task."""
        task = Task(1, "Test Title", tags=["existing"])
        original_count = len(task.tags)
        task.add_tag("existing")  # Should not add duplicate
        self.assertEqual(len(task.tags), original_count)

    def test_remove_tag(self):
        """Test removing a tag from a task."""
        task = Task(1, "Test Title", tags=["existing", "to_remove"])
        task.remove_tag("to_remove")
        self.assertNotIn("to_remove", task.tags)
        self.assertIn("existing", task.tags)

    def test_remove_tag_not_present(self):
        """Test removing a tag that doesn't exist."""
        task = Task(1, "Test Title", tags=["existing"])
        original_count = len(task.tags)
        task.remove_tag("not_present")  # Should not change anything
        self.assertEqual(len(task.tags), original_count)

    def test_to_dict_with_priority_and_tags(self):
        """Test converting a task to a dictionary with priority and tags."""
        task = Task(1, "Test Title", "Test Description", True, "high", ["work", "urgent"])
        task_dict = task.to_dict()
        expected = {
            "id": 1,
            "title": "Test Title",
            "description": "Test Description",
            "completed": True,
            "priority": "high",
            "tags": ["work", "urgent"],
            "due_date": None,
            "is_recurring": False,
            "recurrence_interval": None,
            "original_task_id": None
        }
        self.assertEqual(task_dict, expected)

    def test_str_representation_with_priority_and_tags(self):
        """Test the string representation of a task with priority and tags."""
        task = Task(1, "Test Title", "Test Description", True, "high", ["work", "urgent"])
        expected = "[✓] 1. Test Title (H) - Test Description [work, urgent]"
        self.assertEqual(str(task), expected)

        # Test with incomplete task and tags
        task_incomplete = Task(2, "Test Title", "Test Description", False, "low", ["personal"])
        expected_incomplete = "[○] 2. Test Title (L) - Test Description [personal]"
        self.assertEqual(str(task_incomplete), expected_incomplete)

        # Test with no tags
        task_no_tags = Task(3, "Test Title", "Test Description", True, "medium", [])
        expected_no_tags = "[✓] 3. Test Title (M) - Test Description"
        self.assertEqual(str(task_no_tags), expected_no_tags)

    def test_repr_representation(self):
        """Test the developer-friendly representation of a task."""
        task = Task(1, "Test Title", "Test Description", True, "high", ["work", "urgent"])
        expected = "Task(id=1, title='Test Title', description='Test Description', completed=True, priority='high', tags=['work', 'urgent'], due_date=None, is_recurring=False, recurrence_interval=None, original_task_id=None)"
        self.assertEqual(repr(task), expected)


if __name__ == "__main__":
    unittest.main()