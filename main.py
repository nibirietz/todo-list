import flet
import database


class MainWindow:
    def __init__(self):
        flet.app(target=self.main_loop)

    def main_loop(self, page: flet.Page):
        self.page = page
        self.core = Core()
        self.input_task_field = flet.TextField(value="Введите задачу", on_submit=self.add_task)
        self.page.add(self.input_task_field)

    def add_task(self):
        self.input_task_field.value = ""


class Core:
    def __init__(self):
        pass


def main():
    main_window = MainWindow()


if __name__ == '__main__':
    main()
