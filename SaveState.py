import Store
from Store import Store

class SaveState():


    CUR_PLAYER = None
    CUR_STORE = Store()
    
    def __init__(self, PLAYER, STORE ):
        super().__init__()
     
        


    def save(self, PLAYER, STORE):

        self.CUR_PLAYER = PLAYER
        self.CUR_STORE = STORE
     

    def print(self):
        self.CUR_STORE.printStock()
