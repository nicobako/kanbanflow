"""Definition for the kanbanflow.Board class..."""

from .base_model import BaseModel
from typing import List, Optional
import pydantic


class Entry(BaseModel):
    """An item with a name and unique id."""

    id: str = pydantic.Field(alias="uniqueId")
    name: str


class Column(Entry):
    """A column."""

    pass


class Swimlane(Entry):
    """A swimlane."""

    pass


class Color(BaseModel):
    """A color."""

    name: str
    value: str
    description: Optional[str]


class Board(BaseModel):
    """A board."""

    id: str
    name: str
    columns: List[Column]
    swimlanes: Optional[List[Swimlane]]
    colors: List[Color]
