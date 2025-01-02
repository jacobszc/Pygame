import Store
from Store import Store


PokeShop = Store()
PokeShop.printStock()

PokeShop.buyItem(PokeShop.potion,30)
PokeShop.printStock()
