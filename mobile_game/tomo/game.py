import pygame, sys, os, random

if not __name__ == '__main__':
    sys.exit()

Screen = pygame.display.set_mode((360, 720))
idle_right = [pygame.image.load('sprites/idle1.png'), pygame.image.load('sprites/idle2.png'), pygame.image.load('sprites/idle3.png')]
idle_left = [pygame.image.load('sprites/idle4.png'), pygame.image.load('sprites/idle5.png'), pygame.image.load('sprites/idle6.png')]
shadow = pygame.image.load('sprites/shadow.png')

player = idle_right[0].get_rect(center=(180, 360))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    player_ani = 0
    Screen.fill("#66402B")
    Screen.blit(idle_right[player_ani], player)

    pygame.display.update()


