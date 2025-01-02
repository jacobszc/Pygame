import Store
from Store import Store

class SaveState():


    
    CUR_STORE = Store()
    
    def __init__(self, STORE ):
        super().__init__()
     
        self.CUR_STORE = STORE


    def save(self, STORE):

        
        self.CUR_STORE = STORE
     

    def print(self):
        self.CUR_STORE.printStock()


    
