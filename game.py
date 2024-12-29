
import pygame
import Player
from Player import Player
from pygame.locals import *
from pygame import mixer
from Music import Music

SCREEN_SIZE = 800 , 800 
BACKGROUND_SIZE = SCREEN_SIZE
INITIAL_SPAWN_LOC = 200 , 200
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE), pygame.RESIZABLE) 
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()

# Load sprite sheet
sprite_sheet = pygame.image.load("images/SaraFullSheet.png").convert_alpha()
background = pygame.image.load("images/tiles-map.png")
background = pygame.transform.scale(background, BACKGROUND_SIZE)


title_screen=pygame.image.load("images/Title-screen.png")
title_screen = pygame.transform.scale(title_screen, BACKGROUND_SIZE)



# Create player instance
player = Player(INITIAL_SPAWN_LOC, sprite_sheet)

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
         player.image = pygame.transform.scale((player.image),(width, height))

    player.updateFrameIndex()
    player.makePlayerMove() ## INIT wasd controls for player instance
    
     ## this must be called to dynamicly update the player frame index on the sprite sheet to 
    ## allow for sprite animations while moving or standing still 
    

    
    screen.blit(background, (0,0))
    screen.blit(player.image, (player.rect.x, player.rect.y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
