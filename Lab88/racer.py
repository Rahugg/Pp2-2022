#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
restart = True
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
game_over1 = font_small.render("Press 'R' to restart", True, BLACK)

background = pygame.image.load("img/AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("img/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("img/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        if self.rect.top > 0:
              if pressed_keys[K_UP]:
                  self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:        
              if pressed_keys[K_DOWN]:
                  self.rect.move_ip(0, 5)          
                  
class Coin(pygame.sprite.Sprite):
    def get_random_speed(self):
        speed = random.randint(1, 3)
        return speed

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/coin.png")
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect(center=(random.randint(100, SCREEN_WIDTH - 40), 0))
        self.speed = self.get_random_speed()

    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(100, SCREEN_WIDTH - 40), 0)
            self.speed = self.get_random_speed()
        if pygame.sprite.spritecollideany(P1, coins):
            COIN_SCORE += 1
            pygame.mixer.Sound('sounds/coin-drop-4.mp3').play()
            self.rect.top = 0
            self.rect.center = (random.randint(100, SCREEN_WIDTH - 40), 0)
            self.speed = self.get_random_speed()


# Setting up Sprites        

# Creating Sprites Groups



#Adding a new User event 
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)
while restart:
    running = True
    P1 = Player()
    E1 = Enemy()
    C1 = Coin()
    enemies = pygame.sprite.Group()
    enemies.add(E1)
    coins = pygame.sprite.Group()
    coins.add(C1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)
    all_sprites.add(C1)
    crush = False
    #Game Loop
    while running:
       
        #Cycles through all events occuring  
        for event in pygame.event.get():
            # if event.type == INC_SPEED:
            #     SPEED += 0.5      
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                COIN_SCORE = 0
                running = False
                

        DISPLAYSURF.blit(background, (0,0))
        coinscore = font_small.render("COINS: " + str(COIN_SCORE), True, 'yellow')
        DISPLAYSURF.blit(coinscore, (10, 10))

        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            entity.move()
            DISPLAYSURF.blit(entity.image, entity.rect)
            

        #To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('sounds/crash.wav').play()
            # time.sleep(1)
            for entity in all_sprites:
                entity.kill()
            crush = True

        while crush:
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30,250))
            DISPLAYSURF.blit(game_over1,(75,350))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    crush = False
                    COIN_SCORE = 0
                    running = False
            pygame.display.update()
         
        # time.sleep(2)
            
            
                
            
        pygame.display.update()
        FramePerSec.tick(FPS)
    pygame.display.update()
    FramePerSec.tick(FPS)

