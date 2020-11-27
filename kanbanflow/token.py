from pathlib import Path
import json

token_file = Path.home() / ".kanbanflow/token.json"

if not token_file.exists():
    token_file.parent.mkdir(parents=True)
    with open(token_file, "w") as tf:
        json.dump({}, tf)


def token_store(
    *,
    name: str,
    token: str,
) -> None:
    with open(token_file) as tf:
        tokens = json.load(tf)

    tokens[name] = token

    with open(token_file, "w") as tf:
        json.dump(tokens, tf)


def token_retrieve(
    *,
    name: str,
) -> str:
    with open(token_file) as tf:
        tokens = json.load(tf)

    return tokens[name]


def token_delete(
    *,
    name: str,
) -> None:
    with open(token_file) as tf:
        tokens = json.load(tf)

    tokens.pop(name)

    with open(token_file, "w") as tf:
        json.dump(tokens, tf)
