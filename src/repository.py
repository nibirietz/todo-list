from datetime import datetime
from src.orm import Database, TaskTable
from src.model import Task


class Repository:
    def __init__(self, database=Database()):
        self.database = database

    def _task_to_dict(self, task: Task) -> dict:
        return {"name": task.name, "status": task.status, "create_date": task.create_date,
                "start_date": task.create_date}

    def _to_task(self, task_table: TaskTable):
        return Task(name=task_table.name, status=task_table.status, create_date=task_table.create_date,
                    start_date=task_table.start_date)

    def load_tasks(self):
        tasks_table: list[TaskTable] = self.database.load_tasks()
        return [self._to_task(task[0]) for task in tasks_table]

    def add_task(self, task: Task):
        task_attributes = self._task_to_dict(task)
        self.database.add_task(**task_attributes)

    def update_task(self, task: Task):
        name = task.name
        status = task.status
        create_date = task.create_date
        start_date = task.start_date
        self.database.update_task(create_date=create_date, name=name, status=status, start_date=start_date)

    def delete_task(self, task: Task):
        create_date = task.create_date
        self.database.delete_task(create_date)


repository = Repository()
