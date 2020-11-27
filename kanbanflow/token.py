from pathlib import Path
import json

token_file = Path.home() / ".kanbanflow/token.json"

if not token_file.exists():
    token_file.parent.mkdir(parents=True)
    with open(token_file, "w") as tf:
        json.dump({"tokens": []}, tf)


def store_token(
    *,
    name: str,
    token: str,
) -> None:
    with open(token_file) as tf:
        tokens = json.load(tf)
        tokens["tokens"].append({"name": name, "token": token})

    with open(token_file, "w") as tf:
        json.dump(tokens, tf)


def retrieve_token(
    *,
    name: str,
) -> str:
    with open(token_file) as tf:
        tokens = json.load(tf)
        token = next(filter(lambda tok: tok["name"] == name, tokens["tokens"]))
        return token["token"]
