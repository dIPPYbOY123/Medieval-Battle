from Warrior import Warrior

class Healer(Warrior):
    def __init__(self, name, health, attack, sprite, x, y):
        super().__init__(name, health, attack, sprite, x, y, defense=0)
        self.heal_amount = 2