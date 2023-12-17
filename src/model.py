import datetime


class Task:
    def __init__(self, name: str, status=False, create_date=None, start_date=None):
        self.name = name
        self.status = status
        self.create_date = create_date if create_date is not None else datetime.datetime.now()
        self.start_date = start_date.date() if start_date is not None else None
