
import pygame
from sprite_init import Player
from pygame.locals import *
from pygame import mixer

SCREEN_SIZE = 800 , 800
INITIAL_SPAWN_LOC = 200 , 200
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Sprite Animation Example")
clock = pygame.time.Clock()

# Load sprite sheet
sprite_sheet = pygame.image.load("SaraFullSheet.png").convert_alpha()
background = pygame.image.load("tiles-map.png")
resized_background = pygame.transform.scale(background, SCREEN_SIZE)
title_screen=pygame.image.load("Title-screen.png")

# Create player instance
player = Player(INITIAL_SPAWN_LOC, sprite_sheet)

# Timing variables
last_update_time = pygame.time.get_ticks()
frame_delay = 500  # 500 ms
mixer.init()
mixer.music.load("title-screen-music.mp3")
mixer.music.play()


## title screen loop

title_screen_running = True
while title_screen_running:
 screen.blit(title_screen, (0,0))
 pygame.display.flip()
 for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
     title_screen_running = False




# Main game loop


mixer.music.load("background-music.mp3")
mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   

    keys = pygame.key.get_pressed()
    if not any(keys):
        player.updateDirection(player.direction_moving)
    elif keys[pygame.K_a]:
        player.updateDirection("left")
        player.move(-5, 0)
    elif keys[pygame.K_d]:
        player.updateDirection("right")
        player.move(5, 0)
    elif keys[pygame.K_s]:
        player.updateDirection("down")
        player.move(0, 5)
    elif keys[pygame.K_w]:
        player.updateDirection("up")
        player.move(0, -5)

    # Update frame index
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= frame_delay:
        player.current_frame_index = (player.current_frame_index + 1) % player.NUM_FRAMES
        last_update_time = current_time

      # White background
    screen.blit(resized_background, (0,0))
    screen.blit(player.image, (player.rect.x, player.rect.y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
