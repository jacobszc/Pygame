import pygame
import enum
from enum import Enum

class Store(pygame.sprite.Sprite):
     #### enumeration for calls to buy
     pokeball = 1
     potion = 2
     greatball = 3
     repel = 4
     superrepel = 5

  #### default max stock of items on instanciate
     MAX_STOCK_POKEBALL = 100
     MAX_STOCK_POTION = 20
     MAX_STOCK_GREATBALL = 50
     MAX_STOCK_REPEL = 25
     MAX_STOCK_SUPERREPEL = 10
     STORE_IMG = "images/mart.jpg"

  #### validation flags $$$$$$$

     


        
     
    
    
    
     def __init__(self):
        super().__init__()
        
     CURR_STOCK_POKEBALL = MAX_STOCK_POKEBALL
     CURR_STOCK_POTION = MAX_STOCK_POTION
     CURR_STOCK_GREATBALL = MAX_STOCK_GREATBALL
     CURR_STOCK_REPEL = MAX_STOCK_REPEL
     CURR_STOCK_SUPERREPEL = MAX_STOCK_SUPERREPEL

     def printStock(self):

        print(self.CURR_STOCK_POKEBALL,
              self.CURR_STOCK_POTION, 
              self.CURR_STOCK_GREATBALL,
              self.CURR_STOCK_REPEL,
              self.CURR_STOCK_SUPERREPEL)
        
     def buyItem(self, item, quantity):
      
      if(self.isValBuy(item, quantity) == 0):
         print("the store does not have that many of that item!")
         return
      match item:
       case 1:
         self.CURR_STOCK_POKEBALL -= quantity
       case 2:
        self.CURR_STOCK_POTION -= quantity
       case 3:
         self.CURR_STOCK_GREATBALL -= quantity
       case 3:
         self.CURR_STOCK_REPEL -= quantity
       case 3:
         self.CURR_STOCK_SUPERREPEL -= quantity
       case _:
        print("invalid option")

     def isValBuy(self, item, quantity):
       
       BUY_FLAG = 1
       
       if(quantity>self.CURR_STOCK_POKEBALL):
         BUY_FLAG = 0
       elif(quantity>self.CURR_STOCK_POTION):
          BUY_FLAG = 0
       elif(quantity>self.CURR_STOCK_GREATBALL):
          BUY_FLAG = 0
       elif(quantity>self.CURR_STOCK_REPEL):
          BUY_FLAG = 0
       elif(quantity>self.CURR_STOCK_SUPERREPEL):
          BUY_FLAG = 0
       
       return BUY_FLAG

       

       
         
         
