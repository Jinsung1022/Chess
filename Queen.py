from Piece import Piece


class Queen(Piece):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def possible(self, board):
        move_array = []
        directions = [[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
        for direction in directions:
            blocked = False
            pos_x = self.x
            pos_y = self.y
            for i in range(0, 8):
                # print('blocked is:', blocked, i)
                pos_x = pos_x + direction[0]
                pos_y = pos_y + direction[1]
                if self.inside_board(pos_x, pos_y):
                    if not blocked:
                        if board[pos_x][pos_y] != 0:
                            # print("color is:", board[pos_x][pos_y].get_color)
                            if board[pos_x][pos_y].color == self.opp_color(self.color):
                                move_array.append((pos_x, pos_y))
                                blocked = True
                            elif board[pos_x][pos_y].color == self.color:
                                blocked = True
                        else:
                            move_array.append((pos_x, pos_y))
        return move_array
