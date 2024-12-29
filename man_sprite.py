import pygame
import config


  
# Object class 
class Man(pygame.sprite.Sprite): 
    def __init__(self, x, y): 
        super().__init__() 
  
        self.image = pygame.image.load("man.png").convert_alpha() 
        
  
        self.image = pygame.transform.scale(self.image, (64, 64))  # Resize to 64x64
        
        # Set the rect attribute based on the image
        self.rect = self.image.get_rect()
        
        # Set the initial position of the sprite
        self.rect.x = x
        self.rect.y = y
        
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy