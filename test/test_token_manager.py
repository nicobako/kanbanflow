import pytest
import kanbanflow as kbf
from pathlib import Path


def test_default_token_file():
    token_manager = kbf.TokenManager()
    assert Path.home() / ".kanbanflow/tokens.json" == token_manager.token_file


@pytest.fixture(params=[Path("token-file.json"), Path("sample-token-file.json")])
def token_file(request):
    tf = request.param
    assert not tf.exists()
    yield tf
    tf.unlink()


@pytest.fixture()
def token_manager(token_file):
    # Given a token manager
    token_manager = kbf.TokenManager(token_file)

    # the token file should be stored correctly
    assert token_file == token_manager.token_file

    # tests should revert the token manager back to its original state
    original_names = token_manager.names()

    yield token_manager

    assert original_names == token_manager.names()


def test_token_manager(token_manager):
    assert token_manager.token_file.exists()

    # given a token
    name = "a name"
    token = "a token"

    # and I store the token
    token_manager.store(name=name, token=token)

    # when I retrive the token

    # then the retrieved token should be correct
    retrieved_token = token_manager.retrieve(name=name)

    # and when I overwrite the token with the same name
    new_token = "new token"
    token_manager.store(name=name, token=new_token)

    # then I should get the new token when I retrieve it
    assert new_token == token_manager.retrieve(name=name)

    # and when I ask for a name that doesn't exist
    # then it should raise an exception
    with pytest.raises(KeyError):
        token_manager.retrieve(name="nonexistant")

    # and when I get a list of existing tokens
    assert name in token_manager.names()

    # and when I remove a token by name
    token_manager.remove(name=name)

    # then the token should no longer exist
    assert name not in token_manager.names()

    # and when I clear the token manager
    token_manager.clear()

    # then there should be no more tokens
    assert 0 == len(token_manager.names())
