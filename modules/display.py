"""Formatting and printing tasks to the terminal."""

from datetime import datetime
from collections import Counter


def format_due_date(due_date_str, is_done):
    """Build the '- due: YYYY-MM-DD' text for a task, adding an
    OVERDUE flag if it's past due and not done yet."""
    if not due_date_str: return ""
    task_date = datetime.fromisoformat(due_date_str).date()
    today = datetime.today().date()
    overdue = " OVERDUE" if task_date < today and not is_done else ""
    return f"- due: {due_date_str}{overdue}"

def group_tasks(tasks, title="Tasks:"):
    """Print tasks grouped by priority, with a customizable heading
    so search results can say things like "Tasks matching 'milk':"."""
    counts = Counter(task["priority"] for task in tasks.values())
    print(f"\n{title}")
    current_group = None
    for index, task in tasks.items():
        if task["priority"] != current_group:
            current_group = task["priority"]
            print(f"\n{current_group.upper()} ({counts[current_group]})")

        done_marker = "[x]" if task["done"] else "[ ]"
        due_display = format_due_date(task.get("due_date"), task["done"])
        print(f"{index}. {done_marker} {task['task']} {due_display}".rstrip())