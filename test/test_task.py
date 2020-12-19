import pytest
import kanbanflow as kbf


@pytest.fixture
def task_id() -> str:
    return "ut8vFak3"


def test_task(kbf_session, task_id):
    task = kbf_session.get_task(id=task_id)
    expected_task = kbf.Task.parse_obj(
        {
            "_id": "ut8vFak3",
            "name": "Sample task",
            "description": "This is an example of a sample task.",
            "color": "yellow",
            "columnId": "jFZt2lBzBuff",
            "totalSecondsSpent": 0,
            "totalSecondsEstimate": 0,
            "swimlaneId": "sOgu8h57TiP1",
            "labels": [{"name": "Urgent", "pinned": "false"}],
        }
    )

    assert expected_task == task
