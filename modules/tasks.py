import uuid
from datetime import datetime
from modules.storage import load_tasks, save_tasks
from modules.display import group_tasks

PRIORITY = ["high", "medium", "low"]
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

def tasks_exist():
    tasks = load_tasks()
    if tasks: return tasks
    print("There are no tasks yet.")
    return None

def get_sorted_tasks(tasks):
    sorted_task = sorted(tasks, key=lambda t: PRIORITY_ORDER[t["priority"]])
    numbered_tasks = {}
    for index, task in enumerate(sorted_task, start=1):
        numbered_tasks[index] = task
    return numbered_tasks

def find_task_by_id(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            return i
    return None

def find_index(tasks, task_choice):
    sorted_tasks = get_sorted_tasks(tasks)
    if task_choice not in sorted_tasks: return None
    task_id = sorted_tasks[task_choice]["id"]
    return find_task_by_id(tasks, task_id)

def resolve_task(tasks, task_choice):
    index = find_index(tasks, task_choice)
    if index is None:
        print("Invalid task number.")
    return index

def filter_tasks(tasks, filter_criteria):
    if filter_criteria in PRIORITY:
        return {index: task for index, task in tasks.items() if task["priority"] == filter_criteria}
    elif filter_criteria == "done":
        return {index: task for index, task in tasks.items() if task["done"]}
    return tasks

def add_task(task, priority="medium"):
    tasks = load_tasks()
    tasks.append({
        "id": str(uuid.uuid4()),
        "task": task,
        "priority": priority,
        "done": False,
        "due_date": None,
    })
    save_tasks(tasks)
    print(f"({priority.capitalize()}) '{task}' has been added.")

def set_due_date(task_choice, date_str):
    tasks = tasks_exist()
    if tasks is None: return
    index = resolve_task(tasks, task_choice)
    if index is None: return
    task = tasks[index]
    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD (e.g. 2026-12-31).")
        return
    task["due_date"] = parsed_date.date().isoformat()
    save_tasks(tasks)
    print(f"'{task['task']}' is now due on {task['due_date']}.")

def remove_due_date(task_choice):
    tasks = tasks_exist()
    if tasks is None: return
    index = resolve_task(tasks, task_choice)
    if index is None: return
    task = tasks[index]
    if task.get("due_date") is None:
        print("This task has no due date to remove.")
        return
    task["due_date"] = None
    save_tasks(tasks)
    print(f"Due date for '{task['task']}' has been removed.")

def mark_task_done(task_choice):
    tasks = tasks_exist()
    if tasks is None: return
    index = resolve_task(tasks, task_choice)
    if index is None: return
    task = tasks[index]
    task["done"] = not task["done"]
    status = "done" if task["done"] else "not done"
    print(f"'{task['task']}' has been marked as {status}.")
    save_tasks(tasks)

def list_tasks(filter_criteria=None):
    tasks = tasks_exist()
    if tasks is None: return

    sorted_tasks = get_sorted_tasks(tasks)
    filtered_tasks = filter_tasks(sorted_tasks, filter_criteria)

    if not filtered_tasks:
        if filter_criteria == "done":
            print("There are no done tasks.")
        elif filter_criteria in PRIORITY:
            print(f"There are no tasks with priority '{filter_criteria}'.")
        return

    group_tasks(filtered_tasks)

def search_tasks(keyword, filter_criteria=None):
    tasks = tasks_exist()
    if tasks is None: return
    sorted_tasks = get_sorted_tasks(tasks)
    keyword_matches = {
        index: task for index, task in sorted_tasks.items()
        if keyword.lower() in task["task"].lower()
    }
    filtered_tasks = filter_tasks(keyword_matches, filter_criteria)

    if not filtered_tasks:
        if filter_criteria == "done":
            print(f"There are no done tasks matching '{keyword}'.")
        elif filter_criteria in PRIORITY:
            print(f"There are no tasks matching '{keyword}' with priority '{filter_criteria}'.")
        else:
            print(f"There are no tasks matching '{keyword}'.")
        return

    title = f"Tasks matching '{keyword}'"
    if filter_criteria:
        title += f" ({filter_criteria})"
    title += ":"
    group_tasks(filtered_tasks, title=title)

def edit_task(task_choice, new_priority=None, new_task=None):
    tasks = tasks_exist()
    if tasks is None: return
    index = resolve_task(tasks, task_choice)
    if index is None: return
    task = tasks[index]
    if new_priority: task["priority"] = new_priority
    if new_task: task["task"] = new_task
    save_tasks(tasks)
    print(f"({task['priority'].capitalize()}) '{task['task']}' has been updated.")

def delete_task(task_choice):
    tasks = tasks_exist()
    if tasks is None: return
    index = resolve_task(tasks, task_choice)
    if index is None: return
    task = tasks.pop(index)["task"]
    print(f"'{task}' has been deleted.")
    save_tasks(tasks)