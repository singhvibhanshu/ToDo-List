import json  # Importing JSON module for file handling

file_name = "todo_list.json"  # File to store tasks

# Function to load tasks from the JSON file
def load_tasks():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        return {"tasks": []}  # Return an empty task list if the file doesn't exist

# Function to save tasks to the JSON file
def save_tasks(tasks):
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks, file)
    except:
        print("Failed to save.")

# Function to display the task list
def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display")
    else:
        print("Your To-Do List: ")
        for index, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{index + 1}. {task['description']} | {status}")

# Function to add a new task
def create_tasks(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty.")

# Function to mark a task as complete
def mark_task_as_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

# Function to mark a task as incomplete
def mark_task_as_incomplete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as incomplete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = False
            save_tasks(tasks)
            print("Task marked as incomplete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"].pop(task_number - 1)  # Remove the selected task from the list
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

# Main function to run the To-Do List manager
def main():
    tasks = load_tasks()  # Load tasks from the file

    while True:
        # Display menu options
        print("\nTo-Do List Manager!")
        print("01: View Tasks.")
        print("02: Add Task.")
        print("03: Complete Task.")
        print("04: Mark Task as Incomplete.")
        print("05: Delete Task.")
        print("06: Exit.")

        choice = input("Enter your choice: ").strip()

        # Handle user choices
        if choice == "01":
            view_tasks(tasks)
        elif choice == "02":
            create_tasks(tasks)
        elif choice == "03":
            mark_task_as_complete(tasks)
        elif choice == "04":
            mark_task_as_incomplete(tasks)
        elif choice == "05":
            delete_task(tasks)
        elif choice == "06":
            print("GoodBye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()  # Run the main function