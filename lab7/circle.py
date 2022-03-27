import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
running = True

Blue = (0,0,255)
Green = (0,255,0)
Red = (255,0,0)
White = (255,255,255)

color = Red 
x,y = 25,25
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()    
    if pressed[pygame.K_RIGHT]:
        if x<465:
            x+=20
    elif pressed[pygame.K_LEFT]:
        if x>35:
            x-=20
    elif pressed[pygame.K_DOWN]:
        if y<465:
            y+=20
    elif pressed[pygame.K_UP]:
        if y>35:
            y-=20
            
    screen.fill(White)         
    pygame.draw.circle(screen, color, [x, y], 25, 0)

    pygame.display.flip()
    clock.tick(60)