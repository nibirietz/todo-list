import datetime


class Task:
    def __init__(self, name: str, status=-1, create_date=None):
        self.name = name
        self.status = status
        self.create_date = create_date if create_date is not None else datetime.datetime.now()
