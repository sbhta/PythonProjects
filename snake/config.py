import pygame, sys
from time import sleep
from random import randint


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


class head(s_part):
    def move(self):
        if self.dirX == 1:
            self.x += 16
        elif self.dirX == -1:
            self.x -= 16
        elif self.dirY == 1:
            self.y += 16
        elif self.dirY == -1:
            self.y -= 16


class apple:
    def __init__(self, x, y, snake):
        self.x = x
        self.y = y
        self.snake = snake

    def draw(self, screen):
        pygame.draw.rect(screen, "red", (self.x, self.y, 16, 16))
    def eaten(self, head):
        if head.x == self.x and head.y == self.y:
            self.x = randint(1, 50) * 16
            self.y = randint(1, 50) * 16
            self.snake.insert(0, s_part(self.snake[0].x, self.snake[0].y))

