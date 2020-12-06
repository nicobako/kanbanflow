"""Definition for the kanbanflow.Session class."""

import requests
from requests.auth import HTTPBasicAuth

from .board import Board


class Session:
    """A KanbanFlow session."""

    def __init__(self, token: str):
        """Construct a Session."""
        self._token = token
        self._auth = HTTPBasicAuth("apiToken", self._token)
        self._base_url = "https://kanbanflow.com/api/v1"
        self._board_url = f"{self._base_url}/board"

    def board(self) -> Board:
        """Retrieve the board."""
        board_req = requests.get(self._board_url, auth=self._auth)
        print(board_req.json())
        return Board(**board_req.json())
