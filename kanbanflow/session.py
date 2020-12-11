"""Definition for the kanbanflow.Session class."""

import requests
from requests.auth import HTTPBasicAuth
from typing import Optional
from .board import Board, Column, Swimlane
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

        self._board = self._get_board()

    @property
    def board(self):
        return self._board

    
    def _get_board(self) -> Board:
        """Retrieve the board."""
        board_req = requests.get(self._board_url, auth=self._auth)
        return Board.parse_obj(board_req.json())


    def get_task(self, *, id: str):
        """Retrive one task."""

        task_url = f"{self._task_url}/{id}"
        task_req = requests.get(task_url, auth=self._auth)
        return Task.parse_obj(task_req.json())

    def create_task(self, name:str, column:Column, swimlane:Optional[Swimlane]=None)->str:
        """Create a task."""

        data = {
            "name":name,
            "columnId":column.id,
        }

        if swimlane:
            data["swimlaneId"] = swimlane.id

        print("data", data)

        post = requests.post(self._task_url, data=data, auth=self._auth)

        task_id = post.json()["taskId"]

        return task_id
