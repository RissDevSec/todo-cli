import os
import sys
import json
from collections import Counter
import uuid

TASKS_FILE = "tasks.json"
PRIORITY = ["high", "medium", "low"]
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent="\t")

def get_sorted_tasks(tasks):
    return sorted(tasks, key=lambda t: PRIORITY_ORDER[t["priority"]])

def find_task_by_id(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            return i
    return None

def find_index(tasks, user_choice):
    sorted_tasks = get_sorted_tasks(tasks)
    if user_choice <= 0 or user_choice > len(sorted_tasks):
        return None
    task_id = sorted_tasks[user_choice - 1]["id"]
    return find_task_by_id(tasks, task_id)

def add_task(task, priority="medium"):
    tasks = load_tasks()
    tasks.append({
        "id": str(uuid.uuid4()),
        "task": task,
        "priority": priority,
        "done": False
    })
    save_tasks(tasks)
    print(f"({priority.capitalize()}) '{task}' has been added.")

def mark_task_done(user_choice):
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    index = find_index(tasks, user_choice)
    if index is None: return print("Invalid task number.")
    task = tasks[index]
    task["done"] = not task["done"]
    status = "done" if task["done"] else "not done"
    print(f"'{task['task']}' has been marked as {status}.")
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    sorted_tasks = get_sorted_tasks(tasks)
    counts = Counter(task["priority"] for task in sorted_tasks)
    print("\nTasks:")
    current_group = None
    for index, task in enumerate(sorted_tasks, start=1):
        if task["priority"] != current_group:
            current_group = task["priority"]
            print(f"\n{current_group.upper()} ({counts[current_group]})")

        done = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {done} {task['task']}")

def delete_task(user_choice):
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    index = find_index(tasks, user_choice)
    if index is None: return print("Invalid task number.")
    task = tasks.pop(index)["task"]
    print(f"'{task}' has been deleted.")
    save_tasks(tasks)

def main():
    while True:
        print("\ntodo-cli — a simple task manager\n")
        print("Commands:")
        print(" add [priority] <task>")
        print(" done <index>")
        print(" list")
        print(" delete <index>")
        print(" exit")
        print(" help")

        while True:
            command = input("\n> ").strip().split()
            if not command: continue

            match command[0].lower():
                case "add":
                    if len(command) > 1:
                        if command[1].lower() in PRIORITY:
                            if len(command) == 2:
                                print("Please specify a task. Usage: add (priority: high/medium/low) <task>")
                            else:
                                add_task(" ".join(command[2:]), command[1].lower())
                        else:
                            add_task(" ".join(command[1:]))
                    else:
                        print("Please specify a task. Usage: add (priority: high/medium/low) <task>")
                case "done":
                    if len(command) > 1:
                        try:
                            mark_task_done(int(command[1]))
                        except ValueError:
                            print("Please enter a valid number.")
                    else:
                        print("Please specify a task number. Usage: done <index>")
                case "list":
                    list_tasks()
                case "delete":
                    if len(command) > 1:
                        try:
                            delete_task(int(command[1]))
                        except ValueError:
                            print("Please enter a valid number.")
                    else:
                        print("Please specify a task number. Usage: delete <index>")
                case "exit":
                    print("Goodbye!")
                    sys.exit()
                case "help":
                    os.system("clear")
                    break
                case _:
                    print("Invalid command.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system("clear")
        print("Goodbye!")