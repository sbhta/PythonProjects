import sys

from config import *
import pygame

WIN = pygame.display.set_mode((800, 600))


def main():


    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    main()