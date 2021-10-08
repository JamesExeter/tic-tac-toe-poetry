from typing import List
from tic_tac_toe import __version__
from tic_tac_toe import game
import pytest

@pytest.fixture
def example_empty_board() -> List[List[str]]:
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    return board

@pytest.fixture
def example_win_board_x_horizontal() -> List[List[str]]:
    board = [
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", "X", "O"]
    ]

    return board

@pytest.fixture
def example_win_board_o_vertical() -> List[List[str]]:
    board = [
        ["O", "X", "X"],
        ["O", " ", " "],
        ["O", "X", "O"]
    ]

    return board

@pytest.fixture
def example_win_board_o_diag() -> List[List[str]]:
    board = [
            ["O", "X", "X"],
            ["O", "O", " "],
            [" ", "X", "O"]
        ]

    return board

@pytest.fixture
def example_draw_board() -> List[List[str]]:
    board = [
            ["O", "X", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]

    return board

@pytest.fixture
def expected_print_board() -> str:
    board_str = """
    -------------
    | O | X | X |
    -------------
    | O | O |   |
    -------------
    |   | X | O |
    -------------
    """
    return board_str

@pytest.fixture
def expected_print_board_empty() -> str:
    board_str = """
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    """
    return board_str

def test_check_draw_true():
    assert game.check_draw(9) == True

def test_check_draw_false():
    assert game.check_draw(6) == False

def test_print_board(example_win_board_o_diag: List[List[str]], expected_print_board: str):
    printed_board = game.print_board(example_win_board_o_diag)
    assert printed_board == expected_print_board

def test_print_empty_board(example_empty_board: List[List[str]], expected_print_board_empty: str):
    printed_board = game.print_board(example_empty_board)
    assert printed_board == expected_print_board_empty

def test_version():
    assert __version__ == '0.1.0'
