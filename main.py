import flet
from db import *


class MainWindow(flet.UserControl):
    def __init__(self):
        super().__init__()
        self.page = None
        self.repository = Repository(db)
        flet.app(target=self.main_loop)

    def main_loop(self, page: flet.Page):
        self.page = page
        self.add_input_field()
        self.load_date()

    def add_input_field(self):
        input_field = flet.TextField(label="Введите задачу", on_submit=self.create_task)
        self.page.add(input_field)

    def load_date(self):
        tasks = self.repository.load_tasks()
        for task in tasks:
            print()
            self.page.add(TaskView(task).get_view())

    def create_task(self, field):
        task_name = field.control.value
        task = Task(task_name)
        task_view = TaskView(task)
        self.repository.add_task(task)
        self.page.add(task_view.get_view())


class Task:
    def __init__(self, name: str, status=0, start_date=None):
        self.name = name
        self.status = status
        self.start_date = start_date

    def delete_task(self):
        repo = Repository(db)
        repo.delete_task(self)


class TaskView(flet.UserControl):
    def __init__(self, task: Task):
        super().__init__()
        self.task = task
        name = flet.Text(value=task.name)
        status = flet.Text(value=str(task.status))
        start_date = flet.Text(value=task.start_date)
        delete_button = flet.ElevatedButton(text="D", on_click=self.delete_task)
        self.row = flet.Row([name, status, start_date, delete_button])

    def get_view(self):
        return self.row

    def delete_task(self, task):
        self.task.delete_task()
        self.row.page.remove(self.row)


class Repository:
    def __init__(self, database: Database):
        self.database = database

    def add_task(self, task: Task):
        self.database.add_task(task)

    def update_task(self, task: Task):
        self.database.update_task(task)

    def load_tasks(self):
        tasks = []
        data = self.database.load_tasks()
        for task_row in data:
            name = task_row[1]
            status = task_row[2]
            start_date = task_row[3]
            task = Task(name, status, start_date)
            tasks.append(task)

        return tasks

    def delete_task(self, task):
        self.database.delete_task(task)


def main():
    main_window = MainWindow()


# main_window = MainWindow()

if __name__ == '__main__':
    main()
