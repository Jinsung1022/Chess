import contextlib
with contextlib.redirect_stdout(None):
    import pygame


class Square:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.color = (0, 0, 0)
        self.bd_color = (0, 0, 0)
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, 70, 70)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_color(self, x, y, z):
        self.color = (x, y, z)
        pygame.draw.rect(self.screen, self.color, self.rect)

    def display(self, turn):
        if turn == 1:
            self.color = (238, 220, 198)
            self.bd_color = (238, 220, 198)
            pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            self.color = (179, 133, 107)
            self.bd_color = (179, 133, 107)
            pygame.draw.rect(self.screen, (179, 133, 107), self.rect)

    def check_clicked(self, x, y):
        value = 0
        click = self.rect.collidepoint(x, y)
        if click == 1:
            #print('Clicked', self.x/70, self.y/70)
            value = 1
        return value
