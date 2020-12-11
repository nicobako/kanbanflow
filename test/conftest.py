import pytest
import kanbanflow as kbf


@pytest.fixture(scope="session")
def kbf_token_name() -> str:
    return "kanbanflow-test-board"


@pytest.fixture(scope="session")
def kbf_token_manager(kbf_token_name) -> kbf.TokenManager:
    tm = kbf.TokenManager()
    print(tm.names())
    assert kbf_token_name in tm.names()
    return tm


@pytest.fixture(scope="session")
def kbf_token(kbf_token_manager, kbf_token_name):
    return kbf_token_manager.retrieve(kbf_token_name)


@pytest.fixture(scope="session")
def kbf_session(kbf_token) -> kbf.Session:
    return kbf.Session(kbf_token)
