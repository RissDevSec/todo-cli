"""Reads user input and dispatches each command to modules.tasks."""

import os
import sys
import modules.tasks as tasks

def show_menu():
    """Print the list of available commands."""
    print("\ntodo-cli — a simple task manager\n")
    print("Commands:")
    print("  add [priority] <task>")
    print("  due <index> <date>")
    print("  due delete <index>")
    print("  done <index>")
    print("  list [priority|done]")
    print("  search [priority|done] <keyword>")
    print("  edit <index> [priority] [task]")
    print("  delete <index>")
    print("  help")
    print("  exit")

def main():
    """Show the menu and keep reading commands until the user exits."""
    show_menu()
    while True:
        command = input("\n> ").strip().split()
        if not command:
            continue

        match command[0].lower():
            case "add":
                if len(command) > 1:
                    if command[1].lower() in tasks.PRIORITY:
                        if len(command) == 2:
                            print("Please specify a task. Usage: add (priority: high/medium/low) <task>")
                        else:
                            tasks.add_task(" ".join(command[2:]), command[1].lower())
                    else:
                        tasks.add_task(" ".join(command[1:]))
                else:
                    print("Please specify a task. Usage: add (priority: high/medium/low) <task>")

            case "due":
                if len(command) == 3:
                    if command[1].lower() == "delete":
                        try:
                            tasks.remove_due_date(int(command[2]))
                        except ValueError:
                            print("Please enter a valid task number. Usage: due delete <index>")
                    else:
                        try:
                            task_choice = int(command[1])
                        except ValueError:
                            print("Please enter a valid task number. Usage: due <index> <YYYY-MM-DD>")
                        else:
                            tasks.set_due_date(task_choice, command[2])
                else:
                    print("Usage: due <index> <YYYY-MM-DD>  |  due delete <index>")

            case "done":
                if len(command) > 1:
                    try:
                        tasks.mark_task_done(int(command[1]))
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print("Please specify a task number. Usage: done <index>")

            case "list":
                if len(command) > 1:
                    command_lower = command[1].lower()
                    if command_lower in tasks.PRIORITY or command_lower == "done":
                        tasks.list_tasks(command_lower)
                    else:
                        print("Invalid filter. Usage: list [priority: high/medium/low] or list done")
                else:
                    tasks.list_tasks()

            case "search":
                if len(command) > 1:
                    command_lower = command[1].lower()
                    if command_lower in tasks.PRIORITY or command_lower == "done":
                        if len(command) == 2:
                            print("Please specify a keyword. Usage: search (priority: high/medium/low|done) <keyword>")
                        else:
                            tasks.search_tasks(" ".join(command[2:]), command_lower)
                    else:
                        tasks.search_tasks(" ".join(command[1:]))
                else:
                    print("Please specify a keyword. Usage: search [priority] <keyword>")

            case "edit":
                if len(command) > 2:
                    try:
                        task_choice = int(command[1])
                        if command[2].lower() in tasks.PRIORITY:
                            if len(command) == 3:
                                tasks.edit_task(task_choice, command[2].lower())
                            else:
                                tasks.edit_task(task_choice, command[2].lower(), " ".join(command[3:]))
                        else:
                            tasks.edit_task(task_choice, new_task=" ".join(command[2:]))
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print("Please specify a task number. Usage: edit <index> (priority: high/medium/low) [task]")

            case "delete":
                if len(command) > 1:
                    try:
                        tasks.delete_task(int(command[1]))
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print("Please specify a task number. Usage: delete <index>")

            case "help":
                os.system("clear")
                show_menu()

            case "exit":
                print("Goodbye!")
                sys.exit()

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system("clear")
        print("Goodbye!")