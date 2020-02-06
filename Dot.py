import contextlib
with contextlib.redirect_stdout(None):
    import pygame


class Dot:

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 3
        self.color = (0, 0, 255)

    def display(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.size)
