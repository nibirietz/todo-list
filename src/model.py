import datetime


class Task:
    def __init__(self, name: str, status=-1, create_date=datetime.datetime.now()):
        self.name = name
        self.status = status
        self.create_date = create_date
