import pygame, sys
from time import sleep
from config import *

pygame.init()
screen_x = 720
screen_y = 670
screen = pygame.display.set_mode((screen_x, screen_y))

snake_size = 1
snake_array = [s_part(328, 335),s_part(344, 335),head(360, 335)]

clock = pygame.time.Clock()
tps = 5
while True:
    clock.tick(tps)
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_array[-1].dirY = 0
                if snake_array[-1].x != -1: snake_array[-1].dirX = 1
            elif event.key == pygame.K_LEFT:
                snake_array[-1].dirY = 0
                if snake_array[-1].x != 1: snake_array[-1].dirX = -1
            elif event.key == pygame.K_DOWN:
                snake_array[-1].dirX = 0
                if snake_array[-1].y != -1: snake_array[-1].dirY = 1
            elif event.key == pygame.K_UP:
                snake_array[-1].dirX = 0
                if snake_array[-1].y != 1: snake_array[-1].dirY = -1

    snake_array[-1].move()
    for i in snake_array:
        try: i.move_p(snake_array[snake_array.index(i) + 1])
        except: print("fin")

    for i in snake_array:
        i.draw(screen)

    pygame.display.update()
