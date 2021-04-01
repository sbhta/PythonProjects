import pygame



class Boid():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('tri.png')
        self.image = pygame.transform.scale(self.image, size=(10, 10))
        self.boid = self.image.get_rect(center=(self.x, self.y))
    def draw_boid(self, screen):
        screen.blit(self.image, self.boid)