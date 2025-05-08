"""
three_tier.py

A self-contained demonstration of the 3-Tier Architecture pattern in Python. 
This would normally be devided among separate files, but for simplicity 
of demonstration, we have put them all in one file.

Tiers:
1. Data Layer        - Handles data storage and retrieval
2. Logic Layer       - Applies validation and business rules
3. Presentation Layer - Handles user interaction (CLI)
"""

"""
Data Layer: Handles storage and retrieval of task data.
In a real-world app, this might interface with a database or file system.
"""
from typing import List

# Simulated in-memory "database"
_tasks_db: List[str] = []

def save_task(task: str) -> None:
    """
    Save a task to the data store.

    Args:
        task (str): The task to save.
    """
    _tasks_db.append(task)

def fetch_all_tasks() -> List[str]:
    """
    Retrieve all stored tasks.

    Returns:
        List[str]: A list of task strings.
    """
    return list(_tasks_db)


"""
Logic Layer: Implements business rules for the task manager.
Handles validation and processing before passing data to the data layer.
"""
def add_task(task: str) -> None:
    """
    Add a task after validation.

    Args:
        task (str): The task to add.

    Raises:
        ValueError: If the task is empty or invalid.
    """
    task = task.strip()
    if not task:
        raise ValueError("Task cannot be empty.")
    save_task(task)

def get_all_tasks() -> List[str]:
    """
    Retrieve all tasks.

    Returns:
        List[str]: A list of task strings.
    """
    return fetch_all_tasks()


"""
Presentation Layer: Handles all user interaction (input/output).
Calls the logic layer to perform operations.
"""
def show_menu() -> None:
    """Display the main menu."""
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

def run_cli() -> None:
    """Main CLI loop."""
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter the task: ")
            try:
                add_task(task)
                print("✅ Task added.")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            tasks = get_all_tasks()
            if not tasks:
                print("📭 No tasks found.")
            else:
                print("\n📋 Task List:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")


# =======================
# 🚀 ENTRY POINT
# =======================
if __name__ == "__main__":
    run_cli()
