"""Definition for the kanbanflow.Session class."""

import requests
from requests.auth import HTTPBasicAuth
from typing import Optional
from .board import Board
from .task import Task


class Session:
    """A KanbanFlow session."""

    def __init__(self, token: str):
        """Construct a Session."""
        self._token = token
        self._auth = HTTPBasicAuth("apiToken", self._token)
        self._base_url = "https://kanbanflow.com/api/v1"
        self._board_url = f"{self._base_url}/board"
        self._task_url = f"{self._base_url}/tasks"

    def board(self) -> Board:
        """Retrieve the board."""
        board_req = requests.get(self._board_url, auth=self._auth)
        print(board_req.json())
        return Board.parse_obj(board_req.json())

    def get_task(self, *, id: Optional[str]):
        if id:
            task_url = f"{self._task_url}/{id}"
            task_req = requests.get(task_url, auth=self._auth)
            return Task.parse_obj(task_req.json())
