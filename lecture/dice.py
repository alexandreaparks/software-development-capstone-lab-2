import random

class Dice:
    def __init__(self, sides=6):  # 6 is the default num of dice sides
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


dice = Dice(6)  # 6 for number of sides
for roll in range(100):  # roll 100 times
    print(dice.roll())

dice2 = Dice()  # uses default of 6 sides
print(dice2.roll())