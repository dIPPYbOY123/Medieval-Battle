from Warrior import Warrior
import random

class Lancer(Warrior):
    def __init__(self, name, health, attack, sprite, x, y):
        super().__init__(name, health, attack, sprite, x, y, defense=0)

    def get_attack(self):
        num = random.randint(0, 3)
        return self.attack*num