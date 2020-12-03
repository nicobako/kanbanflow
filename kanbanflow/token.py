"""Contains all logic for storing and retrieving tokens."""

from pathlib import Path
import json
from typing import List, Dict, Optional

_token_file = Path.home() / ".kanbanflow/token.json"

Tokens = Dict[str, str]


def token_file(new_path: Optional[Path] = None) -> Path:
    """Get or set the token file."""
    global _token_file

    if new_path:
        _token_file = Path(new_path)

    return _token_file


def _create_token_file_if_not_exists():
    """Create the token file if it does not exist."""
    if not token_file().exists():
        token_file().parent.mkdir(parents=True, exist_ok=True)
        with open(token_file(), "w") as tf:
            json.dump({}, tf)


def _load_tokens() -> Tokens:
    """Load all tokens stored in the token file."""
    _create_token_file_if_not_exists()

    with open(token_file()) as tf:
        tokens = json.load(tf)
    return tokens


def _write_tokens(tokens: Tokens):
    """Write tokens to the token file."""
    with open(token_file(), "w") as tf:
        json.dump(tokens, tf)


def token_store(
    *,
    name: str,
    token: str,
) -> None:
    """Store a token by name."""
    tokens = _load_tokens()

    tokens[name] = token

    _write_tokens(tokens)


def token_retrieve(
    *,
    name: str,
) -> str:
    """Retrieve a token by name."""
    tokens = _load_tokens()

    return tokens[name]


def token_list() -> List[str]:
    """List all tokens."""
    tokens = _load_tokens()

    return list(tokens.keys())


def token_delete(
    *,
    name: str,
) -> None:
    """Delete a token by name."""
    tokens = _load_tokens()

    tokens.pop(name)

    _write_tokens(tokens)
