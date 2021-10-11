from typing import List
from tic_tac_toe import __version__
from tic_tac_toe import game
import pytest

# FIXTURES HERE

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
def example_win_board_x_diag() -> List[List[str]]:
    board = [
            [" ", "X", "X"],
            ["O", "X", " "],
            ["X", " ", "O"]
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
def example_midgame_board() -> List[List[str]]:
    board = [
            ["O", "X", " "],
            ["X", " ", "O"],
            ["O", "X", "X"]
        ]

    return board

@pytest.fixture
def example_midgame_board_after_move() -> List[List[str]]:
    board = [
            ["O", "X", " "],
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

# TESTS HERE

def test_translate_function():
    coord = game.translate_num_pad_to_coord(1)
    assert coord == (2, 0)

def test_translate_function_bad_input():
    coord = game.translate_num_pad_to_coord(0)
    assert coord == -1

def test_check_valid_move_is_valid(example_midgame_board: List[List[str]]):
    bool_res = game.check_valid_move("5", example_midgame_board)
    assert bool_res == True

def test_check_valid_move_not_a_number(example_midgame_board: List[List[str]]):
    bool_res = game.check_valid_move("gh", example_midgame_board)
    assert bool_res == False

def test_check_valid_move_oob(example_midgame_board: List[List[str]]):
    bool_res = game.check_valid_move("-9", example_midgame_board)
    assert bool_res == False

def test_check_valid_move_occupied_tile(example_midgame_board: List[List[str]]):
    bool_res = game.check_valid_move("4", example_midgame_board)
    assert bool_res == False

def test_update_board(example_midgame_board, example_midgame_board_after_move):
    updated_board = game.update_board(example_midgame_board, 1, 1, "O")
    assert updated_board == example_midgame_board_after_move

def test_update_board_incorrect(example_midgame_board, example_midgame_board_after_move):
    updated_board = game.update_board(example_midgame_board, 1, 1, "X")
    assert updated_board != example_midgame_board_after_move

def test_update_board_out_of_bounds(example_midgame_board, example_midgame_board_after_move):
    updated_board = game.update_board(example_midgame_board, 3, 1, "O")
    assert updated_board == example_midgame_board

def test_win_row(example_win_board_x_horizontal: List[List[str]]):
    assert game.check_win(example_win_board_x_horizontal, "X") == True

def test_win_col(example_win_board_o_vertical: List[List[str]]):
    assert game.check_win(example_win_board_o_vertical, "O") == True

def test_win_diag(example_win_board_o_diag: List[List[str]]):
    assert game.check_win(example_win_board_o_diag, "O") == True

def test_win_diag_other_direction(example_win_board_x_diag: List[List[str]]):
    assert game.check_win(example_win_board_x_diag, "X") == True

def test_win_false_for_draw(example_draw_board: List[List[str]]):
    assert game.check_win(example_draw_board, "X") == False

def test_win_false_for_draw_2(example_draw_board: List[List[str]]):
    assert game.check_win(example_draw_board, "O") == False

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
