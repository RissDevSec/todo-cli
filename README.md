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
- 🗑️ **Delete tasks** — remove a task by its number
- 💾 **Persistent storage** — tasks are saved to a JSON file automatically, no database required
- ⌨️ **Command-based interface** — simple, git-style commands (`add`, `done`, `edit`, `list`, `delete`, `help`, `exit`)

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
| `list` | Show all tasks |
| `delete <index>` | Delete a task by its number |
| `help` | Show the menu again |
| `exit` | Quit the app |

### Example

```
> add high Finish Python homework
(High) 'Finish Python homework' has been added.

> add high Call client
(High) 'Call client' has been added.

> add Buy groceries
(Medium) 'Buy groceries' has been added.

> add Clean house
(Medium) 'Clean house' has been added.

> add low Organize bookshelf
(Low) 'Organize bookshelf' has been added.

> list

Tasks:

HIGH (2)
1. [ ] Finish Python homework
2. [ ] Call client

MEDIUM (2)
3. [ ] Buy groceries
4. [ ] Clean house

LOW (1)
5. [ ] Organize bookshelf

> done 3
'Buy groceries' has been marked as done.

> edit 3 low
(Low) 'Buy groceries' has been updated.

> list

Tasks:

HIGH (2)
1. [ ] Finish Python homework
2. [ ] Call client

MEDIUM (1)
3. [ ] Clean house

LOW (2)
4. [x] Buy groceries
5. [ ] Organize bookshelf

> delete 5
'Organize bookshelf' has been deleted.

> exit
Goodbye!
```

Note: task numbers refer to their position in the sorted, grouped list — not the order they were originally added. Numbers may shift as priorities change.

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