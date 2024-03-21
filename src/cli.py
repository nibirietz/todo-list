from repository import repository
from model import Task


class CLI:
    def __init__(self):
        self.repository = repository
        self.main_loop()

    def main_loop(self):
        tasks = self.repository.load_tasks()


class TaskView(Task):
    def __init__(self):
        super().__init__()


def main():
    cli = CLI()


if __name__ == '__main__':
    main()
