
class Character:
    """ basic class to make all type of class or monster """
    def __init__(self,
                 name: str,
                 strength: int,
                 dexterity: int,
                 constitution: int,
                 integigence: int,
                 winsdom: int,
                 charisma: int):

        if type(name) != str:
            raise TypeError("name must be str")
        self.name = name

        self.char_status = {
            "strength": strength,
            "dexterity": dexterity,
            "constitution": constitution,
            "integigence": integigence,
            "winsdom": winsdom,
            "charisma": charisma
        }

        for status in self.char_status:
            if type(self.char_status[status]) != int:
                raise TypeError(f"{status} must be int")

        self.make_modifier()
        self.calc_def()
        self.make_inventory()

    def make_modifier(self):
        self.char_modifiers = {}

        for status in self.char_status:
            self.char_modifiers[status] = int(
                (self.char_status[status] - 10) / 2)

    def calc_def(self):
        self.defensive_class = 10 + self.char_modifiers["dexterity"]

    def make_inventory(self):
        self.inventory = {
            "weapom": None,
            "body": None,
            "shield": None
        }

    def attack(self):
        pass
