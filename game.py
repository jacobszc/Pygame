
import pygame
import Sprite
from Sprite import Sprite
import Player
from Player import Player
import Store
from Store import Store
import Collision
from Collision import Collision
from pygame.locals import *
from pygame import mixer
from Music import Music
import config
from config import *
import pygame_menu



pygame.init()

##### WINDOW VARIABLES ###########

screen = pygame.display.set_mode((SCREEN_SIZE), pygame.RESIZABLE) 
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()

##### TITLE TITLE_MENU VARIABLES ########

DIFFICULTY = ['Easy']

TITLE_MENU = pygame_menu.Menu('Welcome', 800,800,
                       theme=pygame_menu.themes.THEME_GREEN)

TITLE_MENU.add.text_input('Name :', default='John Doe')
TITLE_MENU.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty(DIFFICULTY))
TITLE_MENU.add.button('Play',  start_the_game())
TITLE_MENU.add.button('Quit', pygame_menu.events.EXIT)
PLAY_TITLE_MUSIC = Music("music_tracks/title-screen-music.mp3")

### CREATE A SHOP INSTANCE##########################################

shopImg=pygame.image.load("images/green_rectangle.png").convert_alpha()
shopImg = pygame.transform.scale(shopImg, (64,64) )
shopClass = Store()
SHOP = Sprite(shopClass, SHOP_LOC, shopImg)

# Create player instance#########################################

playerImg = pygame.image.load("images/red_rectangle.png").convert_alpha()
playerClass = Player(SAMPLE_NAME)
PLAYER_1 = Sprite(playerClass, INITIAL_SPAWN_LOC, playerImg)


#### create a collision checker instance

collisonChecker = Collision()



##################### TITLE SCREEN LOOP START ##############################################

TITLE_SCREEN_RUNNING = True
while TITLE_SCREEN_RUNNING:
 
    if TITLE_MENU.is_enabled():
                TITLE_MENU.update(pygame.event.get())
                TITLE_MENU.draw(screen)

                pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Only allow Enter to exit
                TITLE_SCREEN_RUNNING = False


            
    
               ## screen.blit(TITLE_SCREEN, (0,0))

##################### TITLE SCREEN LOOP END ##############################################



###################### MAIN GAME LOOP START ##########################################

mixer.init()
mixer.music.load("music_tracks/background-music.mp3")
mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # cluase for if the user attemps to resize the window
        elif event.type == pygame.VIDEORESIZE:
         width, height = event.size
         screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
         background = pygame.transform.scale(background, (width, height))
         PLAYER_1.image = pygame.transform.scale((PLAYER_1.image),(width, height)) ## this rescales the player with the backgorund durring screen resize

############################# END OF EVENT CHECKERS #################################### 
    
    background = pygame.image.load("images/tiles-map.png")
    background = pygame.transform.scale(background, BACKGROUND_SIZE)
    current_time = pygame.time.get_ticks()
    
    
    
    PLAYER_1.updateFrameIndex() ## INIT UPDATING THE SPRITE BASED ON DIRECTION
    PLAYER_1.makePlayerMove() ## INIT wasd controls for player instance
    
    
#############################  EVERY 2 SECONDS CHECK FOR COLLIONS #############################
    if current_time - last_collision_check_time >= collision_check_interval:
     collisonChecker.isCollision(PLAYER_1, SHOP)
     last_collision_check_time = current_time

    
     ## this must be called to dynamicly update the player frame index on the sprite sheet to 
    ## allow for sprite animations while moving or standing still 
    

    
    screen.blit(background, (0,0))
    screen.blit(PLAYER_1.image, (PLAYER_1.rect.x, PLAYER_1.rect.y))
    screen.blit(shopImg, SHOP_LOC)
    
    
    ##screen.blit(shopImg, SHOP_LOC)
    
     
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()



