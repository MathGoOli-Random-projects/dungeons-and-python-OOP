from itens import Item


class Potion(Item):
    def __init__(self, name: str, id: int, value: int, description: str):
        super().__init__(self, name, id, value, description)

    def action(self):
        return 10
