import pygame

# defined global pathing variables

closed_chest = "chest.png"
open_chest = "open_chest.png"
man = "man.png"


## meta data for extrracting sprites from sprite sheet
frame_width = 64
frame_height = 64
rows = 4
cols = 5

frame_up_0 = 0, 0, 64, 64
frame_up_1 = 64, 0, 64, 64
frame_up_2 = 128, 0, 64, 64
frame_up_3 = 192, 0, 64, 64
frame_up_4 = 256, 0, 64, 64
frame_up_5 = 320, 0, 64, 64
frame_up_6 = 384, 0, 64, 64





direction_moving = "down"   #default direction when loading sprite is down

