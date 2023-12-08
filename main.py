import flet
from db import Task
import db

class MainWindow(flet.UserControl):
    def __init__(self):
        super().__init__()
        self.page = None
        flet.app(target=self.main_loop)

    def main_loop(self, page: flet.Page):
        self.page = page
        self.add_input_field()
        self.load_data()

    def add_input_field(self):
        input_field = flet.TextField(label="Введите задачу", on_submit=self.create_task)
        self.page.add(input_field)

    def load_data(self):
        tasks = db.database.load_tasks()
        for task in tasks:
            self.page.add(TaskView(task).get_view())

    def create_task(self, field):
        task_name = field.control.value
        task = Task(name=task_name)
        task_view = TaskView(task)
        db.database.add_task(task)
        self.page.add(task_view.get_view())


class TaskView:
    def __init__(self, task: Task):
        self.task = task
        name = flet.Text(value=task.name)
        status = flet.Text(value=str(task.status))
        start_date = flet.Text(value=str(task.start_date))
        delete_button = flet.ElevatedButton(text="D", on_click=self.delete_task)
        self.row = flet.Row([name, status, start_date, delete_button])

    def get_view(self):
        return self.row

    def delete_task(self, task):
        db.database.delete_task(self.task)
        self.row.page.remove(self.row)


def main():
    main_window = MainWindow()


# main_window = MainWindow()

if __name__ == '__main__':
    main()
