import random


class Dice:
    faces = 1

    @classmethod
    def roll(cls):
        return random.randint(1, cls.faces)

    @classmethod
    def roll_advantage(cls):
        roll1 = cls.roll()
        roll2 = cls.roll()

        if roll1 >= roll2:
            return roll1
        return roll2

    @classmethod
    def roll_disadvantage(cls):
        roll1 = cls.roll()
        roll2 = cls.roll()

        if roll1 <= roll2:
            return roll1
        return roll2


class D4(Dice):
    faces = 4


class D10(Dice):
    faces = 10


class D20(Dice):
    faces = 20
