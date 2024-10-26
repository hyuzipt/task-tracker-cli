# Task Tracker CLI

Task Tracker CLI is a command-line application that helps you track and manage your to-do list. With this tool, you can add, update, delete, and list tasks, as well as mark them as "in-progress" or "done." The application stores all tasks in a JSON file.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Add a Task](#add-a-task)
  - [List Tasks](#list-tasks)
  - [Update a Task](#update-a-task)
  - [Delete a Task](#delete-a-task)
  - [Mark a Task as In Progress](#mark-a-task-as-in-progress)
  - [Mark a Task as Done](#mark-a-task-as-done)
- [Examples](#examples)
- [Task Properties](#task-properties)

---

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/hyuzipt/task-tracker-cli.git
   ```

2. Navigate into the project directory:
   ```bash
   cd task-tracker-cli
   ```

3. Ensure you have Python 3.7 or higher installed. The CLI uses Python's built-in libraries, so no additional dependencies are required.

4. Make the `task-cli.py` executable:
   ```bash
   chmod +x task-cli.py
   ```

You're all set to start using Task Tracker CLI!

---

## Usage

### Add a Task
Adds a new task with a description.

```bash
python task-cli.py add "Task description"
```

### List Tasks
Lists all tasks. Optionally, you can filter tasks by their status.

```bash
python task-cli.py list
```

To filter by task status (`todo`, `in-progress`, or `done`):

```bash
python task-cli.py list <status>
```

### Update a Task
Updates the description of an existing task.

```bash
python task-cli.py update <id> "New task description"
```

### Delete a Task
Deletes a task by its ID.

```bash
python task-cli.py delete <id>
```

### Mark a Task as In Progress
Marks a task as `in-progress` by ID.

```bash
python task-cli.py mark-in-progress <id>
```

### Mark a Task as Done
Marks a task as `done` by ID.

```bash
python task-cli.py mark-done <id>
```

---

## Examples

1. **Adding a Task**
   ```bash
   python task-cli.py add "Buy groceries"
   ```
   Output:
   ```
   Task added successfully (ID: 1)
   ```

2. **Listing All Tasks**
   ```bash
   python task-cli.py list
   ```
   Output:
   ```
   List of Tasks:
   ID: 1 - Buy groceries (todo)
   ID: 2 - Walk the dog (in-progress)
   ID: 3 - Finish project (done)
   ```

3. **Updating a Task**
   ```bash
   python task-cli.py update 1 "Buy groceries and cook dinner"
   ```
   Output:
   ```
   Task (ID: 1) updated successfully
   ```

4. **Deleting a Task**
   ```bash
   python task-cli.py delete 3
   ```
   Output:
   ```
   Task (ID: 3) deleted successfully
   ```

5. **Marking a Task as In Progress**
   ```bash
   python task-cli.py mark-in-progress 2
   ```
   Output:
   ```
   Task (ID: 2) marked as 'in-progress'
   ```

6. **Marking a Task as Done**
   ```bash
   python task-cli.py mark-done 2
   ```
   Output:
   ```
   Task (ID: 2) marked as 'done'
   ```

7. **Filtering Tasks by Status**
   ```bash
   python task-cli.py list done
   ```
   Output (if there are no completed tasks):
   ```
   No task with 'done' status found
   ```

---

## Task Properties

Each task in the Task Tracker CLI has the following properties:
- **id**: A unique identifier for the task.
- **description**: A brief description of the task.
- **status**: The current status of the task (`todo`, `in-progress`, or `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

These properties are saved in `tasks.json` and are updated automatically as you modify tasks.

---

https://roadmap.sh/projects/task-tracker
