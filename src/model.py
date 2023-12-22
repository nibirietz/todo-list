from datetime import datetime
from pydantic import BaseModel, Field


class Task(BaseModel):
    name: str
    status: bool = False
    create_date: datetime = Field(default_factory=datetime.now)
    start_date: datetime | None = None
