from src.model import Task


def create_test_task():
    return Task(name="Da!")


def test_read_task():
    task = create_test_task()
    assert task.name == "Da!"
    assert task.status == False


test_read_task()
