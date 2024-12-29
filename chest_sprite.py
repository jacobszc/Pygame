import pygame
import config



class Chest(pygame.sprite.Sprite): 
    def __init__(self, x, y, ): 
        super().__init__() 
        self.image = pygame.image.load("chest.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (64, 64))  # Resize to 64x64
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    