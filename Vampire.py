from Warrior import Warrior
import random

class Vampire(Warrior):
    def __init__(self, name, health, attack, vampirism, sprite, x, y):
        super().__init__(name, health, attack, sprite, x, y, defense=0)
        self.vampirism = vampirism

    def get_attack(self):
        num = random.randint(0, 3)
        if num == 1:
            return self.attack*2
        else:
            return self.attack

    def set_vampirism(self, vampirism):
        self.vampirism = vampirism 
    
    def get_vampirism(self):
        return self.vampirism
