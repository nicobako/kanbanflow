from .base_model import BaseModel
from typing import List


class Entry(BaseModel):
    unique_id:str
    name:str

class Column(Entry):
    pass

class Swimlane(Entry):
    pass

class Color(BaseModel):
    name:str
    value:str
    description:str

class Board(BaseModel):
    id:str
    name:str
    columns:List[Column]
    swimlanes:List[Swimlane]
    colors:List[Color]