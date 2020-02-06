class Piece:

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    @staticmethod
    def opp_color(color):
        if color == 'white':
            return 'black'
        elif color == 'black':
            return 'white'

    @staticmethod
    def inside_board(x, y):
        if (x < 0) or (x > 7) or (y < 0) or (y > 7):
            return False
        else:
            return True

    def get_color(self):
        return self.color

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y