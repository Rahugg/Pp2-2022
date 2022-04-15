import pygame
from random import randrange
import time

pygame.init()

# Screen
size = 800
screen = pygame.display.set_mode((size, size))
running = True

# Snake
block = 50
snake_length = 1
speed = 50
x, y = (randrange(0, 750, 50), randrange(0, 750, 50))
snake = [(x, y)]
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
dx, dy = 0, 0

# Apple
apple = (randrange(0, 750, 50), randrange(0, 750, 50))

# Clock
fps = 10
FramesPerSecond = pygame.time.Clock()

# Levels
levels = {1 : 3, 2 : 4, 3 : 5, 4 : 10}
level = 1
apple_score = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game over", True, (0, 0, 0))
next_level = font.render("Next level", True, (0, 0, 0))

# While loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w] and dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True}
            if pressed[pygame.K_a] and dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False}
            if pressed[pygame.K_s] and dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True}
            if pressed[pygame.K_d] and dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True}

    screen.fill((0, 0, 0))

    # Drawing snake
    for i, j in snake:
        pygame.draw.rect(screen, (0, 255, 0), (i, j, block, block))
    pygame.draw.rect(screen, (255, 0, 0), (*apple, block , block))
    current_level = font_small.render('Level: ' + str(level), True, (255, 255, 255))
    Apples = font_small.render('Apples: ' + str(apple_score), True, (255, 255, 255))

    # Snake movement
    x += dx * block
    y += dy * block
    
    snake.append((x, y))
    snake = snake[-snake_length:]

    # Game over
    if x < -50 or x > size or y < -50 or y > size or len(snake) != len(set(snake)):
        screen.fill((255, 255, 255))
        screen.blit(game_over, (200, 300))
        pygame.display.update()
        time.sleep(2)
        break
    
    # Next level
    if snake_length == levels[level]:
        screen.fill((255, 255, 255))
        screen.blit(next_level, (200, 300))
        pygame.display.update()
        time.sleep(3)
        level += 1
        snake_length = 1
        fps += 2
        x, y = (randrange(0, 750, 50), randrange(0, 750, 50))
        apple = (randrange(0, 750, 50), randrange(0, 750, 50))
        dx, dy = 0, 0
    
    # Eating an apple
    if snake[-1] == apple:
        apple_score += 1
        snake_length += 1
        apple = randrange(0,size,block), randrange(0,size,block)
    
    # Score
    screen.blit(current_level, (10, 10))
    screen.blit(Apples, (340, 10))

    pygame.display.update()
    FramesPerSecond.tick(fps)