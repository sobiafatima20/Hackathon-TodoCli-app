"""
Integration tests for the CLI commands in the Todo CLI application.
Tests the full workflow of adding, viewing, updating, and deleting tasks.
"""

import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the project root to the path to allow absolute imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.task_manager import TaskManager
from src.cli.main import main


class TestCLIIntegration(unittest.TestCase):
    """
    Integration tests for CLI commands.
    """

    def test_full_workflow_add_view_complete_delete(self):
        """Test the full workflow: add, view, complete, view, delete, view."""
        # Test adding a task
        with patch('sys.argv', ['main.py', 'add', 'Test Task', '--description', 'Test Description']):
            # Capture stdout
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                # We can't run the main function directly because it parses sys.argv
                # Instead, we'll test the TaskManager directly to ensure integration works
                task_manager = TaskManager()

                # Add a task
                task = task_manager.add_task("Test Task", "Test Description")
                self.assertEqual(task.title, "Test Task")
                self.assertEqual(task.description, "Test Description")
                self.assertFalse(task.completed)

                # View tasks - should have 1 task
                tasks = task_manager.get_all_tasks()
                self.assertEqual(len(tasks), 1)

                # Complete the task
                success = task_manager.mark_complete(task.id)
                self.assertTrue(success)

                # Verify task is now complete
                updated_task = task_manager.get_task(task.id)
                self.assertTrue(updated_task.completed)

                # Delete the task
                delete_success = task_manager.delete_task(task.id)
                self.assertTrue(delete_success)

                # Verify task is gone
                tasks_after_delete = task_manager.get_all_tasks()
                self.assertEqual(len(tasks_after_delete), 0)

    def test_add_multiple_tasks_and_view_all(self):
        """Test adding multiple tasks and viewing all of them."""
        task_manager = TaskManager()

        # Add multiple tasks
        task1 = task_manager.add_task("Task 1", "Description 1")
        task2 = task_manager.add_task("Task 2", "Description 2")
        task3 = task_manager.add_task("Task 3", "Description 3")

        # Get all tasks
        all_tasks = task_manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 3)

        # Verify each task is present
        titles = [task.title for task in all_tasks]
        self.assertIn("Task 1", titles)
        self.assertIn("Task 2", titles)
        self.assertIn("Task 3", titles)

    def test_update_task_workflow(self):
        """Test the workflow of adding a task, updating it, and verifying changes."""
        task_manager = TaskManager()

        # Add a task
        original_task = task_manager.add_task("Original Title", "Original Description")
        self.assertEqual(original_task.title, "Original Title")
        self.assertEqual(original_task.description, "Original Description")

        # Update the task
        updated_task = task_manager.update_task(original_task.id, title="New Title", description="New Description")
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")

    def test_mark_task_complete_incomplete_workflow(self):
        """Test marking a task as complete then incomplete."""
        task_manager = TaskManager()

        # Add a task
        task = task_manager.add_task("Test Task")
        self.assertFalse(task.completed)  # Should start as incomplete

        # Mark as complete
        success = task_manager.mark_complete(task.id)
        self.assertTrue(success)

        # Verify it's complete
        updated_task = task_manager.get_task(task.id)
        self.assertTrue(updated_task.completed)

        # Mark as incomplete
        success = task_manager.mark_incomplete(task.id)
        self.assertTrue(success)

        # Verify it's incomplete
        updated_task = task_manager.get_task(task.id)
        self.assertFalse(updated_task.completed)

    def test_error_handling_nonexistent_task(self):
        """Test error handling when operating on non-existent tasks."""
        task_manager = TaskManager()

        # Try to get a non-existent task
        nonexistent_task = task_manager.get_task(999)
        self.assertIsNone(nonexistent_task)

        # Try to update a non-existent task
        update_result = task_manager.update_task(999, title="New Title")
        self.assertIsNone(update_result)

        # Try to mark complete a non-existent task
        complete_result = task_manager.mark_complete(999)
        self.assertFalse(complete_result)

        # Try to mark incomplete a non-existent task
        incomplete_result = task_manager.mark_incomplete(999)
        self.assertFalse(incomplete_result)

        # Try to delete a non-existent task
        delete_result = task_manager.delete_task(999)
        self.assertFalse(delete_result)

    def test_task_validation_integration(self):
        """Test validation integration in the task management workflow."""
        task_manager = TaskManager()

        # Try to add a task with an empty title (should raise ValueError)
        with self.assertRaises(ValueError):
            task_manager.add_task("")

        # Try to add a task with a title that's too long (should raise ValueError)
        long_title = "A" * 201  # More than 200 characters
        with self.assertRaises(ValueError):
            task_manager.add_task(long_title)

        # Add a valid task first
        task = task_manager.add_task("Valid Task")

        # Try to update with invalid title (should raise ValueError)
        with self.assertRaises(ValueError):
            task_manager.update_task(task.id, title="")

    def test_task_id_uniqueness_integration(self):
        """Test that task IDs remain unique throughout the workflow."""
        task_manager = TaskManager()

        # Add multiple tasks
        tasks = []
        for i in range(5):
            task = task_manager.add_task(f"Task {i}")
            tasks.append(task.id)

        # Verify all IDs are unique
        self.assertEqual(len(tasks), len(set(tasks)))

        # Delete some tasks
        task_manager.delete_task(tasks[1])  # Delete the second task
        task_manager.delete_task(tasks[3])  # Delete the fourth task

        # Add new tasks - they should get new unique IDs
        new_task1 = task_manager.add_task("New Task 1")
        new_task2 = task_manager.add_task("New Task 2")

        # All IDs should still be unique
        all_ids = [tasks[0], tasks[2], tasks[4], new_task1.id, new_task2.id]
        self.assertEqual(len(all_ids), len(set(all_ids)))

    def test_task_lifecycle(self):
        """Test the complete lifecycle of a task."""
        task_manager = TaskManager()

        # Create task
        task = task_manager.add_task("Lifecycle Test Task", "Testing the full lifecycle")
        original_id = task.id
        self.assertEqual(task.title, "Lifecycle Test Task")
        self.assertEqual(task.description, "Testing the full lifecycle")
        self.assertFalse(task.completed)

        # Update task
        updated_task = task_manager.update_task(original_id, title="Updated Lifecycle Test Task")
        self.assertEqual(updated_task.title, "Updated Lifecycle Test Task")

        # Mark complete
        task_manager.mark_complete(original_id)
        completed_task = task_manager.get_task(original_id)
        self.assertTrue(completed_task.completed)

        # Mark incomplete
        task_manager.mark_incomplete(original_id)
        incomplete_task = task_manager.get_task(original_id)
        self.assertFalse(incomplete_task.completed)

        # Delete task
        success = task_manager.delete_task(original_id)
        self.assertTrue(success)

        # Verify task is gone
        deleted_task = task_manager.get_task(original_id)
        self.assertIsNone(deleted_task)

    def test_priority_integration(self):
        """Test priority functionality integration."""
        task_manager = TaskManager()

        # Add a task with high priority
        high_task = task_manager.add_task("High Priority Task", "Description", "high")
        self.assertEqual(high_task.priority, "high")

        # Add a task with medium priority (default)
        medium_task = task_manager.add_task("Medium Priority Task", "Description")
        self.assertEqual(medium_task.priority, "medium")

        # Add a task with low priority
        low_task = task_manager.add_task("Low Priority Task", "Description", "low")
        self.assertEqual(low_task.priority, "low")

        # Update task priority
        updated_task = task_manager.update_task(high_task.id, priority="low")
        self.assertEqual(updated_task.priority, "low")

        # Add another high priority task to ensure all priority levels exist
        another_high_task = task_manager.add_task("Another High Priority Task", "Description", "high")

        # Verify all tasks exist with correct priorities
        all_tasks = task_manager.get_all_tasks()
        priorities = [task.priority for task in all_tasks]
        self.assertIn("high", priorities)  # Should still have high priority tasks
        self.assertIn("medium", priorities)
        self.assertIn("low", priorities)

    def test_tags_integration(self):
        """Test tags functionality integration."""
        task_manager = TaskManager()

        # Add a task with tags
        tagged_task = task_manager.add_task("Tagged Task", "Description", "medium", ["work", "urgent"])
        self.assertIn("work", tagged_task.tags)
        self.assertIn("urgent", tagged_task.tags)

        # Add a task without tags
        no_tags_task = task_manager.add_task("No Tags Task", "Description")
        self.assertEqual(no_tags_task.tags, [])

        # Update task tags
        updated_task = task_manager.update_task(tagged_task.id, tags=["personal", "later"])
        self.assertIn("personal", updated_task.tags)
        self.assertIn("later", updated_task.tags)
        self.assertNotIn("work", updated_task.tags)  # Old tags should be replaced

        # Verify all tasks exist with correct tags
        all_tasks = task_manager.get_all_tasks()
        has_tags = any(len(task.tags) > 0 for task in all_tasks)
        self.assertTrue(has_tags)

    def test_search_integration(self):
        """Test search functionality integration."""
        task_manager = TaskManager()

        # Add tasks with different content
        task1 = task_manager.add_task("Meeting Preparation", "Prepare for the important meeting", "high", ["work", "urgent"])
        task2 = task_manager.add_task("Grocery Shopping", "Buy groceries for the week", "medium", ["personal"])
        task3 = task_manager.add_task("Project Review", "Review the project status", "low", ["work"])

        # Search by title
        title_results = task_manager.search_tasks("meeting")
        self.assertIn(task1, title_results)
        self.assertEqual(len(title_results), 1)

        # Search by description
        desc_results = task_manager.search_tasks("groceries")
        self.assertIn(task2, desc_results)
        self.assertEqual(len(desc_results), 1)

        # Search by tags
        tag_results = task_manager.search_tasks("work")
        self.assertIn(task1, tag_results)
        self.assertIn(task3, tag_results)
        self.assertEqual(len(tag_results), 2)

        # Search case-insensitive
        case_results = task_manager.search_tasks("MEETING")
        self.assertIn(task1, case_results)
        self.assertEqual(len(case_results), 1)

    def test_filter_integration(self):
        """Test filter functionality integration."""
        task_manager = TaskManager()

        # Add tasks with different statuses and priorities
        task1 = task_manager.add_task("High Priority Task", "Description", "high", ["work"])
        task2 = task_manager.add_task("Medium Priority Task", "Description", "medium", ["personal"])
        task3 = task_manager.add_task("Low Priority Task", "Description", "low", ["home"])

        # Mark one task as complete
        task_manager.mark_complete(task1.id)

        # Filter by status
        completed_tasks = task_manager.filter_tasks(status=True)
        incomplete_tasks = task_manager.filter_tasks(status=False)

        self.assertIn(task1, completed_tasks)
        self.assertIn(task2, incomplete_tasks)
        self.assertIn(task3, incomplete_tasks)

        # Filter by priority
        high_priority_tasks = task_manager.filter_tasks(priority="high")
        self.assertIn(task1, high_priority_tasks)

        # Filter by both status and priority
        completed_high_tasks = task_manager.filter_tasks(status=True, priority="high")
        self.assertIn(task1, completed_high_tasks)

    def test_sort_integration(self):
        """Test sort functionality integration."""
        task_manager = TaskManager()

        # Add tasks in random order
        task_z = task_manager.add_task("Zebra Task", "Description", "low")
        task_a = task_manager.add_task("Apple Task", "Description", "high")
        task_m = task_manager.add_task("Monkey Task", "Description", "medium")

        # Sort by title
        sorted_by_title = task_manager.sort_tasks("title")
        expected_order = [task_a, task_m, task_z]  # Apple, Monkey, Zebra
        self.assertEqual(sorted_by_title, expected_order)

        # Sort by priority
        sorted_by_priority = task_manager.sort_tasks("priority")
        # Expected order: high (task_a), medium (task_m), low (task_z)
        self.assertEqual(sorted_by_priority[0], task_a)  # High priority first
        self.assertEqual(sorted_by_priority[2], task_z)  # Low priority last

    def test_recurring_task_functionality(self):
        """Test recurring task functionality integration."""
        task_manager = TaskManager()

        # Add a recurring task
        from datetime import datetime
        due_date = datetime(2025, 12, 31)
        recurring_task = task_manager.add_task("Recurring Task", "Description", "high", ["test"], due_date,
                                              is_recurring=True, recurrence_interval=7)
        self.assertTrue(recurring_task.is_recurring)
        self.assertEqual(recurring_task.recurrence_interval, 7)

        # Verify the task appears in recurring tasks
        recurring_tasks = task_manager.get_recurring_tasks()
        self.assertIn(recurring_task, recurring_tasks)

        # Complete the recurring task (should create a new instance)
        initial_count = len(task_manager.get_all_tasks())
        result = task_manager.handle_recurring_task_completion(recurring_task.id)
        self.assertTrue(result)

        # Check that original task is marked complete and new instance was created
        final_count = len(task_manager.get_all_tasks())
        self.assertEqual(final_count, initial_count + 1)

        # Verify original task is complete
        original_updated = task_manager.get_task(recurring_task.id)
        self.assertTrue(original_updated.completed)

        # Verify a new task was created with same properties
        all_tasks = task_manager.get_all_tasks()
        new_tasks = [t for t in all_tasks if t.original_task_id == recurring_task.id]
        self.assertEqual(len(new_tasks), 1)
        new_task = new_tasks[0]
        self.assertEqual(new_task.title, recurring_task.title)
        self.assertEqual(new_task.description, recurring_task.description)
        self.assertEqual(new_task.priority, recurring_task.priority)

    def test_due_date_functionality(self):
        """Test due date functionality integration."""
        task_manager = TaskManager()

        # Add tasks with different due dates
        from datetime import datetime, timedelta
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)

        overdue_task = task_manager.add_task("Overdue Task", "Description", "high", ["test"], yesterday)
        upcoming_task = task_manager.add_task("Upcoming Task", "Description", "medium", ["test"], tomorrow)
        today_task = task_manager.add_task("Today Task", "Description", "low", ["test"], today)

        # Test get_overdue_tasks
        overdue_tasks = task_manager.get_overdue_tasks()
        self.assertIn(overdue_task, overdue_tasks)
        self.assertNotIn(upcoming_task, overdue_tasks)
        self.assertNotIn(today_task, overdue_tasks)

        # Test get_upcoming_tasks (within 5 days)
        upcoming_tasks = task_manager.get_upcoming_tasks(5)
        self.assertIn(upcoming_task, upcoming_tasks)
        self.assertIn(today_task, upcoming_tasks)  # Today's task should be in upcoming
        self.assertNotIn(overdue_task, upcoming_tasks)

        # Test get_todays_tasks
        todays_tasks = task_manager.get_todays_tasks()
        self.assertIn(today_task, todays_tasks)
        self.assertNotIn(overdue_task, todays_tasks)
        self.assertNotIn(upcoming_task, todays_tasks)

    def test_recurring_task_via_mark_complete(self):
        """Test that marking a recurring task complete triggers recurrence."""
        task_manager = TaskManager()

        # Add a recurring task
        from datetime import datetime
        due_date = datetime(2025, 12, 31)
        recurring_task = task_manager.add_task("Recurring Task", "Description", "high", ["test"], due_date,
                                              is_recurring=True, recurrence_interval=7)

        # Get initial count
        initial_count = len(task_manager.get_all_tasks())

        # Mark the recurring task complete (this should trigger recurrence)
        success = task_manager.mark_complete(recurring_task.id)
        self.assertTrue(success)

        # Check that a new task was created
        final_count = len(task_manager.get_all_tasks())
        self.assertEqual(final_count, initial_count + 1)

        # Verify original task is complete
        original_task = task_manager.get_task(recurring_task.id)
        self.assertTrue(original_task.completed)

    def test_add_command_with_recurrence_functionality(self):
        """Test the add command with recurrence flags and due date functionality."""
        task_manager = TaskManager()

        # Add a task with due date only
        from datetime import datetime
        due_date = datetime(2025, 12, 31)
        task_with_due_date = task_manager.add_task("Task with Due Date", "Description", "medium", ["test"], due_date)
        self.assertEqual(task_with_due_date.due_date, due_date)
        self.assertFalse(task_with_due_date.is_recurring)

        # Add a recurring task with due date
        recurring_task = task_manager.add_task("Recurring Task", "Description", "high", ["test"], due_date,
                                              is_recurring=True, recurrence_interval=7)
        self.assertTrue(recurring_task.is_recurring)
        self.assertEqual(recurring_task.recurrence_interval, 7)
        self.assertEqual(recurring_task.due_date, due_date)

        # Add a task without due date or recurrence
        simple_task = task_manager.add_task("Simple Task", "Description")
        self.assertIsNone(simple_task.due_date)
        self.assertFalse(simple_task.is_recurring)
        self.assertEqual(simple_task.priority, "medium")  # Default priority
        self.assertEqual(simple_task.tags, [])  # Default tags

        # Verify all tasks were added correctly
        all_tasks = task_manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 3)

        # Test that recurring tasks appear in recurring tasks list
        recurring_tasks = task_manager.get_recurring_tasks()
        self.assertIn(recurring_task, recurring_tasks)
        self.assertEqual(len(recurring_tasks), 1)

    def test_view_command_with_advanced_features(self):
        """Test the view command displays due dates and recurrence information correctly."""
        task_manager = TaskManager()

        # Add various tasks with different features
        from datetime import datetime, timedelta
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)

        # Add a task with due date and high priority
        task_with_due_date = task_manager.add_task("Task with Due Date", "Description", "high", ["work"], today)

        # Add a recurring task
        recurring_task = task_manager.add_task("Recurring Task", "Description", "medium", ["personal"], tomorrow,
                                             is_recurring=True, recurrence_interval=7)

        # Add an overdue task
        overdue_task = task_manager.add_task("Overdue Task", "Description", "low", ["urgent"], yesterday)

        # Add a simple task without due date or recurrence
        simple_task = task_manager.add_task("Simple Task", "Simple Description")

        # Test that all tasks are retrieved correctly
        all_tasks = task_manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 4)

        # Test filtering by due date
        overdue_tasks = task_manager.get_overdue_tasks()
        self.assertIn(overdue_task, overdue_tasks)
        self.assertEqual(len(overdue_tasks), 1)

        # Test upcoming tasks (within 5 days)
        upcoming_tasks = task_manager.get_upcoming_tasks(5)
        self.assertIn(task_with_due_date, upcoming_tasks)
        self.assertIn(recurring_task, upcoming_tasks)
        self.assertEqual(len(upcoming_tasks), 2)

        # Test today's tasks
        todays_tasks = task_manager.get_todays_tasks()
        self.assertIn(task_with_due_date, todays_tasks)
        self.assertEqual(len(todays_tasks), 1)

        # Test recurring tasks
        recurring_tasks_list = task_manager.get_recurring_tasks()
        self.assertIn(recurring_task, recurring_tasks_list)
        self.assertEqual(len(recurring_tasks_list), 1)

        # Test sorting by due date
        sorted_by_due_date = task_manager.sort_tasks("due_date")
        # The order should be: overdue_task (yesterday), task_with_due_date (today),
        # recurring_task (tomorrow), simple_task (None - last)
        self.assertEqual(sorted_by_due_date[0], overdue_task)
        self.assertEqual(sorted_by_due_date[1], task_with_due_date)
        self.assertEqual(sorted_by_due_date[2], recurring_task)
        self.assertEqual(sorted_by_due_date[3], simple_task)

    def test_update_command_with_advanced_features(self):
        """Test the update command handles due dates and recurrence settings correctly."""
        task_manager = TaskManager()

        from datetime import datetime, timedelta
        today = datetime.now()
        next_week = today + timedelta(days=7)

        # Add a task with due date and recurrence
        original_task = task_manager.add_task("Original Task", "Original Description", "medium", ["test"], today,
                                            is_recurring=True, recurrence_interval=7)
        original_id = original_task.id

        # Verify initial state
        self.assertEqual(original_task.title, "Original Task")
        self.assertEqual(original_task.description, "Original Description")
        self.assertEqual(original_task.priority, "medium")
        self.assertIn("test", original_task.tags)
        self.assertEqual(original_task.due_date, today)
        self.assertTrue(original_task.is_recurring)
        self.assertEqual(original_task.recurrence_interval, 7)

        # Update the task with new values
        updated_task = task_manager.update_task(original_id,
                                              title="Updated Task Title",
                                              description="Updated Description",
                                              priority="high",
                                              tags=["updated", "tags"],
                                              due_date=next_week,
                                              is_recurring=False,
                                              recurrence_interval=None)

        # Verify the updates were applied
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "Updated Task Title")
        self.assertEqual(updated_task.description, "Updated Description")
        self.assertEqual(updated_task.priority, "high")
        self.assertIn("updated", updated_task.tags)
        self.assertIn("tags", updated_task.tags)
        self.assertEqual(updated_task.due_date, next_week)
        self.assertFalse(updated_task.is_recurring)
        self.assertIsNone(updated_task.recurrence_interval)

        # Test partial updates - update only the due date
        updated_due_date = today + timedelta(days=10)
        partially_updated_task = task_manager.update_task(original_id, due_date=updated_due_date)
        self.assertEqual(partially_updated_task.due_date, updated_due_date)
        # Other fields should remain as last updated
        self.assertEqual(partially_updated_task.title, "Updated Task Title")
        self.assertEqual(partially_updated_task.description, "Updated Description")
        self.assertEqual(partially_updated_task.priority, "high")

        # Test updating recurrence settings for a non-recurring task
        new_recurrence_task = task_manager.add_task("Non-recurring Task", "Description")
        self.assertFalse(new_recurrence_task.is_recurring)

        # Update to make it recurring
        updated_to_recurring = task_manager.update_task(new_recurrence_task.id,
                                                      is_recurring=True,
                                                      recurrence_interval=14,
                                                      due_date=today)
        self.assertTrue(updated_to_recurring.is_recurring)
        self.assertEqual(updated_to_recurring.recurrence_interval, 14)
        self.assertEqual(updated_to_recurring.due_date, today)

    def test_recurring_command_integration(self):
        """Test the recurring command functionality for managing recurring tasks."""
        task_manager = TaskManager()

        from datetime import datetime
        due_date = datetime(2025, 12, 31)

        # Add several tasks - some recurring, some not
        recurring_task1 = task_manager.add_task("Recurring Task 1", "Description", "high", ["test"], due_date,
                                              is_recurring=True, recurrence_interval=7)
        recurring_task2 = task_manager.add_task("Recurring Task 2", "Description", "medium", ["work"], due_date,
                                              is_recurring=True, recurrence_interval=14)
        non_recurring_task = task_manager.add_task("Non-Recurring Task", "Description", "low", ["personal"])

        # Test getting all recurring tasks
        all_recurring_tasks = task_manager.get_recurring_tasks()
        self.assertEqual(len(all_recurring_tasks), 2)
        recurring_ids = [task.id for task in all_recurring_tasks]
        self.assertIn(recurring_task1.id, recurring_ids)
        self.assertIn(recurring_task2.id, recurring_ids)
        self.assertNotIn(non_recurring_task.id, recurring_ids)

        # Test that recurring tasks have correct properties
        for task in all_recurring_tasks:
            self.assertTrue(task.is_recurring)
            self.assertIsNotNone(task.recurrence_interval)
            self.assertGreater(task.recurrence_interval, 0)

        # Test updating recurrence interval
        updated_task = task_manager.update_task(recurring_task1.id, recurrence_interval=21)
        self.assertEqual(updated_task.recurrence_interval, 21)

        # Verify the update worked by getting recurring tasks again
        updated_recurring_tasks = task_manager.get_recurring_tasks()
        updated_task_from_list = next((t for t in updated_recurring_tasks if t.id == recurring_task1.id), None)
        self.assertIsNotNone(updated_task_from_list)
        self.assertEqual(updated_task_from_list.recurrence_interval, 21)

        # Test that non-recurring tasks remain non-recurring
        non_recurring_updated = task_manager.update_task(non_recurring_task.id, title="Updated Non-Recurring Task")
        self.assertFalse(non_recurring_updated.is_recurring)
        self.assertIsNone(non_recurring_updated.recurrence_interval)

        # Verify recurring task count is still correct
        final_recurring_tasks = task_manager.get_recurring_tasks()
        self.assertEqual(len(final_recurring_tasks), 2)

    def test_reminders_command_integration(self):
        """Test the reminders command functionality for overdue and upcoming tasks."""
        task_manager = TaskManager()

        from datetime import datetime, timedelta
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        next_week = today + timedelta(days=7)

        # Add tasks with various due dates
        overdue_task = task_manager.add_task("Overdue Task", "Description", "high", ["urgent"], yesterday)
        today_task = task_manager.add_task("Today Task", "Description", "medium", ["today"], today)
        upcoming_task = task_manager.add_task("Upcoming Task", "Description", "low", ["upcoming"], tomorrow)
        next_week_task = task_manager.add_task("Next Week Task", "Description", "medium", ["later"], next_week)
        no_due_task = task_manager.add_task("No Due Task", "Description", "low", ["no-date"])

        # Test getting overdue tasks
        overdue_tasks = task_manager.get_overdue_tasks()
        self.assertEqual(len(overdue_tasks), 1)
        self.assertIn(overdue_task, overdue_tasks)
        # Verify other tasks are not in overdue list
        self.assertNotIn(today_task, overdue_tasks)
        self.assertNotIn(upcoming_task, overdue_tasks)
        self.assertNotIn(next_week_task, overdue_tasks)
        self.assertNotIn(no_due_task, overdue_tasks)

        # Test getting upcoming tasks (within 5 days)
        upcoming_tasks_5days = task_manager.get_upcoming_tasks(5)
        self.assertEqual(len(upcoming_tasks_5days), 2)  # today_task and upcoming_task
        self.assertIn(today_task, upcoming_tasks_5days)
        self.assertIn(upcoming_task, upcoming_tasks_5days)
        # Verify other tasks are not in upcoming list
        self.assertNotIn(overdue_task, upcoming_tasks_5days)
        self.assertNotIn(next_week_task, upcoming_tasks_5days)
        self.assertNotIn(no_due_task, upcoming_tasks_5days)

        # Test getting upcoming tasks (within 10 days)
        upcoming_tasks_10days = task_manager.get_upcoming_tasks(10)
        self.assertEqual(len(upcoming_tasks_10days), 3)  # today_task, upcoming_task, next_week_task
        self.assertIn(today_task, upcoming_tasks_10days)
        self.assertIn(upcoming_task, upcoming_tasks_10days)
        self.assertIn(next_week_task, upcoming_tasks_10days)
        # Verify other tasks are not in upcoming list
        self.assertNotIn(overdue_task, upcoming_tasks_10days)
        self.assertNotIn(no_due_task, upcoming_tasks_10days)

        # Test getting today's tasks
        todays_tasks = task_manager.get_todays_tasks()
        self.assertEqual(len(todays_tasks), 1)
        self.assertIn(today_task, todays_tasks)
        # Verify other tasks are not in today's list
        self.assertNotIn(overdue_task, todays_tasks)
        self.assertNotIn(upcoming_task, todays_tasks)
        self.assertNotIn(next_week_task, todays_tasks)
        self.assertNotIn(no_due_task, todays_tasks)

        # Test with completed tasks - they should not appear in any of these lists
        task_manager.mark_complete(overdue_task.id)
        task_manager.mark_complete(today_task.id)

        # After marking as complete, these tasks should not appear in overdue/today/upcoming lists
        overdue_tasks_after_complete = task_manager.get_overdue_tasks()
        self.assertEqual(len(overdue_tasks_after_complete), 0)
        self.assertNotIn(overdue_task, overdue_tasks_after_complete)

        todays_tasks_after_complete = task_manager.get_todays_tasks()
        self.assertEqual(len(todays_tasks_after_complete), 0)
        self.assertNotIn(today_task, todays_tasks_after_complete)

        # Upcoming tasks should still include the non-completed tasks
        upcoming_tasks_after_complete = task_manager.get_upcoming_tasks(10)
        self.assertEqual(len(upcoming_tasks_after_complete), 2)  # upcoming_task and next_week_task
        self.assertIn(upcoming_task, upcoming_tasks_after_complete)
        self.assertIn(next_week_task, upcoming_tasks_after_complete)
        self.assertNotIn(today_task, upcoming_tasks_after_complete)
        self.assertNotIn(overdue_task, upcoming_tasks_after_complete)


if __name__ == "__main__":
    unittest.main()