import pygame
import random

# initialize pygame
pygame.init()

# set up screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# set up snake
snake = [(300, 300)]
dx = 0
dy = 0

# set up food
food = (random.randint(0, 29) * 20, random.randint(0, 29) * 20)

# set up score
score = 0
font = pygame.font.Font(None, 30)

# set up game loop
running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx = 0
                dy = -20
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 20
            elif event.key == pygame.K_LEFT:
                dx = -20
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = 20
                dy = 0

    # move snake
    snake = [(snake[0][0] + dx, snake[0][1] + dy)] + snake[:-1]

    # check for collision with food
    if snake[0] == food:
        food = (random.randint(0, 29) * 20, random.randint(0, 29) * 20)
        snake.append(snake[-1])
        score += 10

    # # check for collision with walls or self
    if snake[0][0] < 0 or snake[0][0] >= 600 or snake[0][1] < 0 or snake[0][1] >= 600:
        running = False
    # for i in range(1, len(snake)):
    #     if snake[0] == snake[i]:
    #         running = False

    # draw screen
    screen.fill(black)
    for s in snake:
        pygame.draw.rect(screen, white, (s[0], s[1], 20, 20))
    pygame.draw.rect(screen, red, (food[0], food[1], 20, 20))
    score_text = font.render("Score: {}".format(score), True, white)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    # set frame rate
    clock.tick(10)

# exit game
pygame.quit()
