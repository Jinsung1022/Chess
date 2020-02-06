from Piece import Piece


class Knight(Piece):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def possible(self, board):
        move_array = []
        # if self.color == 'black':
        try:
            if self.x >= 2:
                if board[self.x - 2][self.y + 1] == 0:
                    move_array.append((self.x - 2, self.y + 1))
                else:
                    if self.color == 'black':
                        if board[self.x - 2][self.y + 1].color == 'white':
                            move_array.append((self.x - 2, self.y + 1))
                    else:
                        if board[self.x - 2][self.y + 1].color == 'black':
                            move_array.append((self.x - 2, self.y + 1))
        except IndexError:
            pass
        try:
            if self.x >= 1:
                if board[self.x - 1][self.y + 2] == 0:
                    move_array.append((self.x - 1, self.y + 2))
                else:
                    if self.color == 'black:':
                        if board[self.x - 1][self.y + 2].color == 'white':
                            move_array.append((self.x - 1, self.y + 2))
                    else:
                        if board[self.x - 1][self.y + 2].color == 'black':
                            move_array.append((self.x - 1, self.y + 2))
        except IndexError:
            pass
        try:
            if board[self.x + 1][self.y + 2] == 0:
                move_array.append((self.x + 1, self.y + 2))
            else:
                if self.color == 'black':
                    if board[self.x + 1][self.y + 2].color == 'white':
                        move_array.append((self.x + 1, self.y + 2))
                else:
                    if board[self.x + 1][self.y + 2].color == 'black':
                        move_array.append((self.x + 1, self.y + 2))
        except IndexError:
            pass
        try:
            if board[self.x + 2][self.y + 1] == 0:
                move_array.append((self.x + 2, self.y + 1))
            else:
                if self.color == 'black':
                    if board[self.x + 2][self.y + 1].color == 'white':
                        move_array.append((self.x + 2, self.y + 1))
                else:
                    if board[self.x + 2][self.y + 1].color == 'black':
                        move_array.append((self.x + 2, self.y + 1))
        except IndexError:
            pass
        try:
            if self.y >= 1:
                if board[self.x + 2][self.y - 1] == 0:
                    move_array.append((self.x + 2, self.y - 1))
                else:
                    if self.color == 'black':
                        if board[self.x + 2][self.y - 1].color == 'white':
                            move_array.append((self.x + 2, self.y - 1))
                    else:
                        if board[self.x + 2][self.y - 1].color == 'black':
                            move_array.append((self.x + 2, self.y - 1))
        except IndexError:
            pass
        try:
            if self.y >= 2:
                if board[self.x + 1][self.y - 2] == 0:
                    move_array.append((self.x + 1, self.y - 2))
                else:
                    if self.color == 'black':
                        if board[self.x + 1][self.y - 2].color == 'white':
                            move_array.append((self.x + 1, self.y - 2))
                    else:
                        if board[self.x + 1][self.y - 2].color == 'black':
                            move_array.append((self.x + 1, self.y - 2))
        except IndexError:
            pass
        try:
            if (self.x >= 1) and (self.y >= 2):
                if board[self.x - 1][self.y - 2] == 0:
                    move_array.append((self.x - 1, self.y - 2))
                else:
                    if self.color == "black":
                        if board[self.x - 1][self.y - 2].color == 'white':
                            move_array.append((self.x - 1, self.y - 2))
                    else:
                        if board[self.x - 1][self.y - 2].color == 'black':
                            move_array.append((self.x - 1, self.y - 2))
        except IndexError:
            pass
        try:
            if (self.x >= 2) and (self.y >= 1):
                if board[self.x - 2][self.y - 1] == 0:
                    move_array.append((self.x - 2, self.y - 1))
                else:
                    if self.color == 'black':
                        if board[self.x - 2][self.y - 1].color == 'white':
                            move_array.append((self.x - 2, self.y - 1))
                    else:
                        if board[self.x - 2][self.y - 1].color == 'black':
                            move_array.append((self.x - 2, self.y - 1))
        except IndexError:
            pass
        # print(move_array)
        return move_array
