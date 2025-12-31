"""
Interactive Command-line interface for the Todo CLI application.
Provides interactive menu for adding, viewing, updating, and managing tasks.
"""

import sys
import os
from datetime import datetime, date

# Add the project root to the path to allow absolute imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.task_manager import TaskManager


def display_menu():
    """Display the interactive menu options."""
    print("\n======= TODO APPLICATION =======")
    print("           MAIN MENU")
    print("=" * 32)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task Complete")
    print("4. Mark Task Incomplete")
    print("5. Update Task")
    print("6. Delete Task")
    print("7. Search Tasks")
    print("8. Filter Tasks")
    print("9. Sort Tasks")
    print("10. Manage Recurring Tasks")
    print("11. View Reminders")
    print("0. Exit")
    print("=" * 32)


def get_user_input(prompt: str) -> str:
    """Get user input with proper handling."""
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\n\nExiting application...")
        return "0"


def handle_add_task(task_manager: TaskManager):
    """Handle adding a new task interactively."""
    print("\n--- ADD NEW TASK ---")
    title = get_user_input("Enter task title: ")

    if not title:
        print("Error: Title cannot be empty!")
        return

    description = get_user_input("Enter task description (optional, press Enter to skip): ")
    if description == "":
        description = None

    # Get priority input
    print("Enter priority (high/medium/low) [default: medium]: ", end="")
    priority = get_user_input("")
    if priority == "":
        priority = "medium"

    # Get tags input
    tags_input = get_user_input("Enter tags separated by commas (optional, press Enter to skip): ")
    tags = []
    if tags_input:
        # Split by comma and strip whitespace
        tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

    # Get due date input
    due_date_input = get_user_input("Enter due date (YYYY-MM-DD format, optional, press Enter to skip): ")
    due_date = None
    if due_date_input:
        try:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
        except ValueError:
            print(f"Invalid date format: {due_date_input}. Using no due date.")
            due_date = None

    # Get recurring task input
    is_recurring_input = get_user_input("Should this task repeat? (y/n) [default: n]: ").lower()
    is_recurring = is_recurring_input in ['y', 'yes']

    recurrence_interval = None
    if is_recurring:
        recurrence_input = get_user_input("Enter recurrence interval in days (e.g., 1 for daily, 7 for weekly): ")
        try:
            recurrence_interval = int(recurrence_input)
            if recurrence_interval <= 0:
                print("Invalid interval. Setting to 7 days.")
                recurrence_interval = 7
        except ValueError:
            print("Invalid interval. Setting to 7 days.")
            recurrence_interval = 7

    try:
        task = task_manager.add_task(title, description, priority, tags, due_date, is_recurring, recurrence_interval)
        print(f"✓ Task added successfully with ID: {task.id}")
        due_date_str = f" (due: {due_date.strftime('%Y-%m-%d')})" if due_date else " (no due date)"
        recurring_str = f", Recurring: every {recurrence_interval} days" if is_recurring else ""
        print(f"  Priority: {task.priority}, Tags: {', '.join(task.tags) if task.tags else 'None'}{due_date_str}{recurring_str}")
    except ValueError as e:
        print(f"✗ Error adding task: {e}")


def handle_view_tasks(task_manager: TaskManager):
    """Handle viewing all tasks."""
    print("\n--- VIEW ALL TASKS ---")
    tasks = task_manager.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print(f"\n{'ID':<3} {'Status':<8} {'Prio':<6} {'Title':<20} {'Due Date':<15} {'Recurring':<10} {'Tags':<15} {'Description'}")
    print("-" * 115)
    for task in tasks:
        status = "✓ Done" if task.completed else "○ Todo"
        priority = f"({task.priority[0].upper()})"  # H for high, M for medium, L for low
        title = task.title[:18] + ".." if len(task.title) > 18 else task.title

        # Check for overdue and upcoming tasks
        due_date_str = ""
        if task.due_date:
            due_date_str = task.due_date.strftime('%Y-%m-%d')
            # Check if task is overdue (not completed and due date is in the past)
            today = datetime.now().date()
            task_due_date = task.due_date.date()
            if not task.completed and task_due_date < today:
                due_date_str += " [OVERDUE]"
            elif not task.completed and task_due_date == today:
                due_date_str += " [TODAY]"
            elif not task.completed and task_due_date > today:
                # Show how many days away
                days_until = (task_due_date - today).days
                due_date_str += f" [in {days_until}d]"

        recurring = "Yes" if task.is_recurring else "No"
        tags = ', '.join(task.tags[:2]) + ".." if len(task.tags) > 2 else ', '.join(task.tags)  # Show first 2 tags if more
        description = task.description[:25] + ".." if len(task.description) > 25 else task.description
        print(f"{task.id:<3} {status:<8} {priority:<6} {title:<20} {due_date_str:<15} {recurring:<10} {tags:<15} {description}")
    print("-" * 115)
    print(f"Total tasks: {len(tasks)}")


def handle_mark_complete(task_manager: TaskManager):
    """Handle marking a task as complete."""
    print("\n--- MARK TASK COMPLETE ---")
    task_id_str = get_user_input("Enter task ID to mark complete: ")

    try:
        task_id = int(task_id_str)
    except ValueError:
        print("✗ Error: Please enter a valid task ID (number)")
        return

    success = task_manager.mark_complete(task_id)
    if success:
        print(f"✓ Task {task_id} marked as complete")
    else:
        print(f"✗ Error: Task with ID {task_id} not found")


def handle_mark_incomplete(task_manager: TaskManager):
    """Handle marking a task as incomplete."""
    print("\n--- MARK TASK INCOMPLETE ---")
    task_id_str = get_user_input("Enter task ID to mark incomplete: ")

    try:
        task_id = int(task_id_str)
    except ValueError:
        print("✗ Error: Please enter a valid task ID (number)")
        return

    success = task_manager.mark_incomplete(task_id)
    if success:
        print(f"✓ Task {task_id} marked as incomplete")
    else:
        print(f"✗ Error: Task with ID {task_id} not found")


def handle_update_task(task_manager: TaskManager):
    """Handle updating a task."""
    print("\n--- UPDATE TASK ---")
    task_id_str = get_user_input("Enter task ID to update: ")

    try:
        task_id = int(task_id_str)
    except ValueError:
        print("✗ Error: Please enter a valid task ID (number)")
        return

    # Check if task exists first
    task = task_manager.get_task(task_id)
    if not task:
        print(f"✗ Error: Task with ID {task_id} not found")
        return

    print(f"Current task: {task.title}")
    print(f"Current description: {task.description}")
    print(f"Current priority: {task.priority}")
    print(f"Current tags: {', '.join(task.tags) if task.tags else 'None'}")
    print(f"Current due date: {task.due_date.strftime('%Y-%m-%d') if task.due_date else 'None'}")

    new_title = get_user_input("Enter new title (press Enter to keep current): ")
    if new_title == "":
        new_title = None

    new_description = get_user_input("Enter new description (press Enter to keep current): ")
    if new_description == "":
        new_description = None

    # Get new priority
    print(f"Enter new priority (high/medium/low) [current: {task.priority}, press Enter to keep current]: ", end="")
    new_priority = get_user_input("")
    if new_priority == "":
        new_priority = None  # Don't update if empty

    # Get new tags
    new_tags_input = get_user_input(f"Enter new tags separated by commas [current: {', '.join(task.tags) if task.tags else 'None'}, press Enter to keep current]: ")
    new_tags = None
    if new_tags_input == "":
        new_tags = None  # Don't update if empty
    else:
        # Split by comma and strip whitespace
        new_tags = [tag.strip() for tag in new_tags_input.split(',') if tag.strip()]

    # Get new due date
    new_due_date_input = get_user_input(f"Enter new due date (YYYY-MM-DD format) [current: {task.due_date.strftime('%Y-%m-%d') if task.due_date else 'None'}, press Enter to keep current]: ")
    new_due_date = None
    if new_due_date_input == "":
        new_due_date = None  # Don't update if empty
    elif new_due_date_input.lower() == "none":
        new_due_date = None  # Allow clearing the due date
    else:
        try:
            new_due_date = datetime.strptime(new_due_date_input, "%Y-%m-%d")
        except ValueError:
            print(f"Invalid date format: {new_due_date_input}. Due date not changed.")
            new_due_date = None

    # Get new recurrence settings
    print(f"Current recurring status: {'Yes' if task.is_recurring else 'No'} (every {task.recurrence_interval} days)" if task.is_recurring else "Current recurring status: No")
    new_is_recurring_input = get_user_input("Update recurring status? (y/n, press Enter to keep current): ").lower()
    new_is_recurring = None
    if new_is_recurring_input == "":
        new_is_recurring = None  # Don't update
    elif new_is_recurring_input in ['y', 'yes']:
        new_is_recurring = True
    elif new_is_recurring_input in ['n', 'no']:
        new_is_recurring = False

    new_recurrence_interval = None
    if new_is_recurring is True:
        interval_input = get_user_input(f"Enter new recurrence interval in days [current: {task.recurrence_interval}, press Enter to keep current]: ")
        if interval_input == "":
            new_recurrence_interval = None  # Keep current
        else:
            try:
                new_interval = int(interval_input)
                if new_interval > 0:
                    new_recurrence_interval = new_interval
                else:
                    print("Invalid interval. Keeping current interval.")
                    new_recurrence_interval = None
            except ValueError:
                print("Invalid interval. Keeping current interval.")
                new_recurrence_interval = None
    elif new_is_recurring is False:
        # If disabling recurrence, we don't need to update the interval
        new_recurrence_interval = None

    # If all are unchanged, don't update
    if (new_title is None and new_description is None and new_priority is None and
        new_tags is None and new_due_date is None and new_is_recurring is None and
        new_recurrence_interval is None):
        print("No changes made.")
        return

    try:
        updated_task = task_manager.update_task(task_id, new_title, new_description, new_priority, new_tags, new_due_date,
                                               new_is_recurring, new_recurrence_interval)
        if updated_task:
            print(f"✓ Task {task_id} updated successfully")
            due_date_str = f" (due: {updated_task.due_date.strftime('%Y-%m-%d')})" if updated_task.due_date else " (no due date)"
            recurring_str = f", Recurring: every {updated_task.recurrence_interval} days" if updated_task.is_recurring else ", Not recurring"
            print(f"  New priority: {updated_task.priority}, New tags: {', '.join(updated_task.tags) if updated_task.tags else 'None'}{due_date_str}{recurring_str}")
        else:
            print(f"✗ Error: Task with ID {task_id} not found")
    except ValueError as e:
        print(f"✗ Error updating task: {e}")


def handle_delete_task(task_manager: TaskManager):
    """Handle deleting a task."""
    print("\n--- DELETE TASK ---")
    task_id_str = get_user_input("Enter task ID to delete: ")

    try:
        task_id = int(task_id_str)
    except ValueError:
        print("✗ Error: Please enter a valid task ID (number)")
        return

    success = task_manager.delete_task(task_id)
    if success:
        print(f"✓ Task {task_id} deleted successfully")
    else:
        print(f"✗ Error: Task with ID {task_id} not found")


def handle_search_tasks(task_manager: TaskManager):
    """Handle searching tasks by keyword."""
    print("\n--- SEARCH TASKS ---")
    keyword = get_user_input("Enter keyword to search for: ")

    if not keyword:
        print("No keyword provided. Search cancelled.")
        return

    tasks = task_manager.search_tasks(keyword)

    if not tasks:
        print(f"No tasks found containing '{keyword}'.")
        return

    print(f"\nFound {len(tasks)} task(s) containing '{keyword}':")
    print(f"\n{'ID':<3} {'Status':<8} {'Prio':<6} {'Title':<20} {'Due Date':<15} {'Tags':<15} {'Description'}")
    print("-" * 105)
    for task in tasks:
        status = "✓ Done" if task.completed else "○ Todo"
        priority = f"({task.priority[0].upper()})"  # H for high, M for medium, L for low
        title = task.title[:18] + ".." if len(task.title) > 18 else task.title

        # Check for overdue and upcoming tasks
        due_date_str = ""
        if task.due_date:
            due_date_str = task.due_date.strftime('%Y-%m-%d')
            # Check if task is overdue (not completed and due date is in the past)
            today = datetime.now().date()
            task_due_date = task.due_date.date()
            if not task.completed and task_due_date < today:
                due_date_str += " [OVERDUE]"
            elif not task.completed and task_due_date == today:
                due_date_str += " [TODAY]"
            elif not task.completed and task_due_date > today:
                # Show how many days away
                days_until = (task_due_date - today).days
                due_date_str += f" [in {days_until}d]"

        tags = ', '.join(task.tags[:2]) + ".." if len(task.tags) > 2 else ', '.join(task.tags)  # Show first 2 tags if more
        description = task.description[:25] + ".." if len(task.description) > 25 else task.description
        print(f"{task.id:<3} {status:<8} {priority:<6} {title:<20} {due_date_str:<15} {tags:<15} {description}")
    print("-" * 105)


def handle_filter_tasks(task_manager: TaskManager):
    """Handle filtering tasks by various criteria."""
    print("\n--- FILTER TASKS ---")

    # Get filter options from user
    print("Filter options (press Enter to skip each filter):")

    # Filter by status
    status_input = get_user_input("Filter by status (complete/incomplete) [c/i]: ").lower()
    status = None
    if status_input == 'c' or status_input == 'complete':
        status = True
    elif status_input == 'i' or status_input == 'incomplete':
        status = False

    # Filter by priority
    priority = get_user_input("Filter by priority (high/medium/low): ").lower()
    if priority == "":
        priority = None
    elif priority not in ["high", "medium", "low"]:
        print(f"Invalid priority '{priority}'. Skipping priority filter.")
        priority = None

    # Filter by due date
    due_date_input = get_user_input("Filter by due date (YYYY-MM-DD format, optional, press Enter to skip): ")
    due_date = None
    if due_date_input:
        try:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
        except ValueError:
            print(f"Invalid date format: {due_date_input}. Skipping due date filter.")
            due_date = None

    # Perform filtering
    tasks = task_manager.filter_tasks(status=status, priority=priority, due_date=due_date)

    if not tasks:
        print("No tasks match the filter criteria.")
        return

    print(f"\nFound {len(tasks)} task(s) matching filter criteria:")
    print(f"\n{'ID':<3} {'Status':<8} {'Prio':<6} {'Title':<20} {'Due Date':<15} {'Tags':<15} {'Description'}")
    print("-" * 105)
    for task in tasks:
        status = "✓ Done" if task.completed else "○ Todo"
        priority = f"({task.priority[0].upper()})"  # H for high, M for medium, L for low
        title = task.title[:18] + ".." if len(task.title) > 18 else task.title

        # Check for overdue and upcoming tasks
        due_date_str = ""
        if task.due_date:
            due_date_str = task.due_date.strftime('%Y-%m-%d')
            # Check if task is overdue (not completed and due date is in the past)
            today = datetime.now().date()
            task_due_date = task.due_date.date()
            if not task.completed and task_due_date < today:
                due_date_str += " [OVERDUE]"
            elif not task.completed and task_due_date == today:
                due_date_str += " [TODAY]"
            elif not task.completed and task_due_date > today:
                # Show how many days away
                days_until = (task_due_date - today).days
                due_date_str += f" [in {days_until}d]"

        tags = ', '.join(task.tags[:2]) + ".." if len(task.tags) > 2 else ', '.join(task.tags)  # Show first 2 tags if more
        description = task.description[:25] + ".." if len(task.description) > 25 else task.description
        print(f"{task.id:<3} {status:<8} {priority:<6} {title:<20} {due_date_str:<15} {tags:<15} {description}")
    print("-" * 105)


def handle_sort_tasks(task_manager: TaskManager):
    """Handle sorting tasks by various criteria."""
    print("\n--- SORT TASKS ---")

    print("Sort options:")
    print("1. By title (alphabetical)")
    print("2. By priority (high to low)")
    print("3. By due date (earliest first)")

    choice = get_user_input("Choose sort option (1-3): ")

    sort_by = None
    if choice == "1":
        sort_by = "title"
    elif choice == "2":
        sort_by = "priority"
    elif choice == "3":
        sort_by = "due_date"
    else:
        print("Invalid choice. Sorting cancelled.")
        return

    tasks = task_manager.sort_tasks(sort_by)

    if not tasks:
        print("No tasks to display.")
        return

    print(f"\nTasks sorted by {sort_by}:")
    print(f"\n{'ID':<3} {'Status':<8} {'Prio':<6} {'Title':<20} {'Due Date':<15} {'Tags':<15} {'Description'}")
    print("-" * 105)
    for task in tasks:
        status = "✓ Done" if task.completed else "○ Todo"
        priority = f"({task.priority[0].upper()})"  # H for high, M for medium, L for low
        title = task.title[:18] + ".." if len(task.title) > 18 else task.title

        # Check for overdue and upcoming tasks
        due_date_str = ""
        if task.due_date:
            due_date_str = task.due_date.strftime('%Y-%m-%d')
            # Check if task is overdue (not completed and due date is in the past)
            today = datetime.now().date()
            task_due_date = task.due_date.date()
            if not task.completed and task_due_date < today:
                due_date_str += " [OVERDUE]"
            elif not task.completed and task_due_date == today:
                due_date_str += " [TODAY]"
            elif not task.completed and task_due_date > today:
                # Show how many days away
                days_until = (task_due_date - today).days
                due_date_str += f" [in {days_until}d]"

        tags = ', '.join(task.tags[:2]) + ".." if len(task.tags) > 2 else ', '.join(task.tags)  # Show first 2 tags if more
        description = task.description[:25] + ".." if len(task.description) > 25 else task.description
        print(f"{task.id:<3} {status:<8} {priority:<6} {title:<20} {due_date_str:<15} {tags:<15} {description}")
    print("-" * 105)


def handle_recurring_tasks(task_manager: TaskManager):
    """Handle managing recurring tasks."""
    print("\n--- MANAGE RECURRING TASKS ---")
    print("Options:")
    print("1. List all recurring tasks")
    print("2. Modify recurrence settings for a task")
    print("3. Disable recurrence for a task")

    choice = get_user_input("Choose an option (1-3): ")

    if choice == "1":
        recurring_tasks = task_manager.get_recurring_tasks()

        if not recurring_tasks:
            print("No recurring tasks found.")
            return

        print(f"\n{'ID':<3} {'Status':<8} {'Prio':<6} {'Title':<20} {'Due Date':<15} {'Interval':<10} {'Tags':<15} {'Description'}")
        print("-" * 115)
        for task in recurring_tasks:
            status = "✓ Done" if task.completed else "○ Todo"
            priority = f"({task.priority[0].upper()})"  # H for high, M for medium, L for low
            title = task.title[:18] + ".." if len(task.title) > 18 else task.title

            # Check for overdue and upcoming tasks
            due_date_str = ""
            if task.due_date:
                due_date_str = task.due_date.strftime('%Y-%m-%d')
                # Check if task is overdue (not completed and due date is in the past)
                today = datetime.now().date()
                task_due_date = task.due_date.date()
                if not task.completed and task_due_date < today:
                    due_date_str += " [OVERDUE]"
                elif not task.completed and task_due_date == today:
                    due_date_str += " [TODAY]"
                elif not task.completed and task_due_date > today:
                    # Show how many days away
                    days_until = (task_due_date - today).days
                    due_date_str += f" [in {days_until}d]"

            interval = str(task.recurrence_interval) if task.recurrence_interval else "N/A"
            tags = ', '.join(task.tags[:2]) + ".." if len(task.tags) > 2 else ', '.join(task.tags)  # Show first 2 tags if more
            description = task.description[:25] + ".." if len(task.description) > 25 else task.description
            print(f"{task.id:<3} {status:<8} {priority:<6} {title:<20} {due_date_str:<15} {interval:<10} {tags:<15} {description}")
        print("-" * 115)
        print(f"Total recurring tasks: {len(recurring_tasks)}")

    elif choice == "2":
        task_id_str = get_user_input("Enter task ID to modify recurrence settings: ")
        try:
            task_id = int(task_id_str)
        except ValueError:
            print("✗ Error: Please enter a valid task ID (number)")
            return

        task = task_manager.get_task(task_id)
        if not task:
            print(f"✗ Error: Task with ID {task_id} not found")
            return

        if not task.is_recurring:
            print(f"✗ Error: Task {task_id} is not a recurring task")
            return

        print(f"Current task: {task.title}")
        print(f"Current interval: {task.recurrence_interval} days")

        new_interval_str = get_user_input("Enter new interval in days: ")
        try:
            new_interval = int(new_interval_str)
            if new_interval <= 0:
                print("Invalid interval. Must be positive.")
                return
        except ValueError:
            print("Invalid interval. Must be a number.")
            return

        # Update the task's recurrence interval
        try:
            updated_task = task_manager.update_task(task_id, recurrence_interval=new_interval)
            if updated_task:
                print(f"✓ Recurrence interval updated to {new_interval} days for task {task_id}")
            else:
                print(f"✗ Error: Could not update task {task_id}")
        except ValueError as e:
            print(f"✗ Error updating recurrence interval: {e}")

    elif choice == "3":
        task_id_str = get_user_input("Enter task ID to disable recurrence: ")
        try:
            task_id = int(task_id_str)
        except ValueError:
            print("✗ Error: Please enter a valid task ID (number)")
            return

        task = task_manager.get_task(task_id)
        if not task:
            print(f"✗ Error: Task with ID {task_id} not found")
            return

        if not task.is_recurring:
            print(f"✗ Error: Task {task_id} is not a recurring task")
            return

        # Disable recurrence by setting is_recurring to False
        try:
            updated_task = task_manager.update_task(task_id, is_recurring=False)
            if updated_task:
                print(f"✓ Recurrence disabled for task {task_id}")
            else:
                print(f"✗ Error: Could not update task {task_id}")
        except ValueError as e:
            print(f"✗ Error disabling recurrence: {e}")

    else:
        print("✗ Invalid choice. Please enter 1, 2, or 3.")


def handle_reminders(task_manager: TaskManager):
    """Handle viewing reminders for overdue and upcoming tasks."""
    print("\n--- VIEW REMINDERS ---")
    print("Options:")
    print("1. View overdue tasks")
    print("2. View upcoming tasks")
    print("3. View today's tasks")

    choice = get_user_input("Choose an option (1-3): ")

    if choice == "1":
        overdue_tasks = task_manager.get_overdue_tasks()

        if not overdue_tasks:
            print("No overdue tasks found.")
            return

        print(f"\n{'ID':<3} {'Status':<8} {'Prio':<6} {'Title':<20} {'Due Date':<15} {'Tags':<15} {'Description'}")
        print("-" * 105)
        for task in overdue_tasks:
            status = "✓ Done" if task.completed else "○ Todo"
            priority = f"({task.priority[0].upper()})"  # H for high, M for medium, L for low
            title = task.title[:18] + ".." if len(task.title) > 18 else task.title

            # Check for overdue and upcoming tasks (for overdue tasks, we already know they're overdue)
            due_date_str = ""
            if task.due_date:
                due_date_str = task.due_date.strftime('%Y-%m-%d')
                # Since these are overdue tasks, add the [OVERDUE] indicator
                due_date_str += " [OVERDUE]"

            tags = ', '.join(task.tags[:2]) + ".." if len(task.tags) > 2 else ', '.join(task.tags)  # Show first 2 tags if more
            description = task.description[:25] + ".." if len(task.description) > 25 else task.description
            print(f"{task.id:<3} {status:<8} {priority:<6} {title:<20} {due_date_str:<15} {tags:<15} {description}")
        print("-" * 105)
        print(f"Total overdue tasks: {len(overdue_tasks)}")

    elif choice == "2":
        days_ahead_str = get_user_input("How many days ahead to look for upcoming tasks? (e.g., 7 for next week): ")
        try:
            days_ahead = int(days_ahead_str)
            if days_ahead <= 0:
                print("Invalid number of days. Must be positive.")
                return
        except ValueError:
            print("Invalid number of days. Must be a number.")
            return

        upcoming_tasks = task_manager.get_upcoming_tasks(days_ahead)

        if not upcoming_tasks:
            print(f"No upcoming tasks within the next {days_ahead} days.")
            return

        print(f"\n{'ID':<3} {'Status':<8} {'Prio':<6} {'Title':<20} {'Due Date':<15} {'Tags':<15} {'Description'}")
        print("-" * 105)
        for task in upcoming_tasks:
            status = "✓ Done" if task.completed else "○ Todo"
            priority = f"({task.priority[0].upper()})"  # H for high, M for medium, L for low
            title = task.title[:18] + ".." if len(task.title) > 18 else task.title

            # Check for overdue and upcoming tasks (for upcoming tasks)
            due_date_str = ""
            if task.due_date:
                due_date_str = task.due_date.strftime('%Y-%m-%d')
                # Check if task is due today
                from datetime import datetime
                today = datetime.now().date()
                task_due_date = task.due_date.date()
                if not task.completed and task_due_date == today:
                    due_date_str += " [TODAY]"
                elif not task.completed and task_due_date > today:
                    # Show how many days away
                    days_until = (task_due_date - today).days
                    due_date_str += f" [in {days_until}d]"

            tags = ', '.join(task.tags[:2]) + ".." if len(task.tags) > 2 else ', '.join(task.tags)  # Show first 2 tags if more
            description = task.description[:25] + ".." if len(task.description) > 25 else task.description
            print(f"{task.id:<3} {status:<8} {priority:<6} {title:<20} {due_date_str:<15} {tags:<15} {description}")
        print("-" * 105)
        print(f"Total upcoming tasks: {len(upcoming_tasks)}")

    elif choice == "3":
        todays_tasks = task_manager.get_todays_tasks()

        if not todays_tasks:
            print("No tasks due today.")
            return

        print(f"\n{'ID':<3} {'Status':<8} {'Prio':<6} {'Title':<20} {'Due Date':<15} {'Tags':<15} {'Description'}")
        print("-" * 105)
        for task in todays_tasks:
            status = "✓ Done" if task.completed else "○ Todo"
            priority = f"({task.priority[0].upper()})"  # H for high, M for medium, L for low
            title = task.title[:18] + ".." if len(task.title) > 18 else task.title

            # Check for overdue and upcoming tasks (for today's tasks, we know they're due today)
            due_date_str = ""
            if task.due_date:
                due_date_str = task.due_date.strftime('%Y-%m-%d')
                # Add TODAY indicator for today's tasks
                due_date_str += " [TODAY]"

            tags = ', '.join(task.tags[:2]) + ".." if len(task.tags) > 2 else ', '.join(task.tags)  # Show first 2 tags if more
            description = task.description[:25] + ".." if len(task.description) > 25 else task.description
            print(f"{task.id:<3} {status:<8} {priority:<6} {title:<20} {due_date_str:<15} {tags:<15} {description}")
        print("-" * 105)
        print(f"Total tasks due today: {len(todays_tasks)}")

    else:
        print("✗ Invalid choice. Please enter 1, 2, or 3.")


def main():
    """Main entry point for the interactive CLI application."""
    print("Welcome to the Todo CLI Application!")
    print("Initializing task manager...")

    # Initialize task manager ONCE at the start of the program
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = get_user_input("\nEnter your choice (0-11): ")

        if choice == "0":
            print("\nThank you for using Todo CLI Application!")
            print("Goodbye! 👋")
            break
        elif choice == "1":
            handle_add_task(task_manager)
        elif choice == "2":
            handle_view_tasks(task_manager)
        elif choice == "3":
            handle_mark_complete(task_manager)
        elif choice == "4":
            handle_mark_incomplete(task_manager)
        elif choice == "5":
            handle_update_task(task_manager)
        elif choice == "6":
            handle_delete_task(task_manager)
        elif choice == "7":
            handle_search_tasks(task_manager)
        elif choice == "8":
            handle_filter_tasks(task_manager)
        elif choice == "9":
            handle_sort_tasks(task_manager)
        elif choice == "10":
            handle_recurring_tasks(task_manager)
        elif choice == "11":
            handle_reminders(task_manager)
        else:
            print("✗ Invalid choice. Please enter a number between 0-11.")

        if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()