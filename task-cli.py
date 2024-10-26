from argparse import ArgumentParser
from datetime import datetime
import json
import os

# File where tasks are stored
TASKS_FILE = "tasks.json"

# Load tasks from the JSON file or create the file if it doesn't exist
def load_tasks():
    # Create an empty tasks file if it doesn't exist
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            json.dump([], file)

    # Load and return tasks from the JSON file
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

# Save the list of tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1 # Generate new task ID
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

# Update an existing task's description
def update_task(task_id, new_description):
    tasks = load_tasks()
    # Search for the task with the specified ID
    for task in tasks:
        if task["id"] == task_id:
            # Update the description and updatedAt timestamp
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) updated successfully")
            return
    print(f"Task (ID: {task_id}) not found")

# Delete a task and ajust IDs of following tasks
def delete_task(task_id):
    tasks = load_tasks()
    # Find and remove the task with the specified ID
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            # Update IDs of tasks that come after the deleted task
            for task in tasks:
                if task["id"] > task_id:
                    task["id"] = int(task["id"]) - 1
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) deleted successfully")
            break
    else:
        print(f"Task (ID: {task_id}) not found")

# Mark a task as "in-progress" or "done"  
def mark_task(task_id, status):
    tasks = load_tasks()
    # Find the task with the specified ID
    for task in tasks:
        if task["id"] == task_id:
            # Update the status and updatedAt timestamp
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) marked as in progress")
            return
    print(f"Task (ID: {task_id}) not found")

# List all tasks, optionally filtered by status
def list_tasks(status=None):
    tasks = load_tasks()
    found_task = False # Track if any tasks have been found

    print("List of Tasks:")

    # Print each task, filtering by status if specified
    for task in tasks:
        if status is None or task["status"] == status:
            print(f"ID: {task['id']} - {task['description']} ({task['status']})")
            found_task = True

    # Print a message if no task was found
    if not found_task:
        if status:
            print(f"No task with '{status}' found")
        else:
            print("No task found")

# Main function that sets up the CLI arg prasing
def main():
    parser = ArgumentParser(description="CLI app to track your tasks and manage your to-do list.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Define commands and arguments
    
    # Add a new task
    parser_add = subparsers.add_parser("add", help="Adds a new task")
    parser_add.add_argument("description", type=str, help="Description of the task to add")

    # Update an existing task's description
    parser_update = subparsers.add_parser("update", help="Change the description of an existing task")
    parser_update.add_argument("id", type=int, help="The id of the task to update")
    parser_update.add_argument("description", type=str, help="New description of the task to update")

    # Delete a task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="The id of the task to delete")

    # Mark a task as "in-progress"
    parser_mark_in_progress = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
    parser_mark_in_progress.add_argument("id", type=int, help="The id of the task to mark as in progress")

    # Mark a task as "done"
    parser_mark_done = subparsers.add_parser("mark-done", help="Mark a task as done")
    parser_mark_done.add_argument("id", type=int, help="The id of the task to mark as done")

    # List all tasks, optionally filtered by status
    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_list.add_argument("status", type=str, nargs="?", choices=["todo", "in-progress", "done"], help="Filter the tasks by status (optional)")

    # Parse command-line arguments and call the appropriate function
    args = parser.parse_args()

    # Execute the appropriate function based on the parsed command
    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_task(args.id, "in-progress")
    elif args.command == "mark-done":
        mark_task(args.id, "done")
    elif args.command == "list":
        list_tasks(args.status)

# Entry point for the program
if __name__ == "__main__":
    main()