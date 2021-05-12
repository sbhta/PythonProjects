import pygame


class s_part:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dirX = 1
        self.dirY = 1

    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.x, self.y, 16, 16))


class head(s_part):
    def move(self):
        if self.dirX == 1:
            self.x += 16
        if self.dirX == -1:
            self.x -= 16
        if self.dirY == 1:
            self.y += 16
        if self.dirY == -1:
            self.y -= 16

