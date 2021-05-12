import pygame, sys
from time import sleep
from config import *

pygame.init()
screen_x = 720
screen_y = 670
screen = pygame.display.set_mode((screen_x, screen_y))

snake_size = 1
snake_array = [head(360, 335)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_array[0].dirY = 0
                if snake_array[0].x != -1: snake_array[0].dirX = 1
            elif event.key == pygame.K_LEFT:
                snake_array[0].dirY = 0
                if snake_array[0].x != 1: snake_array[0].dirX = -1
            elif event.key == pygame.K_RIGHT:
                snake_array[0].dirY = 0
                if snake_array[0].x != -1: snake_array[0].dirX = 1
            elif event.key == pygame.K_RIGHT:
                snake_array[0].dirY = 0
                if snake_array[0].x != -1: snake_array[0].dirX = 1

    for part in snake_array:
            part.draw(screen)

    pygame.display.update()
