# Class for orchestrating the game


class Game_Controller:
    def __init__(self, init_board, symbol_choices):
        self.init_board = init_board
        self.symbol_choices = symbol_choices
        self.MAX_TURNS = len(init_board) * len(init_board)
        self.is_won = False
