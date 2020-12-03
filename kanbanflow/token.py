from pathlib import Path
import json
from typing import List, Dict

token_file = Path.home() / ".kanbanflow/token.json"

if not token_file.exists():
    token_file.parent.mkdir(parents=True, exist_ok=True)
    with open(token_file, "w") as tf:
        json.dump({}, tf)

Tokens = Dict[str, str]


def _load_tokens() -> Tokens:
    with open(token_file) as tf:
        tokens = json.load(tf)
    return tokens


def _write_tokens(tokens: Tokens):
    with open(token_file, "w") as tf:
        json.dump(tokens, tf)


def token_store(
    *,
    name: str,
    token: str,
) -> None:
    tokens = _load_tokens()

    tokens[name] = token

    _write_tokens(tokens)


def token_retrieve(
    *,
    name: str,
) -> str:
    tokens = _load_tokens()

    return tokens[name]


def token_delete(
    *,
    name: str,
) -> None:
    tokens = _load_tokens()

    tokens.pop(name)

    _write_tokens(tokens)


def token_list() -> List[str]:
    tokens = _load_tokens()

    return list(tokens.keys())
