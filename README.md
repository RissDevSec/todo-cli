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
- ✏️ **Edit tasks** — update a task's text, priority, or both — even if it's already marked done
- 🔍 **Filter tasks** — view only tasks with a specific priority, or only completed tasks
- 🔎 **Search tasks** — find tasks by keyword (case-insensitive), optionally narrowed down further by priority or done status
- 🗑️ **Delete tasks** — remove a task by its number
- 💾 **Persistent storage** — tasks are saved to a JSON file automatically, no database required
- ⌨️ **Command-based interface** — simple, git-style commands (`add`, `done`, `edit`, `list`, `search`, `delete`, `help`, `exit`)

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

> add high Buy milk and eggs
(High) 'Buy milk and eggs' has been added.

> add Buy bread
(Medium) 'Buy bread' has been added.

> list

Tasks:

HIGH (2)
1. [ ] Finish Python homework
2. [ ] Buy milk and eggs

MEDIUM (1)
3. [ ] Buy bread

> search milk

Tasks matching 'milk':

HIGH (1)
2. [ ] Buy milk and eggs

> search high milk

Tasks matching 'milk' (high):

HIGH (1)
2. [ ] Buy milk and eggs

> search high bread
There are no tasks matching 'bread' with priority 'high'.

> done 2
'Buy milk and eggs' has been marked as done.

> delete 3
'Buy bread' has been deleted.

> exit
Goodbye!
```

Note: task numbers refer to their position in the sorted, grouped list — not the order they were originally added. Filtering and searching (with or without a priority) keep each task's original number rather than renumbering from 1, so `delete`, `edit`, and `done` always target the correct task. Numbers may shift whenever a task's priority changes, since that changes its position in the sorted list — always run `list` again after an edit to confirm current numbering before acting on it.

**A note on `search [priority|done] <keyword>`:** because the priority/`done` word is optional and comes first, a single-word search that happens to match a priority name or `done` (e.g. `search high`) is interpreted as "filter by that with no keyword" and will prompt for a keyword, rather than searching for the literal word. If you need to search for a task containing a word like "high" as part of a longer phrase, include more of the phrase (e.g. `search high quality paper`).

## 🛠️ Tech Stack

- Python 3 (standard library only — no external dependencies)

## 📁 Project Structure

```
todo-cli/
├── main.py       # Main application logic
├── tasks.json    # Local storage for tasks (auto-generated, gitignored)
├── README.md
└── LICENSE
```

## 📄 License

This project is licensed under the [MIT License](LICENSE) — feel free to use, modify, and distribute it.
