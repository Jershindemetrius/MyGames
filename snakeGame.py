import pygame
import random

# initialize pygame
pygame.init()

# set up window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# set up snake properties
SNAKE_SIZE = 15
SNAKE_COLOR = WHITE

# set up food properties
FOOD_SIZE = 10
FOOD_COLOR = RED

# set up game clock
clock = pygame.time.Clock()

# set up initial snake position and movement
snake_x = 200
snake_y = 200
snake_dx = SNAKE_SIZE
snake_dy = 0

# set up initial food position
food_x = random.randint(0, WINDOW_WIDTH - FOOD_SIZE)
food_y = random.randint(0, WINDOW_HEIGHT - FOOD_SIZE)

# set up initial score
score = 0

# game loop
game_over = False
while not game_over:

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            elif event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE
            elif event.key == pygame.K_LEFT:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0

    # update snake position
    snake_x += snake_dx
    snake_y += snake_dy

    # check if snake hit the wall
    if snake_x < 0 or snake_x > WINDOW_WIDTH - SNAKE_SIZE or snake_y < 0 or snake_y > WINDOW_HEIGHT - SNAKE_SIZE:
        game_over = True

    # check if snake hit the food
    if snake_x == food_x and snake_y == food_y:
        # increase score
        score += 1
        # spawn new food
        food_x = random.randint(0, WINDOW_WIDTH - FOOD_SIZE)
        food_y = random.randint(0, WINDOW_HEIGHT - FOOD_SIZE)

    # draw game objects
    window.fill(BLACK)
    pygame.draw.rect(window, SNAKE_COLOR, (snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(window, FOOD_COLOR, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))
    pygame.display.update()

    # set game speed
    clock.tick(5)

# quit pygame
pygame.quit()
