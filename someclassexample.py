


class Character():

    def __init__(self, name, hp, inventory, Def, int, spd):
        self.name = name
        self.hp = hp
        self.inventory = inventory
        self.Def = Def
        self.int = int
        self.spd = spd


someguy = Character('bloke', 30, ['Iron Dagger', 'Leather Armour'], 5, 3, 7)

print(someguy.inventory)
