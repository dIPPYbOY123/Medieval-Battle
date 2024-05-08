from Warrior import Warrior

class Defender(Warrior):
    def __init__(self, health, attack, defense):
        super().__init__(health, attack)
        self.defense = defense

    def set_defense(self, defense):
        self.defense = defense

    def get_defense(self):
        return self.defense