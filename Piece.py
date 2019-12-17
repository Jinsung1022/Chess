class Piece:

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def get_color(self):
        return self.color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y