import pygame


class s_part:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dirX = 0
        self.dirY = 0
        self.oldX = self.x
        self.oldY = self.y
    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.x, self.y, 16, 16))

    def move_p(self, p):
        self.x = p.oldX
        self.y = p.oldY
        print(f"{self.x} {self.y}")


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

