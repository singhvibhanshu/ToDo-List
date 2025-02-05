def load_tasks():
    pass

def save_tasks():
    pass

def view_tasks():
    pass

def create_tasks():
    pass

def mark_task_as_complete():
    pass

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager!")
        print("01: View Tasks.")
        print("02: Add Tasks.")
        print("03: Complete Tasks.")
        print("04: Exit.")

        choice = input("Enter your choice: ").strip()

        if choice == "01":
            view_tasks()
        elif choice == "02":
            create_tasks()
        elif choice == "03":
            mark_task_as_complete()
        elif choice == "04":
            print("GoodBye!")
            break
        else:
            print("Invalid choice. Please try again!")