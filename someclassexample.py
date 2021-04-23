import os
import random

class dice_rolls():

    def d6(x):
        total = 0
        for i in range(x):
            total += random.randint(1, 6)
        return total

    def d10(x):
        total = 0
        for i in range(x):
            total += random.randint(1, 10)
        return total

    def d20(x):
        total = 0
        for i in range(x):
            total += random.randint(1, 20)
        return total



class char_stuff():

    def __init__(self):
        self.name = char_stuff.get_charName()
        self.inventory = []
        self.hp = int(dice_rolls.d6(4)) + 15
        self.defence = dice_rolls.d6(4)
        self.strength = dice_rolls.d6(4)
        self.speed = dice_rolls.d6(4)

    def npc_maker(self, name, hp, inventory, mdef, dex, spd):
        pass

    def __str__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        stats = f"************  {self.name}  ************\n"
        stats += f"\n| -  HP =  {self.hp}\n"
        stats += f"| -  DEFENCE =  {self.defence}\n"
        stats += f"| -  STRENGTH =  {self.strength}\n"
        stats += f"| -  SPEED =  {self.speed}\n"
        stats += f"| - INVENTORY : "
        for i in self.inventory:
            stats += f"{i}, "
        stats += "\n"
        stars = len(self.name) * "*"
        stats += f"\n**************{stars}**************"
        return stats

    def get_charName():
        return input("Enter your character's name : ")


    def add_item(self, item):
        self.inventory.append(item)

    def drop_item(self): # im having a hard time getting this to work, hopefully i can get it fixed pretty quick lol
        
        item = input("Which item do you want to drop? : ")

        try:
            item = input("Which item do you want to drop? : ")
            for i in self.inventory:
                if i == item:
                    self.inventory.remove(item)
                    print("Item removed: ", item)
            return
        except IndexError:
            print("You can only drop items currently in your inventory.")
            self.drop_item()






someguy = char_stuff()
print(someguy)
someguy.add_item("my penis")
someguy.add_item("my balls")
someguy.drop_item()
print(someguy)
k = input("lol")
