import os
import sys

TASKS_FILE = "task.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE): 
        with open(TASKS_FILE, "r") as file:
            for task in file:
                tasks.append(task.strip())
    return tasks

def add_task(task):
    with open(TASKS_FILE, "a") as file:
        file.write(f"{task}\n")
    print(f"\'{task}\' has been added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks: return print("There are no tasks yet.")
    print("\nTasks:")
    for index, task in enumerate(tasks, start=1): 
        print(f"{index}. {task}")

def delete_task(index):
    tasks = load_tasks()
    try:
        print(f"\'{tasks.pop(int(index) - 1)}\' has been deleted.")
    except IndexError:
        print("Invalid Task Number")
    else:
        with open(TASKS_FILE, "w",) as file:
            for task in tasks:
                file.write(f"{task}\n")

def main():
    while True:
        print("=== MENU ===")
        print("Commands:")
        print(" add <task>")
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
                case "list":
                    list_tasks()
                case "delete":
                    if len(command) > 1:
                        try:
                            delete_task(int(command[1]))
                        except ValueError:
                            print("Please enter a valid number")
                    else:
                        print("Please specify a task number. Usage: delete <index>")
                case "exit":
                    print("Good Bye!")
                    sys.exit()
                case "help":
                    os.system("clear")
                    break
                case _:
                    print("Invalid Command.")
                    continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system("clear")
        print("Good Bye!")