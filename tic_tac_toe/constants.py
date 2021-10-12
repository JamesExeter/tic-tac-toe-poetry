# File containing all constants for the game

BOARD_SIZE = 3  # int, the size of the game board
MAX_TURNS = BOARD_SIZE * BOARD_SIZE  # int, the number of max turns to check for a draw
# in relation to the board size
EMPTY_BOARD_SYMBOL = " "  # str, for denoting the empty board character

CONVERSION_DICT = {
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
}  # dict of ints to tuple coordinates, think of row index in list of lists and then column index in list

PLAYER_SYMBOLS = ["X", "O"]

STARTING_BOARD = [[EMPTY_BOARD_SYMBOL] * BOARD_SIZE] * BOARD_SIZE # List of list of strings that denotes the initial board state