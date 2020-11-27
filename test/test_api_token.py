import pytest
import kanbanflow as kbf

def test_store_api_token():
    # given a token
    token = "sample-token"
    # and a name for that tokn
    name = "Sample Token"

    # when we store that token
    kbf.store_token(name=name, token=token)

    # then we should be able to retrieve the token by name
    retrieved_token = kbf.retrieve_token(name=name)

    assert retrieved_token == token

    # and token should be stored in file in home directory

    kanbanflow_token_file = kbf.token_file

    assert kanbanflow_token_file.exists()