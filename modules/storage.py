"""Reading and writing the task list to disk as JSON."""

import json
from pathlib import Path

TASKS_FILE = Path("data/tasks.json")


def load_tasks():
    """Load tasks from disk, or return an empty list if the file
    doesn't exist yet or is corrupted."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Write the task list to disk, creating the data folder first if needed."""
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent="\t")