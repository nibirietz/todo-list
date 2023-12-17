from repository import repository
from model import Task
import flet


class MainWindow:
    def __init__(self):
        self.page: flet.Page
        flet.app(target=self.main_loop)

    def main_loop(self, page: flet.Page):
        self.page = page
        self.create_text_field()
        self.load_tasks()

    def load_tasks(self):
        tasks = repository.load_tasks()
        tasks_view = []
        for task in tasks:
            task_view = TaskView(task)
            tasks_view.append(task_view.row)
            self.page.overlay.append(task_view.date_picker)
        self.page.add(*tasks_view)

    def create_text_field(self):
        text_field = flet.TextField(label="Введите задачу", on_submit=self.create_task)
        self.page.add(text_field)

    def create_task(self, field):
        task = Task(field.control.value)
        repository.add_task(task)
        field.control.value = ""
        task_view = TaskView(task)
        self.page.overlay.append(task_view.date_picker)
        self.page.add(task_view.row)


class TaskView:
    def __init__(self, task: Task):
        self.task = task
        name = flet.TextField(label=task.name, on_submit=self.update_name)
        status = flet.Checkbox(value=task.status, on_change=self.update_checkbox)
        create_date = flet.Text(value=str(task.create_date.strftime("%Y-%m-%d %H:%M:%S")))
        self.start_date = flet.ElevatedButton(text=task.start_date
        if task.start_date is not None else "Выбрать дату",
                                              on_click=lambda _: self.date_picker.pick_date())
        self.date_picker = flet.DatePicker(on_change=self.change_date)
        delete_button = flet.IconButton(icon=flet.icons.DELETE_OUTLINE,
                                        on_click=self.delete)
        self.row = flet.Row([status, name, create_date, self.start_date, delete_button])

    def update_name(self, field):
        name = field.control.value
        field.control.label = name
        field.control.value = ""
        self.task.name = name
        repository.update_task(task=self.task)

    def delete(self, button):
        repository.delete_task(self.task)
        self.row.page.remove(self.row)

    def update_checkbox(self, button):
        self.task.status = button.control.value
        repository.update_task(self.task)

    def change_date(self, button):
        self.task.start_date = self.date_picker.value.date()
        repository.update_task(self.task)
        self.start_date.text = self.date_picker.value.date()
        self.date_picker.page.update()


def main():
    window = MainWindow()


if __name__ == '__main__':
    main()
