from Warrior import Warrior

class Defender(Warrior):
    def __init__(self, name, health, attack, defense, sprite, x, y):
        super().__init__(name, health, attack, sprite, x, y, defense)
        self.defense = defense

    def set_defense(self, defense):
        self.defense = defense

    def get_defense(self):
        return self.defense