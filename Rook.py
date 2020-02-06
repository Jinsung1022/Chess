from Piece import Piece


class Rook(Piece):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def possible(self, board):
        move_array = []
        left_blocked = False
        right_blocked = False
        front_blocked = False
        back_blocked = False
        # Checking left
        for i in range(self.y - 1, -1, -1):
            if not left_blocked:
                if board[self.x][i] == 0:
                    move_array.append((self.x, i))
                else:
                    # print(board[self.x][i])
                    if board[self.x][i].color == self.opp_color(self.color):
                        move_array.append((self.x, i))
                        left_blocked = True
                    else:
                        left_blocked = True
        # Checking right
        for i in range(self.y + 1, 8):
            if not right_blocked:
                if board[self.x][i] == 0:
                    move_array.append((self.x, i))
                else:
                    if board[self.x][i].color == self.opp_color(self.color):
                        move_array.append((self.x, i))
                        right_blocked = True
                    else:
                        right_blocked = True

        for i in range(self.x + 1, 8):
            if self.color == 'black':
                if not front_blocked:
                    if board[i][self.y] == 0:
                        move_array.append((i, self.y))
                    else:
                        if board[i][self.y].color == self.opp_color(self.color):
                            move_array.append((i, self.y))
                            front_blocked = True
                        else:
                            front_blocked = True
            elif self.color == 'white':
                if not back_blocked:
                    if board[i][self.y] == 0:
                        move_array.append((i, self.y))
                    else:
                        if board[i][self.y].color == self.opp_color(self.color):
                            move_array.append((i, self.y))
                            back_blocked = True
                        else:
                            back_blocked = True

        for i in range(self.x - 1, -1, -1):
            if self.color == 'white':
                if not front_blocked:
                    if board[i][self.y] == 0:
                        move_array.append((i, self.y))
                    else:
                        if board[i][self.y].color == self.opp_color(self.color):
                            move_array.append((i, self.y))
                            front_blocked = True
                        else:
                            front_blocked = True
            elif self.color == 'black':
                if not back_blocked:
                    if board[i][self.y] == 0:
                        move_array.append((i, self.y))
                    else:
                        if board[i][self.y].color == self.opp_color(self.color):
                            move_array.append((i, self.y))
                            back_blocked = True
                        else:
                            back_blocked = True
        # print("inside_board:", move_array)
        return move_array
