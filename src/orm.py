from sqlalchemy import Column, create_engine, select, insert, delete, update, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime

Base = declarative_base()


class TaskTable(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    status = Column(Integer)
    create_date = Column(DateTime)


class Database:
    def __init__(self):
        engine = create_engine("sqlite:///tasks.db")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def load_tasks(self):
        with self.Session() as session:
            return session.execute(select(TaskTable)).fetchall()

    def add_task(self, **data):
        with self.Session() as session:
            session.execute(insert(TaskTable).values(**data))
            session.commit()

    def delete_task(self, create_date: datetime):
        with self.Session() as session:
            session.execute(delete(TaskTable).where(TaskTable.create_date == create_date))
            session.commit()