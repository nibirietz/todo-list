from src.orm import Database
from src.model import Task


class Repository:
    def __init__(self, database=Database()):
        self.database = database

    def load_tasks(self):
        tasks_table = self.database.load_tasks()
        return [Task(name=task.TaskTable.name,
                     status=task.TaskTable.status,
                     create_date=task.TaskTable.create_date,
                     start_date=task.TaskTable.start_date) for
                task in
                tasks_table]

    def add_task(self, task: Task):
        name = task.name
        status = task.status
        create_date = task.create_date
        start_date = task.start_date
        self.database.add_task(name=name, status=status, create_date=create_date, start_date=start_date)

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
