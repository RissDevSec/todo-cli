import os
import sys
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent="\t")

def add_task(task):
    tasks = load_tasks()
    tasks.append({
        "task": task,
        "done": False
    })
    save_tasks(tasks)
    print(f"'{task}' has been added.")

def mark_task_done(index):
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    try:
        if index <= 0: raise IndexError
        task = tasks[index - 1]
        if task['done']:
            task['done'] = False
            print(f"'{task['task']}' has been marked as not done.")
        else:
            task['done'] = True
            print(f"'{task['task']}' has been marked as done.")
    except IndexError:
        return print("Invalid task number.")
    else:
        save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    print("\nTasks:")
    for index, task in enumerate(tasks, start=1): 
        done = "[x]" if task['done'] else "[ ]"
        print(f"{index}. {done} {task['task']}")

def delete_task(index):
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    try:
        if index <= 0: raise IndexError
        task = tasks.pop(index - 1)['task']
        print(f"'{task}' has been deleted.")
    except IndexError:
        print("Invalid task number.")
    else:
        save_tasks(tasks)

def main():
    while True:
        print("\ntodo-cli — a simple task manager\n")
        print("Commands:")
        print(" add <task>")
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
                        add_task(" ".join(command[1:]))
                    else:
                        print("Please specify a task. Usage: add <task>")
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