import pygame


class Sprite():
    
    
    
    FRAME_WIDTH = 64
    FRAME_HEIGHT = 64
    NUM_FRAMES = 6
    clock = pygame.time.Clock()
    LAST_UPDATE_TIME = pygame.time.get_ticks()
    CURRENT_TIME = None
    CURPLAYER = None
    CUR_SPRITE_SHEET = None

    def __init__(self, Player, INITAL_SPAWN_LOCATION, sprite_sheet):
        super().__init__()
        self.CURPLAYER = Player
        self.CUR_SPRITE_SHEET = sprite_sheet
        self.current_frame_index = 0
        self.direction_moving = "down"
        self.image = self.extract_frame(self.current_frame_index, 0)
        self.rect = self.image.get_rect()
        self.rect.x = INITAL_SPAWN_LOCATION[0]
        self.rect.y = INITAL_SPAWN_LOCATION[1]
      
    def updateDirection(self, direction_moving):
        
        
        self.direction_moving = direction_moving
      
            
        if direction_moving == "up":
            self.image = self.extract_frame(self.current_frame_index, 0)
        elif direction_moving == "down":
            self.image = self.extract_frame(self.current_frame_index, 2)
        elif direction_moving == "left":
            self.image = self.extract_frame(self.current_frame_index, 1)
        elif direction_moving == "right":
            self.image = self.extract_frame(self.current_frame_index, 3)
        

    def extract_frame(self, xindex, yindex):
        x = xindex * self.FRAME_WIDTH
        y = yindex * self.FRAME_HEIGHT
        return self.CUR_SPRITE_SHEET.subsurface(pygame.Rect(x, y, self.FRAME_WIDTH, self.FRAME_HEIGHT))

    
            
    
    def updateFrameIndex(self):
     self.CURRENT_TIME = pygame.time.get_ticks()
     
     frame_delay = 500  # 500 ms
     if self.CURRENT_TIME - self.LAST_UPDATE_TIME >= frame_delay:
      self.current_frame_index = (self.current_frame_index + 1) % self.NUM_FRAMES
      self.LAST_UPDATE_TIME = self.CURRENT_TIME
      
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
       

    

    def makePlayerMove(self):
     keys = pygame.key.get_pressed()
     if not any(keys):
        self.updateDirection(self.direction_moving)
     elif keys[pygame.K_a]:
        self.updateDirection("left")
        self.move(-5, 0)
     elif keys[pygame.K_d]:
        self.updateDirection("right")
        self.move(5, 0)
     elif keys[pygame.K_s]:
        self.updateDirection("down")
        self.move(0, 5)
     elif keys[pygame.K_w]:
        self.updateDirection("up")
        self.move(0, -5)