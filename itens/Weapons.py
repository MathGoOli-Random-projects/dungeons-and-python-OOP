
from random_events.dices import D10, D4


class Weapon():

    def __init__(self,
                 name,
                 value,
                 description,
                 damage=[D4],
                 modifier="strength"):

        self.damage = damage
        self.modifier = modifier

    def action(self):
        return {"damage": self.damage, "modifier": self.modifier}


class LongSword(Weapon):
    def __init__(self):
        super().__init__(name="longsword",
                         value=25,
                         description="longsword",
                         damage=[D10],
                         modifier="strength")


