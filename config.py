import pygame

# sizes of screens and backgrounds
SCREEN_SIZE = 800 , 800 
BACKGROUND_SIZE = SCREEN_SIZE



# spawn locations
INITIAL_SPAWN_LOC = 400 , 400
SHOP_LOC = 400, 400

# player PARAMS
SAMPLE_NAME = "Jake"



# 2 variables used to delay calling functions by a given interval

last_collision_check_time = 0  # Stores the last time the collision was checked
collision_check_interval = 2000  # 2 seconds in milliseconds




def start_the_game():

    print("game started")
    


def set_difficulty(DIFFICULTY):
    
    if(DIFFICULTY == 1):
        DIFFICULTY[0] ='Hard'

    if(DIFFICULTY == 2):
        DIFFICULTY[0] ='Easy'   

    

