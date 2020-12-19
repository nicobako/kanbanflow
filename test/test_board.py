import pytest
import kanbanflow as kbf


def test_board(kbf_session):
    board = kbf_session.board
    expected_board = kbf.Board.parse_obj(
        {
            "_id": "yM2tQft",
            "name": "Python KanbanFlow Test Board",
            "columns": [
                {"uniqueId": "jFZt2lBzBuff", "name": "To-do"},
                {"uniqueId": "jGbgYjlPTUxE", "name": "Do today"},
                {"uniqueId": "jHiCcJglztj8", "name": "In progress"},
                {"uniqueId": "jIzYm0iRzZ81", "name": "Done"},
            ],
            "colors": [
                {"name": "Yellow", "value": "yellow"},
                {"name": "Green", "value": "green"},
                {"name": "Blue", "value": "blue"},
                {"name": "Red", "value": "red"},
                {"name": "Orange", "value": "orange"},
                {"name": "Purple", "value": "purple"},
                {"name": "Magenta", "value": "magenta"},
                {"name": "Cyan", "value": "cyan"},
            ],
            "swimlanes": [
                {"uniqueId": "sOgu8h57TiP1", "name": "top"},
                {"uniqueId": "sPqYCUNLhjEf", "name": "bottom"},
            ],
        }
    )
    assert board == expected_board
