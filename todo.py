import os

FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks from a text file if available."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    """Save current tasks to the text file."""
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

def view_tasks(tasks):
    """Display a numbered, easy-to-read task list."""
    if not tasks:
        print("\nYour to-do list is currently empty.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("-" * 18)

def add_task(tasks):
    """Add a new task to the list."""
    task = input("\nEnter task description: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task description cannot be empty.")

def remove_task(tasks):
    """Remove a task by its list number."""
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("\nEnter the number of the task to remove: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                save_tasks(tasks)
                print(f"Task '{removed}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do List CLI App ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    main()
