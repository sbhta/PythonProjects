import pygame, config, sys


def main():
    WIN = pygame.display.set_mode((500, 500))
    Clock = pygame.time.Clock()

    Boids = []
    for i in range(4):
        Boids.append(config.Boid(300, 300))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WIN.fill("black")
        pygame.display.update()
        Clock.tick(60)




if __name__ == '__main__':
    main()