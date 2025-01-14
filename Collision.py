import Sprite
from Sprite import Sprite


class Collision:
    playerX = 0 
    playerY = 0
    shopX =0
    shopY =0
    
    
    playerXline = 0
    playerYline = 0
    
    shopXline = 0
    shopYline =0

    playerXcoors = []
    shopXcoors = []

    
    
    

    horizontal_touch = False
    vertical_touch = False
    corner_touch = False


    whatever = 0

    def __init__(self):
        super().__init__



    def isCollision(self,sprite1, sprite2):
       
          ## check for corners


          ## check for lines
       
       self.playerX = sprite1.rect.x
       self.playerY = sprite1.rect.y

       self.shopX = sprite2.rect.x
       self.shopY = sprite2.rect.y
       
       
      
 ############# left corner X axis check #########################
       if(self.shopX <= self.playerX <= self.shopX + 64):
         
          print("your left corner is toucing the shops x line on the top")
    
  ########## right corner x axis check
       if(self.shopX <= self.playerX + 64 <= self.shopX + 64):
         
          print("your right corner is toucing the shops x line on the top")
        
       if(self.shopY <= self.playerY <= self.shopY + 64):
         
          print("your left corner is toucing the shops Y line on the left")

       if(self.shopY >= self.playerY + 64 <= self.shopY + 64):
          
          print("your left corner is toucing the shops Y line on the left")
       
  ###### left corner y axis check 
       
       
       
       

       if(self.playerX + self.playerY == self.shopX + self.shopY):  ### must look at this again. this works for most cases but could be buggy
         print("you are perfectly overlapped")

       print("Player :", sprite1.rect.x, " ", sprite1.rect.y)
       print("Shop", sprite2.rect.x, " ", sprite2.rect.y)
      
       
          #####################
          #####################
          #####################
          ##########$$XX#######
          ##########$$XX#######
          #####################
          #####################

       

     

     
     
     


 
     
     
        
    def printCoor(self):
  
     print("Player X,Y: ", self.x1, ", ", self.x2 )
     print("/n")
     print("Shop X,Y: ", self.y2, ", ", self.y2 )
     print("/n")



