import os
import random
import keyboard

class diceRolls():

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

    def stat_roll():
        number = diceRolls.d6(4)
        while number < 8:
            number = diceRolls.d6(4)
        return number


class char_stuff():
    def __init__(self):
        self.name = char_stuff.get_charName()
        self.inventory = []
        self.hp = diceRolls.stat_roll() + 15
        self.defence = diceRolls.stat_roll()
        self.strength = diceRolls.stat_roll()
        self.speed = diceRolls.stat_roll()

    def npc_maker(self, name, hp, inventory, mdef, dex, spd):
        pass

    def __str__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        stats = f"************| {self.name} |************\n"
        stats += f"\n| -  HP =  {self.hp}\n"
        stats += f"| -  DEFENCE =  {self.defence}\n"
        stats += f"| -  STRENGTH =  {self.strength}\n"
        stats += f"| -  SPEED =  {self.speed}\n"
        stats += f"| -  INVENTORY : "
        for i in self.inventory:
            if i == self.inventory[len(self.inventory) - 1]:
                stats += f"{i}."
            else:
                stats += f"{i}, "
        stats += "\n"
        stars = len(self.name) * "*"
        stats += f"\n**************{stars}**************"
        return stats

    def get_charName():
        return input("Enter your character's name : ")


    def add_item(self, item):
        self.inventory.append(item)

    def drop_item(self):
        while True:
            item = input("What item do you want to drop? : ")
            answer = input("Do you really want to drop it? Yes or No : ")
            if answer.upper() == 'NO':
                return

            try:
                self.inventory.remove(item)
                print("Items removed: ", item)
                print("Press Space to continue.")
                keyboard.wait('space')
                break

            except ValueError:
                print("You can only drop something currently in your inventory.")
                continue

class action(): # lawsuit
    pass

def main():

    someguy = char_stuff()
    someguy.add_item("Iron Dagger")
    someguy.add_item("Iron Chestplate")
    someguy.add_item("Iron Leggings")
    someguy.add_item("Iron Helmet")
    someguy.add_item("Iron Boots")
    print(someguy)
    someguy.drop_item()
    print(someguy)


if __name__ == "__main__":
    main()
