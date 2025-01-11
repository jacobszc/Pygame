import Sprite
from Sprite import Sprite


class Collision:
    x1 = 0 
    y1 = 0
    x2 =0
    y2 =0
    width1 = 0
    width2=0
    height1 =0
    height2=0

    horizontal_touch = False
    vertical_touch = False
    corner_touch = False


    whatever = 0

    def __init__(self):
        super().__init__



    def isCollision(self,sprite1, sprite2):
  ### top left pixel of first sprite
     self.x1 = sprite1.rect.x
     self.y1 = sprite1.rect.y  
  
  ## top left pixel of second sprite
     self.x2 = sprite2.rect.x
     self.y2 = sprite2.rect.y 

     self.height1 = sprite1.FRAME_HEIGHT
     self.width1 = sprite1.FRAME_WIDTH

     self.height2 = sprite2.FRAME_HEIGHT
     self.width2 = sprite2.FRAME_WIDTH

     self.printCoor()

     
     if (self.x1 + self.width1 == self.x2 or self.x2 + self.width2 == self.x1) and (self.y1 < self.y2 + self.height2 and self.y2 < self.y1 + self.height1):
        self.horizontal_touch = True
    
    
    # Check if vertically adjacent
     if (self.y1 + self.height1 == self.y2 or self.y2 + self.height2 == self.y1) and (self.x1 < self.x2 +self.width2 and self.x2 < self.x1 + self.width1):
         self.vertical_touch = True
    
    
    # Check if corners touch
     if (self.x1 + self.width1 == self.x2 and self.y1 + self.height1 == self.y2) or (self.x2 + self.width2 == self.x1 and self.y2 + self.height2 == self.y1):
         self.corner_touch = True
    
     if(self.horizontal_touch == True) or (self.vertical_touch == True) or (self.corner_touch== True):
        print("COLLISION!")
        
    
     
     return self.horizontal_touch or self.vertical_touch or self.corner_touch

     
     


 
     
     
        
    def printCoor(self):
  
     print("Player X,Y: ", self.x1, ", ", self.x2 )
     print("/n")
     print("Shop X,Y: ", self.y2, ", ", self.y2 )
     print("/n")



