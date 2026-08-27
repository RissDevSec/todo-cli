# To-Do List CLI

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A simple command-line to-do list manager built with Python. Tasks are stored persistently in a local JSON file, so your list stays intact between sessions.

## Features

- **Add tasks** — quickly add a new task from the command line
- **List tasks** — view all your tasks with numbered indexing and completion status
- **Mark tasks as done** — toggle a task's completion status on or off
- **Delete tasks** — remove a task by its number
- **Persistent storage** — tasks are saved to a JSON file automatically, no database required
- **Command-based interface** — simple, git-style commands (`add`, `done`, `list`, `delete`, `help`, `exit`)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/todo-cli.git
   cd todo-cli
   ```

2. No external dependencies required — this project only uses Python's standard library.

## Usage

Run the app:
```bash
python main.py
```

Available commands:

| Command | Description |
|---|---|
| `add <task>` | Add a new task |
| `done <index>` | Toggle a task's completion status |
| `list` | Show all tasks |
| `delete <index>` | Delete a task by its number |
| `help` | Show the menu again |
| `exit` | Quit the app |

### Example

```
> add Buy groceries
'Buy groceries' has been added.

> add Finish Python homework
'Finish Python homework' has been added.

> done 2
'Finish Python homework' has been marked as done.

> list

Tasks:
1. [ ] Buy groceries
2. [x] Finish Python homework

> delete 1
'Buy groceries' has been deleted.

> exit
Goodbye!
```

## Tech Stack

- Python 3 (standard library only — no external dependencies)

## Project Structure

```
todo-cli/
├── main.py       # Main application logic
├── tasks.json    # Local storage for tasks (auto-generated, gitignored)
├── README.md
└── LICENSE
```

## License

This project is licensed under the [MIT License](LICENSE) — feel free to use, modify, and distribute it.