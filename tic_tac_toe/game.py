PLAYER_SYMBOLS = {
    1: 'X',
    2: 'O'
}

# after a move, check the board to see if any player has won
def check_win(board):
    return False

# for the coordinates entered by a user, check they are valid
# check the alpha-numeric type, and the bounds
def check_valid_move(x, y):
    pass

# print out the current state of the board
def print_board(board):
    pass

# update the board to reflect the last move made
def update_board(new_board):
    pass

# function to convert the user input to coordinates in the board
def translate_num_pad_to_coord(num):
    pass

# function to process a player move, get their input etc.
# the accepted move must be between 1 to 9
def move(symbol, cur_board):
    return cur_board

# function to play a singular game to the end,
# need to update the current player each time a move is made
# and also check if the game was won with the last move or not
def play_game():
    cur_player = None
    is_player_1 = True
    is_won = False
    BOARD = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]

    while not is_won:
        if is_player_1:
            cur_player = 1
        else:
            cur_player = 2
        
        symbol = PLAYER_SYMBOLS[cur_player]
        board = move(symbol)
        is_won = check_win(board)
        
        if is_won:
            print(f"Congratulations Player {cur_player}, you won!")
        else:
            is_player_1 = not is_player_1
        

# Main entry point into the game
# Initialises flags and plays game infinitely until user says no
if __name__ == "__main__":
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