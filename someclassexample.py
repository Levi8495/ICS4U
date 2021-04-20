


class Character():

    def __init__(self, name, hp, inventory, mdef, dex, spd):
        self.name = name
        self.hp = hp
        self.inventory = inventory
        self.mdef = mdef
        self.dex = dex
        self.spd = spd


someguy = Character('bloke', 30, ['Iron Dagger', 'Leather Armour'], 5, 3, 7)

print(someguy.inventory)
