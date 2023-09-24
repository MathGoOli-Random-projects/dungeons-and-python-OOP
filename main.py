from caracters.Character import Character
from itens.Weapons import LongSword


player = Character("Math", 10, 18, 10, 10, 10, 10)


player.inventory["weapon"] = LongSword()

print(player.attack())
