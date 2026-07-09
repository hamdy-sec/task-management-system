import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n===== Task List =====")

    for i, task in enumerate(tasks, start=1):
        print(f"""
{i}) {task['title']}
   Status: {task['status']}
   Priority: {task['priority']}
   Date: {task['date']}
""")


def add_task(tasks):
    title = input("Enter task title: ")

    priority = input("Enter priority (High / Medium / Low): ")

    while priority not in ["High", "Medium", "Low"]:
        priority = input("Invalid input! Enter (High / Medium / Low): ")

    date = input("Enter date: ")

    task = {
        "title": title,
        "status": "Not Completed",
        "priority": priority,
        "date": date
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully ✔")


def delete_task(tasks):
    display_tasks(tasks)

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Task deleted ✔")
        else:
            print("Invalid number ❌")

    except:
        print("Invalid input ❌")


def update_task(tasks):
    display_tasks(tasks)

    try:
        index = int(input("Enter task number to update: ")) - 1

        if 0 <= index < len(tasks):

            print("1- Title")
            print("2- Priority")
            print("3- Date")

            choice = input("What do you want to update? ")

            if choice == "1":
                tasks[index]['title'] = input("Enter new title: ")

            elif choice == "2":
                priority = input("Enter priority: ")

                while priority not in ["High", "Medium", "Low"]:
                    priority = input("Invalid input! Enter (High / Medium / Low): ")

                tasks[index]['priority'] = priority

            elif choice == "3":
                tasks[index]['date'] = input("Enter new date: ")

            else:
                print("Invalid choice ❌")
                return

            save_tasks(tasks)
            print("Task updated ✔")

        else:
            print("Invalid number ❌")

    except:
        print("Invalid input ❌")


def mark_done(tasks):
    display_tasks(tasks)

    try:
        index = int(input("Enter task number: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index]['status'] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed ✔")

        else:
            print("Invalid number ❌")

    except:
        print("Invalid input ❌")


def search_task(tasks):
    keyword = input("Enter keyword to search: ")

    found = False

    for task in tasks:
        if keyword.lower() in task['title'].lower():

            print(f"""
Task found:
{task['title']}
Status: {task['status']}
Priority: {task['priority']}
""")

            found = True

    if not found:
        print("No results found ❌")


def menu():
    tasks = load_tasks()

    while True:

        print("""
===== To-Do List =====
1. Add Task
2. Display Tasks
3. Delete Task
4. Update Task
5. Mark Task as Completed
6. Search
7. Exit
""")

        choice = input("Choose a number: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            update_task(tasks)

        elif choice == "5":
            mark_done(tasks)

        elif choice == "6":
            search_task(tasks)

        elif choice == "7":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice ❌")


if __name__ == "__main__":
    menu()
