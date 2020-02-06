from Piece import Piece


class Pawn(Piece):

    def __init__(self, color, x, y):
        self.moved = False
        super().__init__(color, x, y)

    def get_moved(self):
        return self.moved

    def set_moved(self, move):
        self.moved = move

    def move(self, x, y):
        self.x = x
        self.y = y

    def possible(self, board):
        move_array = []
        if self.color == 'black':
            if board[self.x + 1][self.y] == 0:
                move_array.append((self.x + 1, self.y))
            if not self.moved:
                # print(self.y, self.x)
                if (board[self.x + 2][self.y] == 0) and (board[self.x + 1][self.y] == 0):
                    move_array.append((self.x + 2, self.y))
            if self.x < 7:
                if self.y > 0:
                    if board[self.x+1][self.y-1] != 0:
                        if board[self.x + 1][self.y - 1].color == 'white':
                            move_array.append((self.x+1, self.y-1))
                if self.y < 7:
                    if board[self.x+1][self.y+1] != 0:
                        if board[self.x + 1][self.y + 1].color == 'white':
                            move_array.append((self.x+1, self.y+1))
        else:
            if board[self.x - 1][self.y] == 0:
                move_array.append((self.x - 1, self.y))
            if not self.moved:
                if (board[self.x - 2][self.y] == 0) and (board[self.x - 1][self.y] == 0):
                    move_array.append((self.x - 2, self.y))
            if self.x > 0:
                if self.y < 7:
                    if board[self.x - 1][self.y + 1] != 0:
                        if board[self.x - 1][self.y + 1].color == 'black':
                            move_array.append((self.x-1, self.y+1))
                if self.y > 0:
                    if board[self.x-1][self.y-1] != 0:
                        if board[self.x - 1][self.y - 1].color == 'black':
                            move_array.append((self.x-1, self.y-1))

        return move_array

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
