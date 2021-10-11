# global dictionary to store which symbols are used for each player
from typing import List

"""
import Player
import Board
import Game_Controller
"""

def check_draw(elapsed_turns: int) -> bool:
    '''
    Checks if the game is a draw

        Parameters:
            elapsed_turns (int): a value representing the number of turns that have elapsed

        Returns:
            is_draw (bool): True if the game is a draw, False if it is not
    '''

    MAX_TURNS = 9
    try:
        elapsed_turns = int(elapsed_turns)
    except ValueError:
        print("int expected for comparison, something else recieved instead")

    is_draw = elapsed_turns == MAX_TURNS
    return is_draw

# unsure of how to test
def win_indexes(n: int) -> tuple[int, int]:
    '''
    Function to return the indexes of winning configurations in the board

        Parameters:
            n (int): the size of the board (n x n)

        Return:
            List[tuple(int, int)]: yields lists of coordinates that are required to win the game for any symbol
    '''
    if (n < 1):
        return []

    # Rows
    for r in range(n):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(n)]
    # Diagonal top left to bottom right
    yield [(i, i) for i in range(n)]
    # Diagonal top right to bottom left
    yield [(i, n - 1 - i) for i in range(n)]

def check_win(board: List[List[str]], symbol: str) -> bool:
    '''
    Checks if the game has been won by the player who made the last move

        Parameters:
            board (List of List of str): the current state of the board
            symbol (str): the symbol being checked for winning

        Return:
            (bool): True if the game has been won, False otherwise
    '''

    n = len(board)  # int, the size of the board
    # check n isn't too small
    if n > 2: 
        for indexes in win_indexes(n):
            if all(board[r][c] == symbol for r, c in indexes):
                return True

    return False

def translate_num_pad_to_coord(num: int) -> tuple[int, int]:
    '''
    Converts the valid number entered by the user for their move into a tuple 
    representing x and y coordinates

        Parameters:
            num (int): a number between 1 and 9 representing a board space

        Returns:
            coordinate (tuple (int, int)): a tuple containing the x and y index for the board of the move

    '''
    conversion_dict = {
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

    coordinate = None
    try:
        coordinate = conversion_dict[num]
    except KeyError:
        print("Invalid number for coordinate key")
        coordinate = -1
    except ValueError:
        print("Expected an int, recieved something else")
        coordinate = -1
    
    return coordinate

def check_valid_move(move_num: int, board: List[List[str]]) -> bool:
    '''
    Validates a made move by the user, checking that it is numeric and in the valid range

        Parameters:
            move_num (int): the entered move, representing a place in the board
            board (List of List of str): the current board state

        Return:
            is_valid (bool): True if the move is valid, False if invalid

    '''

    is_valid = False
    try:
        move_num = int(move_num)
        if (move_num > 0) and (move_num < 10):
            coordinate = translate_num_pad_to_coord(move_num)
            if board[coordinate[0]][coordinate[1]] == " ":
                is_valid = True
            else:
                print("That tile is already occupied!")
        else:
            print("Number entered outside the range: 1-9")
    except ValueError:
        print("You didn't enter a number!")

    return is_valid

def print_board(board: List[List[str]]) -> str:
    '''
    Prints the current board

        Parameters:
            board (List of List of str): the current board state

        Returns:
            printed_board (str): the string output of the board

    '''
    printed_board = f"""
    -------------
    | {board[0][0]} | {board[0][1]} | {board[0][2]} |
    -------------
    | {board[1][0]} | {board[1][1]} | {board[1][2]} |
    -------------
    | {board[2][0]} | {board[2][1]} | {board[2][2]} |
    -------------
    """
    return printed_board

def update_board(board: List[List[str]], x: int, y: int, sym: str) -> List[List[str]]:
    '''
    Updates the board to include the previously made move after it has been validated

        Parameters:
            board (List of List of str): the board state prior to the move
            x (int): the x coordinate of the move
            y (int): the y coordinate of the move
            sym (str): the symbol to be entered into the board

        Returns:
            board (List of List of str): the new updated board
    '''

    if type(sym) == str:
        if len(sym) == 1:
            try:
                board[x][y] = sym
            except IndexError:
                print("Coordinates out of bounds")
            except ValueError:
                print("Coordinate values provided are invalid")
            except TypeError:
                print("Coordinate values provided are invalid")
        else:
            print("Symbol was not one character long")
    else:
        print("Symbol provided was not a string")

    return board

def move(symbol: str, cur_board: List[List[str]]) -> List[List[str]]:
    '''
    Processes a player move, gets their input, validates it and then updates the board
    The move entered must be between 1 and 9 inclusive

        Parameters:
            symbol (str): a symbol that denotes the current player
            cur_board (List of List of str): represents the current state of the board

        Returns:
            new_board (List of List of str): new state of the board, or
            cur_board (List of List of str): returns old board in case of error
    '''

    is_valid_move = False
    player_move = ""
    while not is_valid_move:
        print(f"\nYour move, player {symbol}")
        player_move = input("Enter the tile number: ")
        is_valid_move = check_valid_move(player_move, cur_board)

    coordinate = translate_num_pad_to_coord(int(player_move))
    if coordinate == -1:
        print("Problem converting to coordinate")
        return move(symbol, cur_board)
    
    new_board = update_board(cur_board, coordinate[0], coordinate[1], symbol)

    return new_board

def user_setup() -> dict:
    '''
    Function allows users to select which symbol they play as out of X and O

        Parameters:
            None

        Returns:
            player_syms (dict): a dictionary that maps each player to their respective symbols
    '''

    is_valid = False
    first_player_piece = ""
    second_player_piece = ""
    choices = ["X", "O"]

    while not is_valid:
        first_player_piece = input("Choose your piece, Player 1 (X | O): ")
        if first_player_piece.upper() in choices:
            is_valid = True
        else:
            print("Pick either X or O")

    choices.remove(first_player_piece)
    second_player_piece = choices[0]
    players_dict = {
        1: first_player_piece,
        2: second_player_piece
    }

    return players_dict

def play_game() -> None:
    '''
    Function to play a singular game to the end
    Requires that a flag is updated that denotes the current player for each move
    After each turn, the board is checked to see if the game has been won

        Parameters:
            None
        Returns:
            None
    '''
    TURN_NUM = 1      # int, denoting the number of turns that have elapsed
    cur_player = None      # bool, denotes current players
    is_player_1 = True     # bool, for denoting if the current player is player 1
    is_won = False         # bool, for whether the game has been won or not
    is_draw = False        # bool, for whether the game is a draw or not
    BOARD = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]                      # List of list of strings that denote the current board state

    # should be a dictionary with an int key and string value
    PLAYER_SYMBOLS = user_setup()

    print("Initial board: ")
    print(print_board(BOARD) + "\n")

    while (not is_won) and (not is_draw):
        if is_player_1:
            cur_player = 1
        else:
            cur_player = 2

        # string representing the symbol of the current player
        symbol = PLAYER_SYMBOLS[cur_player]
        board = move(symbol, BOARD)
        BOARD = board

        print("Current board: ")
        print(print_board(BOARD) + "\n")

        is_won = check_win(board, symbol)
        is_draw = check_draw(TURN_NUM)

        if is_won:
            print(f"Congratulations Player {cur_player}, you won!")
        elif is_draw:
            print("No one wins!")
        else:
            is_player_1 = not is_player_1
            TURN_NUM += 1

if __name__ == "__main__":
    '''
    Main entry point into the game
    Initialises flags and plays game infinitely until user says no
    '''

    print("Welcome to Tic Tac Toe!")
    print("You know the drill of how this works, player 1 is X, player 2 is O")
    print("When making a move, the grid is layed out as so:")
    print("""
    7 | 8 | 9
    ---------
    4 | 5 | 6
    ---------
    1 | 2 | 3
    """)
    print("So when making a move, enter a number from 1 to 9")
    print("\n\n------------------------- GAME ON --------------------------\n\n")

    play = True
    while play:
        play_game()
        is_play = input("\nPlay again (y | n)? ")
        if is_play.lower() in ["n", "no"]:
            play = False
        elif is_play.lower() in ["y", "yes"]:
            pass
        else:
            print("Please retry")

    print("Goodbye!")
