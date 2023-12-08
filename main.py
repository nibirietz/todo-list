import flet
from db import Task
import db


class MainWindow():
    def __init__(self):
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
            task_view = TaskView(task)
            self.page.overlay.append(task_view.date_picker)
            self.page.add(task_view.get_view())

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
        start_date = flet.Text(value=str(task.start_date))
        created_on = flet.Text(value=task.created_on)

        self.check_box = flet.Checkbox(value=task.status, on_change=self.check_box_change)

        delete_button = flet.PopupMenuItem(text="Удалить задачу", on_click=self.delete_task)
        popup_button = flet.PopupMenuButton(items=[delete_button])

        self.date_picker = flet.DatePicker(on_change=self.change_date)

        self.date_button = flet.ElevatedButton(text=str(task.created_on),
                                               on_click=lambda _: self.date_picker.pick_date())
        self.row = flet.Row([self.check_box, name, created_on, self.date_button, popup_button])

    def get_view(self):
        return self.row

    def check_box_change(self, check_box):
        self.task.update(status=self.check_box.value)

    def delete_task(self, task):
        db.database.delete_task(self.task)
        self.row.page.remove(self.row)

    def change_date(self, e):
        print(self.date_picker.value)
        self.task.update(start_date=self.date_picker.value)
        self.date_button.text = self.date_picker.value.date()
        self.date_button.update()


def main():
    main_window = MainWindow()


if __name__ == '__main__':
    main()
