# To-Do List

A simple command-line To-Do List Manager built using Python. It allows users to add, view, mark tasks as complete/incomplete, and delete tasks while saving them in a JSON file.

## Features
- View all tasks with their status (Completed/Pending)
- Add new tasks
- Mark tasks as complete
- Mark tasks as incomplete
- Delete tasks
- Persistent storage using JSON

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/singhvibhanshu/ToDo-List.git
   ```
2. Navigate to the project directory:
   ```sh
   cd ToDo-List
   ```
3. Ensure you have Python installed (version 3.x recommended).

## Usage
Run the script using:
```sh
python todo-list.py
```
Follow the on-screen instructions to interact with the To-Do List Manager.

## How It Works
1. The tasks are stored in a `todo_list.json` file.
2. The menu provides the following options:
   - View tasks
   - Add a new task
   - Mark a task as complete
   - Mark a task as incomplete
   - Delete a task
   - Exit the program
3. The input from the user determines the action performed.