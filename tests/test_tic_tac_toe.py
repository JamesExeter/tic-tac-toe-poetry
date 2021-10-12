from typing import List
from unittest import mock
from tic_tac_toe import __version__
from tic_tac_toe import game
import pytest
from unittest.mock import patch, call

# FIXTURES HERE


@pytest.fixture
def example_empty_board() -> List[List[str]]:
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    return board


@pytest.fixture
def example_win_board_x_horizontal() -> List[List[str]]:
    board = [["X", "X", "X"], ["O", "O", " "], [" ", "X", "O"]]

    return board


@pytest.fixture
def example_win_board_o_vertical() -> List[List[str]]:
    board = [["O", "X", "X"], ["O", " ", " "], ["O", "X", "O"]]

    return board


@pytest.fixture
def example_win_board_o_diag() -> List[List[str]]:
    board = [["O", "X", "X"], ["O", "O", " "], [" ", "X", "O"]]

    return board


@pytest.fixture
def example_win_board_x_diag() -> List[List[str]]:
    board = [[" ", "X", "X"], ["O", "X", " "], ["X", " ", "O"]]

    return board


@pytest.fixture
def example_draw_board() -> List[List[str]]:
    board = [["O", "X", "X"], ["X", "O", "O"], ["O", "X", "X"]]

    return board


@pytest.fixture
def example_midgame_board() -> List[List[str]]:
    board = [["O", "X", " "], ["X", " ", "O"], ["O", "X", "X"]]

    return board


@pytest.fixture
def example_midgame_board_after_move() -> List[List[str]]:
    board = [["O", "X", " "], ["X", "O", "O"], ["O", "X", "X"]]

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


def test_indices_calc():
    indexes = list(game.win_indexes(2))
    assert indexes == [
        [(0, 0), (0, 1)],
        [(1, 0), (1, 1)],
        [(0, 0), (1, 0)],
        [(0, 1), (1, 1)],
        [(0, 0), (1, 1)],
        [(0, 1), (1, 0)],
    ]


def test_indices_bad_board():
    indexes = list(game.win_indexes(0))
    assert indexes == []


def test_translate_function():
    coord = game.translate_num_pad_to_coord(1)
    assert coord == (2, 0)


def test_translate_function_out_of_bounds_low():
    coord = game.translate_num_pad_to_coord(0)
    assert coord == -1


def test_translate_function_out_of_bounds_high():
    coord = game.translate_num_pad_to_coord(10)
    assert coord == -1


def test_translate_function_string_entered():
    coord = game.translate_num_pad_to_coord("gh")
    assert coord == -1


def test_translate_function_given_float():
    coord = game.translate_num_pad_to_coord(3.4)
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


def test_check_valid_move_float_input(example_midgame_board: List[List[str]]):
    bool_res = game.check_valid_move("3.5", example_midgame_board)
    assert bool_res == False


def test_update_board(example_midgame_board, example_midgame_board_after_move):
    updated_board = game.update_board(example_midgame_board, 1, 1, "O")
    assert updated_board == example_midgame_board_after_move


def test_update_board_incorrect(
    example_midgame_board, example_midgame_board_after_move
):
    updated_board = game.update_board(example_midgame_board, 1, 1, "X")
    assert updated_board != example_midgame_board_after_move


def test_update_board_out_of_bounds(
    example_midgame_board, example_midgame_board_after_move
):
    updated_board = game.update_board(example_midgame_board, 3, 1, "O")
    assert updated_board != example_midgame_board_after_move


def test_update_board_float_x(example_midgame_board, example_midgame_board_after_move):
    updated_board = game.update_board(example_midgame_board, 3.4, 1, "O")
    assert updated_board != example_midgame_board_after_move


def test_update_board_float_y(example_midgame_board, example_midgame_board_after_move):
    updated_board = game.update_board(example_midgame_board, 3, 1.4, "O")
    assert updated_board != example_midgame_board_after_move


def test_update_board_float_x_y(
    example_midgame_board, example_midgame_board_after_move
):
    updated_board = game.update_board(example_midgame_board, 3.4, 1.4, "O")
    assert updated_board != example_midgame_board_after_move


def test_update_board_str_x(example_midgame_board, example_midgame_board_after_move):
    updated_board = game.update_board(example_midgame_board, "b", 1, "O")
    assert updated_board != example_midgame_board_after_move


def test_update_board_str_y(example_midgame_board, example_midgame_board_after_move):
    updated_board = game.update_board(example_midgame_board, 3, "j", "O")
    assert updated_board != example_midgame_board_after_move


def test_update_board_str_x_y(example_midgame_board, example_midgame_board_after_move):
    updated_board = game.update_board(example_midgame_board, "j", "hfd", "O")
    assert updated_board != example_midgame_board_after_move


def test_update_board_symbol_not_str(
    example_midgame_board, example_midgame_board_after_move
):
    updated_board = game.update_board(example_midgame_board, 3, 1, 0)
    assert updated_board != example_midgame_board_after_move


def test_update_board_symbol_empty(
    example_midgame_board, example_midgame_board_after_move
):
    updated_board = game.update_board(example_midgame_board, 3, 1, "")
    assert updated_board != example_midgame_board_after_move


def test_update_board_symbol_longer_than_one_char(
    example_midgame_board, example_midgame_board_after_move
):
    updated_board = game.update_board(example_midgame_board, 3, 1, "OX")
    assert updated_board != example_midgame_board_after_move


def test_win_small_board():
    small_board = [["X", "O"], [" ", " "]]

    assert game.check_win(small_board, "X") == False


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


def test_check_draw_not_a_number():
    assert game.check_draw("st") == False


def test_check_draw_negative():
    assert game.check_draw(-5) == False


def test_check_draw_float_input():
    assert game.check_draw(6.3) == False


def test_print_board(
    example_win_board_o_diag: List[List[str]], expected_print_board: str
):
    printed_board = game.print_board(example_win_board_o_diag)
    assert printed_board == expected_print_board


def test_print_empty_board(
    example_empty_board: List[List[str]], expected_print_board_empty: str
):
    printed_board = game.print_board(example_empty_board)
    assert printed_board == expected_print_board_empty


# MOCKING TESTS


@patch("builtins.input", return_value="X")
def test_user_setup_X(mock_input):
    player_choice = game.user_setup()
    expected_dict = {1: "X", 2: "O"}

    assert player_choice == expected_dict


@patch("builtins.input", return_value="O")
def test_user_setup_O(mock_input):
    player_choice = game.user_setup()
    expected_dict = {1: "O", 2: "X"}

    assert player_choice == expected_dict


@patch("builtins.input", return_value="4")
def test_move_valid_on_empty(mock_input, example_empty_board: List[List[str]]):
    player_move = game.move("X", example_empty_board)
    expected_board = [[" ", " ", " "], ["X", " ", " "], [" ", " ", " "]]

    assert player_move == expected_board


@patch("builtins.input", return_value="9")
def test_move_valid_on_empty_o(mock_input, example_empty_board: List[List[str]]):
    player_move = game.move("O", example_empty_board)
    expected_board = [[" ", " ", "O"], [" ", " ", " "], [" ", " ", " "]]

    assert player_move == expected_board


@patch("builtins.input")
def test_invalid_moves_on_empty_board_x(
    mock_input, example_empty_board: List[List[str]]
):
    mock_input.side_effect = ["-1", "gh", "4.3", 5]
    player_move_result = game.move("X", example_empty_board)
    expected_board = [[" ", " ", " "], [" ", "X", " "], [" ", " ", " "]]

    assert player_move_result == expected_board


@patch("builtins.input")
def test_invalid_moves_on_midgame_board_o(
    mock_input,
    example_midgame_board: List[List[str]],
    example_midgame_board_after_move: List[List[str]],
):
    mock_input.side_effect = ["-1", "gh", "4.3", 4, 5]
    player_move_result = game.move("O", example_midgame_board)

    assert player_move_result == example_midgame_board_after_move


@patch("builtins.input")
def test_play_game_func_win_game_x(mock_input):
    mock_input.side_effect = ["X", "1", "4", "2", "4", "5", "3"]
    assert game.play_game() == None


@patch("builtins.input")
def test_play_game_func_win_game_x_lots_of_bad_inputs(mock_input):
    mock_input.side_effect = ["X", "1", "4", "2", "4", "5", "3"]
    assert game.play_game() == None


@patch("builtins.input")
def test_play_game_func_win_game_o_lots_of_bad_inputs(mock_input):
    mock_input.side_effect = ["O", "gh", "1", "-4", "4", "20", "2", "4", "5", "3"]
    assert game.play_game() == None


@patch("builtins.input")
def test_play_game_func_draw_game_o(mock_input):
    mock_input.side_effect = ["O", "7", "4", "8", "9", "6", "5", "1", "3", "2"]
    assert game.play_game() == None


@patch("builtins.input")
def test_main_func_win_game_x_play_once(mock_input):
    mock_input.side_effect = ["X", "1", "4", "2", "4", "5", "3", "hi", "no"]
    assert game.main() == None


@patch("builtins.input")
def test_main_func_win_game_x_play_twice(mock_input):
    mock_input.side_effect = ["X","1","4","2","4","5","3","Yes","O","7","1","8","1","2","9","no"]
    assert game.main() == None


@patch("builtins.input")
def test_main_func_draw_game_o(mock_input):
    mock_input.side_effect = ["O", "7", "4", "8", "9", "6", "5", "1", "3", "2", "no"]
    assert game.play_game() == None


# PARAMETERIZE


@pytest.mark.parametrize(
    "test_input, expected",
    [
        [([["X", "X", "X"], ["O", " ", "O"], [" ", "O", " "]], "X"), True],
        [([["X", " ", " "], ["X", "O", "O"], ["X", " ", " "]], "X"), True],
        [([["X", " ", " "], ["O", "X", "O"], [" ", " ", "X"]], "X"), True],
        [([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "X"), True],
    ],
)
def test_win_x_boards(test_input, expected):
    assert game.check_win(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        [([["O", "O", "O"], ["X", " ", "X"], [" ", "X", " "]], "O"), True],
        [([["O", " ", " "], ["O", "X", "X"], ["O", " ", " "]], "O"), True],
        [([["O", " ", " "], ["X", "O", "X"], [" ", " ", "O"]], "O"), True],
        [([["X", " ", "O"], ["X", "O", " "], ["O", " ", " "]], "O"), True],
    ],
)
def test_win_o_boards(test_input, expected):
    assert game.check_win(test_input[0], test_input[1]) == expected
