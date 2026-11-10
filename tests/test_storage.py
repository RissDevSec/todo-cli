"""Storage regression tests: a tasks.json with valid JSON of the wrong
shape must load as an empty list instead of crashing every command."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from modules.storage import load_tasks


def _write_tasks_file(tmp_path, monkeypatch, content):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "tasks.json").write_text(content, encoding="utf-8")


def test_load_tasks_wrong_shape_dict(tmp_path, monkeypatch):
    """A JSON object is not a task list: load as empty, don't crash."""
    _write_tasks_file(tmp_path, monkeypatch, json.dumps({"a": 1}))
    assert load_tasks() == []


def test_load_tasks_wrong_shape_scalar(tmp_path, monkeypatch):
    """A JSON scalar is not a task list: load as empty, don't crash."""
    _write_tasks_file(tmp_path, monkeypatch, '"just a string"')
    assert load_tasks() == []


def test_load_tasks_valid_list_preserved(tmp_path, monkeypatch):
    """A proper task list must still load unchanged."""
    tasks = [{"id": "1", "task": "milk", "priority": "high", "done": False,
              "due_date": None}]
    _write_tasks_file(tmp_path, monkeypatch, json.dumps(tasks))
    assert load_tasks() == tasks


def test_load_tasks_missing_file(tmp_path, monkeypatch):
    """A missing file still loads as empty."""
    monkeypatch.chdir(tmp_path)
    assert load_tasks() == []


def test_load_tasks_malformed_json(tmp_path, monkeypatch):
    """Malformed JSON still loads as empty."""
    _write_tasks_file(tmp_path, monkeypatch, "{not json")
    assert load_tasks() == []
