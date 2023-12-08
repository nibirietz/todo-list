import datetime

from sqlalchemy import Column, Integer, String, DateTime, create_engine, select
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Integer)
    created_on = Column(DateTime)
    start_date = Column(DateTime)

    def __init__(self, name, status=-1, start_date=None):
        self.name = name
        self.status = status
        self.created_on = datetime.datetime.now()
        self.start_date = start_date


class Database:
    def __init__(self):
        self.engine = create_engine("sqlite:///task.db", echo=True)
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def add_task(self, task: Task):
        self.session.add(task)
        self.session.commit()

    def load_tasks(self) -> list[type(Task)]:
        return [task for task in self.session.query(Task)]

    def delete_task(self, task: Task):
        self.session.delete(task)
        self.session.commit()


database = Database()
print(database.load_tasks())
