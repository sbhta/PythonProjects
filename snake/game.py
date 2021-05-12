from config import *

pygame.init()
screen_x = 800
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))

snake_size = 1
snake_array = [head(384, 400)]

a = apple(randint(1, 49) * 16, randint(1, 49) * 16, snake_array)

clock = pygame.time.Clock()
tps = 10
while True:
    clock.tick(tps)
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_array[-1].dirY = 0
                if snake_array[-1].dirX != -1: snake_array[-1].dirX = 1
            elif event.key == pygame.K_LEFT:
                snake_array[-1].dirY = 0
                if snake_array[-1].dirX != 1: snake_array[-1].dirX = -1
            elif event.key == pygame.K_DOWN:
                snake_array[-1].dirX = 0
                if snake_array[-1].dirY != -1: snake_array[-1].dirY = 1
            elif event.key == pygame.K_UP:
                snake_array[-1].dirX = 0
                if snake_array[-1].dirY != 1: snake_array[-1].dirY = -1

    snake_array[-1].move()
    for i in snake_array:
        try:
            i.move_p(snake_array[snake_array.index(i) + 1])
        except:
            pass
    for i in snake_array:
        i.oldX = i.x
        i.oldY = i.y

    a.draw(screen)
    for i in snake_array:
        i.draw(screen)
    for i in snake_array[:-1]:
        if snake_array[-1].x == i.x and snake_array[-1].y == i.y:
            sys.exit()

    if snake_array[-1].x > 800: snake_array[-1].x = 0
    if snake_array[-1].x < 0: snake_array[-1].x = 800
    if snake_array[-1].y > 800: snake_array[-1].y = 0
    if snake_array[-1].y < 0: snake_array[-1].y = 800


    a.eaten(snake_array[-1])

    pygame.display.update()
