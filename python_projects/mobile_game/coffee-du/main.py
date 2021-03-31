import pygame, time, threading, classes, sys, random

pygame.init()


def main():
    global score, possible_spots, coffee_bean_pos, threads, coffee_bean_state
    # preparations
    Screen = pygame.display.set_mode((600, 700))
    CoffeeDu = pygame.transform.scale(pygame.image.load("coffeedu.png"), (49, 37))
    CoffeeBean = pygame.transform.scale(pygame.image.load("coffee_bean.png"), (24, 24))
    Clock = pygame.time.Clock()
    pygame.display.set_icon(CoffeeDu)

    # creating the threads
    threads = []

    # creating player and bean hit-boxes
    player = CoffeeDu.get_rect(center=(300, 350))
    coffee_bean = CoffeeBean.get_rect(center=(575, 200))

    # creating spikes
    spikes = []
    for i in range(12):
        spikes.append(classes.Spike(17, 34))
        if i >= 6:
            spikes[i].spike.center = (586, 34)
            spikes[i].image = pygame.transform.flip(spikes[i].image, True, False)
            spikes[i].state = "right"

    # values and variables
    player_velocity = 0
    gravity = 0.25
    player_move = 1
    coffee_bean_pos = "right"
    score = 0
    game_font = pygame.font.Font("04B_19.TTF", 60)
    possible_spots = [650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50]
    coffee_bean_state = True

    # functions
    def change_trans(img, pop):
        global coffee_bean_pos, coffee_bean_state
        coffee_bean_state = False
        for i in range(15):
            img.set_alpha(255 - i * 18)
            time.sleep(0.01)
        if coffee_bean_pos == "right":
            coffee_bean.center = (570, pop)
            coffee_bean_pos = "left"
        else:
            coffee_bean.center = (30, pop)
            coffee_bean_pos = "right"
        for i in range(15):
            img.set_alpha(0 + i * 18)
            time.sleep(0.01)
        coffee_bean_state = True

    def collision_check(col):
        global score, coffee_bean_pos, threads
        if player.colliderect(col) == True:
            if col == coffee_bean and coffee_bean_state == True:
                random.shuffle(possible_spots)
                t1 = threading.Thread(target=shuffle_spikes)
                t2 = threading.Thread(target=change_trans, args=[CoffeeBean, possible_spots.pop()])
                random.shuffle(possible_spots)

                t1.start()
                t2.start()
                threads.append(t1)
                threads.append(t2)
                score = score + 1

    def shuffle_spikes():
        threads = []
        for i in spikes:
            if i.state == "right": t = threading.Thread(target=retract, args=[i, 2]); t.start();threads.append(t)
            if i.state == "left": t = threading.Thread(target=retract, args=[i, -2]); t.start();threads.append(t)

        for thread in threads:
            thread.join()

    def retract(spike, negative):
        global possible_spots
        # print("moving")
        time.sleep(0.1)
        for i in range(25):
            spike.spike.x += negative
            time.sleep(0.005)
        spike.spike.centery = possible_spots.pop()
        for i in range(25):
            spike.spike.x -= negative
            time.sleep(0.005)

        # resetting the possible positions
        possible_spots = [650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50]

    def display_score():
        global score
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(300, 100))
        Screen.blit(score_surface, score_rect)

    # creating the while loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_velocity = -8
                    gravity = 0.25
        # checking if the player is not to high up or down
        if player.bottom >= 700:
            player.y -= 1
            player_velocity = 0
            gravity = 0
        elif player.top <= 0:
            player.y += 1
            player_velocity = 0
        if player_move == 1 and player.right >= 600:
            player_move = -1
            CoffeeDu = pygame.transform.flip(CoffeeDu, True, False)
        if player_move == -1 and player.left <= 0:
            player_move = 1
            CoffeeDu = pygame.transform.flip(CoffeeDu, True, False)

        # changing the player position
        player.x += player_move * 6

        player_velocity += gravity
        player.y += player_velocity

        # checking for collisions
        collision_check(coffee_bean)
        for i in spikes:
            if player.bottom >= i.spike.top + 20 and player.top <= i.spike.bottom - 20:
                if player.right >= i.spike.left + 5 and player.left <= i.spike.right - 5:
                    pygame.quit()
                    sys.exit()

        # drawing the screen
        Screen.fill((120, 84, 52))
        display_score()

        for spike in spikes: spike.draw_spike(Screen)
        Screen.blit(CoffeeDu, player)
        Screen.blit(CoffeeBean, coffee_bean)

        pygame.display.update()
        Clock.tick(60)


if __name__ == '__main__':
    main()
