import os
import sys
import json

TASKS_FILE = "tasks.json"
PRIORITY = ["high", "medium", "low"]

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent="\t")

def add_task(task, priority = "medium"):
    tasks = load_tasks()
    tasks.append({
        "task": task,
        "priority": priority,
        "done": False
    })
    save_tasks(tasks)
    print(f"({priority.capitalize()}) '{task}' has been added.")

def mark_task_done(index):
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    if index <= 0 or index > len(tasks):
        return print("Invalid task number.")
    task = tasks[index - 1]
    if task['done']:
        task['done'] = False
        print(f"'{task['task']}' has been marked as not done.")
    else:
        task['done'] = True
        print(f"'{task['task']}' has been marked as done.")
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    print("\nTasks:")
    for index, task in enumerate(tasks, start=1): 
        done = "[x]" if task['done'] else "[ ]"
        priority = f"({task['priority'].capitalize()})"
        task = task['task']
        print(f"{index}. {priority:<12}{done} {task}")

def delete_task(index):
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    if index <= 0 or index > len(tasks):
        return print("Invalid task number.")
    task = tasks.pop(index - 1)['task']
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