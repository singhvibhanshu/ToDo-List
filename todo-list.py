import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks, file)
    except:
        print("Failed to save.")

def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display")
    else:
        print("Your To-Do List: ")
        for index, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{index + 1}. {task['description']} | {status}")

def create_tasks(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty.")

def mark_task_as_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    print(tasks)

    while True:
        print("\nTo-Do List Manager!")
        print("01: View Tasks.")
        print("02: Add Tasks.")
        print("03: Complete Tasks.")
        print("04: Exit.")

        choice = input("Enter your choice: ").strip()

        if choice == "01":
            view_tasks(tasks)
        elif choice == "02":
            create_tasks(tasks)
        elif choice == "03":
            mark_task_as_complete(tasks)
        elif choice == "04":
            print("GoodBye!")
            break
        else:
            print("Invalid choice. Please try again!")