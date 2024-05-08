from Warrior import Warrior

class Healer(Warrior):
    def __init__(self, health, attack):
        super().__init__(health, attack)

    def heal(self):
        print("Blank")