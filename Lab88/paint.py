from tkinter import Frame
import pygame

pygame.init()

# Screen
size = 800
screen = pygame.display.set_mode((size, size))
running = True
instrument = "pen"
radius = 20
holding = False
last_pos = (0, 0)

# FPS
fps = 60
FramesPerSecond = pygame.time.Clock()


# Colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
current_color = grey

# Fonts
font = pygame.font.SysFont("Verdana", 20)

def drawline(screen, last, end_pos, radius, cur_color): # DRAWING LINE

    x1, y1, x2, y2 = last[0], last[1], end_pos[0], end_pos[1]

    dx, dy = abs(x1 - x2), abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, cur_color, (x, y), radius)
    
    else:

        if y1 > y2:
            x1, x2 = x2, x1 
            y1, y2 = y2, y1

        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, cur_color, (x, y), radius)

def drawCircle(screen, start_pos, end_pos, width, cur_color): # DRAWING CIRCLE

    x1, y1, x2, y2 = start_pos[0], start_pos[1], end_pos[0], end_pos[1]

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2

    pygame.draw.circle(screen, cur_color, (x, y), radius, width)

def drawRectangle(screen, start_pos, end_pos, width, cur_color): # DRAWING RECTANGLE

    x1, y1, x2, y2 = start_pos[0], start_pos[1], end_pos[0], end_pos[1]

    widthr = abs(x2 - x1)
    height = abs(y1 - y2)

    pygame.draw.rect(screen, cur_color, (x1, y1, widthr, height), width)

screen.fill((255, 255, 255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            key = pygame.key.get_pressed()

            if key[pygame.K_w]:
                instrument = "pen"
            if key[pygame.K_s]:
                instrument = "circle"
            if key[pygame.K_a]:
                instrument = "rectangle"
            if key[pygame.K_u]:
                screen.fill((255, 255, 255))
            if key[pygame.K_c] and key[pygame.K_r]:
                current_color = red
            if key[pygame.K_c] and key[pygame.K_b]:
                current_color = blue
            if key[pygame.K_c] and key[pygame.K_g]:
                current_color = green
            if key[pygame.K_c] and key[pygame.K_e]:
                current_color = white

        if event.type == pygame.MOUSEBUTTONDOWN:

            holding = True
            startpos = event.pos

            if instrument == "pen":
                pygame.draw.circle(screen, current_color, event.pos, radius)

        if event.type == pygame.MOUSEBUTTONUP:

            if instrument == "rectangle":
                drawRectangle(screen, startpos, event.pos, radius, current_color)

            if instrument == "circle":
                drawCircle(screen, startpos, event.pos, radius, current_color)

            holding = False

        if event.type == pygame.MOUSEMOTION:

            if holding and instrument == "pen":
                drawline(screen, last_pos, event.pos, radius, current_color)
            last_pos = event.pos

    # TEXT
    info = font.render("[U] - clean screen, [W] - draw line, [A] - draw rectangle, [S] - draw circle", True, black)
    info2 = font.render("[C + (color)] - change color, [R] - red, [B] - blue, [G] - green, [E] - eraser", True, black)
    screen.blit(info, (10, 10))
    screen.blit(info2, (10, 750))
    pygame.display.update()
    FramesPerSecond.tick(fps)