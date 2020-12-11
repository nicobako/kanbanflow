"""Defines the TokenManager class."""

from pathlib import Path
from typing import Optional, Dict, List
import json

Tokens = Dict[str, str]


class TokenManager:
    """API token manager.

    The TokenManager class is a simple way of storing API tokens.
    It is similar to a simple password manager.
    A name is associated with every API token,
    and API tokens are stored and retrieved by their name.

    Parameters
    ----------
    token_file: Optional Path
        An optional path to store the tokens in.
        Defaults to ``~/.kanbanflow/tokens.json``.
    """

    def __init__(self, token_file: Path = Path.home() / ".kanbanflow/tokens.json"):
        """Construct a TokenManager."""

        self.token_file = Path(token_file)

        self._tokens: Tokens = {}

        if not self.token_file.exists():
            self._create_file()
        else:
            self._load_tokens()

    def _create_file(self):
        """Create the token file if it doesn't exist."""
        parent_dir = self.token_file.parent
        parent_dir.mkdir(
            parents=True,
            exist_ok=True,
        )
        self._write_tokens()

    def _write_tokens(self):
        """Write the current tokens to the file."""
        with open(self.token_file, "w") as tf:
            json.dump(self._tokens, tf)

    def _load_tokens(self):
        """Load the tokens from the file."""
        with open(self.token_file, "r") as tf:
            self._tokens = json.load(tf)

    def clear(self):
        """Clear any stored tokens."""
        self._tokens = {}
        self._write_tokens()

    def store(self, name, token):
        """Store a token.

        Parameters
        ----------
        name: str
            The name of the token to store.
            If this token already exists it gets reset.

        token: str
            The API token.
        """
        self._load_tokens()
        self._tokens[name] = token
        self._write_tokens()

    def retrieve(self, name):
        """Retrieve an API token.

        Parameters
        ----------
        name: str
            The name of the token to retrieve.

        Raises
        ------
        KeyError if the name does not exist.
        """
        self._load_tokens()
        return self._tokens[name]

    def remove(self, name: str):
        """Remove a token by name."""
        self._load_tokens()
        self._tokens.pop(name)
        self._write_tokens()

    def names(self) -> List[str]:
        """Get a list of all stored names."""
        return list(self._tokens.keys())
