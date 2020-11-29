import pytest
import kanbanflow as kbf


def test_token_file_exists():
    # tokens should be stored in a token file
    assert kbf.token_file.exists()


def test_store_api_token():
    # given a token
    token = "sample-token"
    # and a name for that tokn
    name = "Sample Token"

    # when we store that token
    kbf.token_store(name=name, token=token)

    # then we should be able to retrieve the token by name
    retrieved_token = kbf.token_retrieve(name=name)

    assert retrieved_token == token

    # and when we delete that token
    kbf.token_delete(name=name)

    # that token should no longer exist
    with pytest.raises(KeyError):
        kbf.token_retrieve(name=name)
