import pytest
import kanbanflow as kbf

def test_board():
    token_manager = kbf.TokenManager()
    token = token_manager.retrieve("kanbanflow-test-board")

    session = kbf.Session(token)
    board = session.board()
    print(board)