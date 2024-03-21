import datetime

from src.repository import Repository
from src.model import Task

repository = Repository()
task = Task(name="test111",
            create_date=datetime.datetime.strptime("2023-12-11 20:16:51.179616", "%Y-%m-%d %H:%M:%S.%f"))
# dao.delete_task(task)

print([task.__dict__ for task in repository.load_tasks()])
