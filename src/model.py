from datetime import datetime
from pydantic import BaseModel


class Task(BaseModel):
    name: str
    status: bool = False
    create_date: datetime = datetime.now()
    start_date: datetime | None = None
