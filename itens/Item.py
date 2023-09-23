class Item:
    def __init__(self, name: str, id: int, value: int, description: str):
        self.name = name
        self.id = id
        self.description = description
        self.value = value

    def action(self):
        pass
