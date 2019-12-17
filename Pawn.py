from Piece import Piece


class Pawn(Piece):

    def __init__(self, color, x, y):
        self.moved = False
        super().__init__(color, x, y)

    def get_moved(self):
        return self.moved

    '''
    Returns whether this pawn has reached the
    other end of the board.
    '''
    def reached_end(self):
        ret = False
        if self.color == 'white':
            if self.y == 7:
                ret = True
        elif self.color == 'black':
            if self.y == 0:
                ret = True
        return ret
