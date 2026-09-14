# 📝 To-Do List CLI

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A simple command-line to-do list manager built with Python. Tasks are stored persistently in a local JSON file, so your list stays intact between sessions.

## ✨ Features

- ➕ **Add tasks** — quickly add a new task from the command line
- 📋 **List tasks** — view tasks automatically grouped and sorted by priority (High → Medium → Low)
- ✅ **Mark tasks as done** — toggle a task's completion status on or off
- 🚦 **Priority levels** — tag tasks as High, Medium, or Low priority (defaults to Medium if unspecified)
- 📅 **Due dates** — set a deadline for any task; overdue, unfinished tasks are flagged automatically
- ✏️ **Edit tasks** — update a task's text, priority, or both — even if it's already marked done
- 🔍 **Filter tasks** — view only tasks with a specific priority, or only completed tasks
- 🔎 **Search tasks** — find tasks by keyword (case-insensitive), optionally narrowed down further by priority or done status
- 🗑️ **Delete tasks** — remove a task by its number
- 💾 **Persistent storage** — tasks are saved to a JSON file automatically, no database required
- ⌨️ **Command-based interface** — simple, git-style commands (`add`, `done`, `due`, `edit`, `list`, `search`, `delete`, `help`, `exit`)

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/RissDevSec/todo-cli.git
   cd todo-cli
   ```

2. No external dependencies required — this project only uses Python's standard library.

## 📖 Usage

Run the app:
```bash
python main.py
```

Available commands:

| Command | Description |
|---|---|
| `add [priority] <task>` | Add a new task. Priority is optional (`high`/`medium`/`low`), defaults to `medium` |
| `done <index>` | Toggle a task's completion status |
| `due <index> <YYYY-MM-DD>` | Set or update a task's due date |
| `due delete <index>` | Remove a task's due date |
| `edit <index> [priority] [task]` | Update a task's priority, text, or both |
| `list [priority\|done]` | Show all tasks, or filter by priority (`high`/`medium`/`low`) or `done` status |
| `search [priority\|done] <keyword>` | Find tasks whose text contains the keyword. Optionally narrow the results by priority or `done` status |
| `delete <index>` | Delete a task by its number |
| `help` | Show the menu again |
| `exit` | Quit the app |

### Example

```
> add high Finish Python homework
(High) 'Finish Python homework' has been added.

> due 1 2020-01-01
'Finish Python homework' is now due on 2020-01-01.

> add Buy milk
(Medium) 'Buy milk' has been added.

> due 2 2030-01-01
'Buy milk' is now due on 2030-01-01.

> list

Tasks:

HIGH (1)
1. [ ] Finish Python homework - due: 2020-01-01 OVERDUE

MEDIUM (1)
2. [ ] Buy milk - due: 2030-01-01

> done 1
'Finish Python homework' has been marked as done.

> list high

Tasks:

HIGH (1)
1. [x] Finish Python homework - due: 2020-01-01
```

Note that once a task is marked done, an overdue due date is no longer flagged — the `OVERDUE` marker only applies to unfinished tasks.

```
> due delete 1
Due date for 'Finish Python homework' has been removed.
```

Note: task numbers refer to their position in the sorted, grouped list — not the order they were originally added. Filtering and searching (with or without a priority) keep each task's original number rather than renumbering from 1, so `delete`, `edit`, `due`, and `done` always target the correct task. Numbers may shift whenever a task's priority changes, since that changes its position in the sorted list — always run `list` again after an edit to confirm current numbering before acting on it.

**A note on `search [priority|done] <keyword>`:** because the priority/`done` word is optional and comes first, a single-word search that happens to match a priority name or `done` (e.g. `search high`) is interpreted as "filter by that with no keyword" and will prompt for a keyword, rather than searching for the literal word. If you need to search for a task containing a word like "high" as part of a longer phrase, include more of the phrase (e.g. `search high quality paper`).

## 🛠️ Tech Stack

- Python 3 (standard library only — no external dependencies)

The code is split into a small package (`modules/`) separating storage (reading/writing `tasks.json`), business logic (adding, editing, filtering tasks), and display (formatting output) from the command-line entry point in `main.py`.

## 📁 Project Structure

```
todo-cli/
├── main.py              # Entry point: menu display and command parsing
├── modules/
│   ├── __init__.py
│   ├── storage.py       # Reading/writing tasks.json
│   ├── tasks.py         # Business logic: add, edit, delete, filter, search, due dates
│   └── display.py       # Formatting and printing tasks to the terminal
├── data/
│   └── tasks.json       # Local storage for tasks (auto-generated, gitignored)
├── README.md
└── LICENSE
```

## 📄 License

This project is licensed under the [MIT License](LICENSE) — feel free to use, modify, and distribute it.