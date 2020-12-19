from .base_model import BaseModel
from typing import Optional, List
from datetime import date


class Label(BaseModel):
    name: str
    pinned: bool


class Task(BaseModel):
    id: str
    name: str
    column_id: str
    description: str
    color: str
    total_seconds_estimate: int
    total_seconds_spent: int
    swimlane_id: Optional[str]
    position: Optional[int]
    number: Optional[int]
    responsible_user_id: Optional[str]
    points_estimate: Optional[float]
    grouping_date: Optional[date]
    labels: Optional[List[Label]]
