import json
from todo_cli_ultra.constants import TASKS_FILE
from todo_cli_ultra.models import Task


def save_task(task: str):
    tasks = load_task()
    new_task = Task(content=task)
    with open(TASKS_FILE, "w") as f:
        tasks.append(new_task.to_dict())
        json.dump(tasks, f)


def update_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)


def load_task():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
            return tasks
    except Exception:
        return []
