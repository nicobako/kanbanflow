import pytest
import kanbanflow as kbf

@pytest.fixture
def task():
    token_manager = kbf.TokenManager()
    api_token = token_manager.retrieve(name="kanbanflow-test-board")
    
def test_task(task):
    assert True
