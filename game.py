
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

SCREEN_SIZE = 800 , 800 
BACKGROUND_SIZE = SCREEN_SIZE
INITIAL_SPAWN_LOC = 400 , 400
STORE_LOC = 400, 400
SAMPLE_NAME = "Jake"
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE), pygame.RESIZABLE) 
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()


last_collision_check_time = 0  # Stores the last time the collision was checked
collision_check_interval = 2000  # 2 seconds in milliseconds


sprite_sheet = pygame.image.load("images/red_rectangle.png").convert_alpha()
background = pygame.image.load("images/tiles-map.png")
background = pygame.transform.scale(background, BACKGROUND_SIZE)


title_screen=pygame.image.load("images/Title-screen.png")
title_screen = pygame.transform.scale(title_screen, BACKGROUND_SIZE)


greenRectange = pygame.image.load("images/green_rectangle.png")
greenRectange = pygame.transform.scale(greenRectange, (64,64) )
redRectange = pygame.image.load("images/red_rectangle.png")
redRectange = pygame.transform.scale(redRectange, (64,64) )

shopImg=pygame.image.load("images/green_rectangle.png").convert_alpha()
shopImg = pygame.transform.scale(shopImg, (64,64) )



# Create player instance
player = Player(SAMPLE_NAME)
shop = Store()
playerSprite = Sprite(player, INITIAL_SPAWN_LOC, sprite_sheet)
ShopSprite = Sprite(shop, STORE_LOC, shopImg)


Red = Player(SAMPLE_NAME)
RED = Sprite(Red,INITIAL_SPAWN_LOC, redRectange,)

green = Player(SAMPLE_NAME)
GREEN = Sprite(green,STORE_LOC, redRectange,)



collisonChecker = Collision()

playtitleMusic = Music("music_tracks/title-screen-music.mp3")








## title screen loop

title_screen_running = True
while title_screen_running:
 screen.blit(title_screen, (0,0))
 pygame.display.flip()
 for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            title_screen = pygame.transform.scale(title_screen, (width, height))
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Only allow Enter to exit
                title_screen_running = False
    
    
        
        

                screen.blit(title_screen, (0,0))




# Main game loop

mixer.init()
mixer.music.load("music_tracks/background-music.mp3")
mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
         width, height = event.size
         screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
         background = pygame.transform.scale(background, (width, height))
         playerSprite.image = pygame.transform.scale((player.image),(width, height))
    
    current_time = pygame.time.get_ticks()
    playerSprite.updateFrameIndex()
    playerSprite.makePlayerMove() ## INIT wasd controls for player instance
    
    if current_time - last_collision_check_time >= collision_check_interval:
     collisonChecker.isCollision(playerSprite, ShopSprite)
     last_collision_check_time = current_time

    
     ## this must be called to dynamicly update the player frame index on the sprite sheet to 
    ## allow for sprite animations while moving or standing still 
    

    
    screen.blit(background, (0,0))
    screen.blit(playerSprite.image, (playerSprite.rect.x, playerSprite.rect.y))
    screen.blit(shopImg, STORE_LOC)
    
    
    ##screen.blit(shopImg, STORE_LOC)
    
     
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()



