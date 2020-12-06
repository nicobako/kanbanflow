from .base_model import BaseModel
from typing import Optional


class Task(BaseModel):
    id: str
    name: str
    description: str
    color: str
    column_id: str
    total_seconds_estimate: int
    total_seconds_spent: int
    swimlane_id: Optional[str]
