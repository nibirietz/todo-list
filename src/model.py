from datetime import datetime
from pydantic import BaseModel, Field


class Task(BaseModel):
    """
    Дата-класс задачи. Хранит в себе: название задачи, статус, дату создания и дату начала выполнения задачи.
    """
    name: str
    status: bool = False
    create_date: datetime = Field(default_factory=datetime.now)
    start_date: datetime | None = None
