from Pawn import Pawn
from Knight import Knight
from Piece import Piece


class ChessBoard:
    '''
    A class representing a ChessBoard
    '''
    def __init__(self):
        self.board = []

    def setup(self):
        for i in range(8):
            self.board.append([0, 0, 0, 0, 0, 0, 0, 0])

    def get_board(self):
        return self.board
