# global dictionary to store which symbols are used for each player
from typing import List

PLAYER_SYMBOLS = {
    1: 'X',
    2: 'O'
}   # should be a dictionary with an int key and string value

def check_draw(board: List[List[str]]) -> bool:
    '''
    Checks if the game is a draw

        Parameters:
            board (List of List of str): the current state of the board

        Returns:
            is_draw (bool): True if the game is a draw, False if it is not
    '''
    pass

def check_win(board: List[List[str]]) -> bool:
    '''
    Checks if the game has been won by the player who made the last move

        Parameters:
            board (List of List of str): the current state of the board
        
        Return:
            has_won (bool): True if the game has been won, False otherwise
    '''
    return False

def check_valid_move(move_num: int) -> bool:
    '''
    Validates a made move by the user, checking that it is numeric and in the valid range

        Parameters:
            move_num (int): the entered move, representing a place in the board

        Return:
            is_valid (bool): True if the move is valid, False if invalid

    '''
    pass

def print_board(board: List[List[str]]) -> None:
    '''
    Prints the current board

        Parameters:
            board (List of List of str): the current board state

        Returns:
            None

    '''
    pass

def update_board(old_board: List[List[str]], x: int, y: int, sym: str) -> List[List[str]]:
    '''
    Updates the board to include the previously made move after it has been validated

        Parameters:
            old_board (List of List of str): the board state prior to the move
            x (int): the x coordinate of the move
            y (int): the y coordinate of the move
            sym (str): the symbol to be entered into the board

        Returns:
            new_board (List of List of str): the new updated board
    '''
    pass

def translate_num_pad_to_coord(num: int) -> tuple(int, int):
    '''
    Converts the valid number entered by the user for their move into a tuple 
    representing x and y coordinates

        Parameters:
            num (int): a number between 1 and 9 representing a board space
        
        Returns:
            coordinate (tuple (int, int)): a tuple containing the x and y index for the board of the move

    '''
    pass

def move(symbol: str, cur_board: List[List[str]]) -> List[List[str]]:
    '''
    Processes a player move, gets their input, validates it and then updates the board
    The move entered must be between 1 and 9 inclusive

        Parameters:
            symbol (str): a symbol that denotes the current player
            cur_board (List of List of str): represents the current state of the board

        Returns:
            new_board (List of List of str): new state of the board
    '''
    return cur_board

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
    cur_player = None      # denotes current players, should be bool
    is_player_1 = True     # boolean for denoting if the current player is player 1
    is_won = False         # boolean for whether the game has been won or not
    BOARD = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]                      # List of list of strings that denote the current board state

    while not is_won:
        if is_player_1:
            cur_player = 1
        else:
            cur_player = 2
        
        symbol = PLAYER_SYMBOLS[cur_player]     # string representing the symbol of the current player
        board = move(symbol)
        is_won = check_win(board)

        if is_won:
            print(f"Congratulations Player {cur_player}, you won!")
        else:
            is_player_1 = not is_player_1
        
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
    play = True
    while play:
        play_game()
        is_play = input("Play again (y | n)? ")
        if is_play.lower() in ["n", "no"]:
            play = False
    
    print("Goodbye!")