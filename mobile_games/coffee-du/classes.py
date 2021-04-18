import pygame

class Spike:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("png/spike.png"), (34, 34))
        self.x, self.y = x, y
        self.spike = self.image.get_rect(center=(self.x, self.y))
        self.state = "left"

    def draw_spike(self, s):
        s.blit(self.image, self.spike)
