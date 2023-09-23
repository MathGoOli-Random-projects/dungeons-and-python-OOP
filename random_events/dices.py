import random


class Dice:
    def __init__(self):
        self.faces = 1

    def roll(self):
        return random.randint(1, self.faces)


class D20(Dice):
    def __init__(self):
        super().__init__()
        self.faces = 20
