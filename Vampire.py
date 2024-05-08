from Warrior import Warrior

class Vampire(Warrior):
    def __init__(self, health, attack, vampirism):
        super().__init__(health, attack)
        self.vampirism = vampirism

    def __init__(self, health, attack, defense):
        super().__init__(health, attack)
        self.defense = defense

    def set_vampirism(self, vampirism):
        self.vampirism = vampirism 
    
    def get_vampirism(self):
        return self.vampirism
