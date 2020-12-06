import pytest
import kanbanflow as kbf


@pytest.fixture
def task_id() -> str:
    return


def test_task():
    task_id = "ut8vFak3"

    token = kbf.TokenManager().retrieve("kanbanflow-test-board")
    session = kbf.Session(token)

    task = session.get_task(id=task_id)
    expected_task = kbf.Task.parse_obj(
        {
            "_id": "ut8vFak3",
            "name": "Sample task",
            "description": "This is a sample task.",
            "color": "yellow",
            "columnId": "jFZt2lBzBuff",
            "totalSecondsSpent": 0,
            "totalSecondsEstimate": 0,
            "swimlaneId": "sOgu8h57TiP1",
        }
    )

    assert expected_task == task
