class Warrior:
    def __init__ (self, health, attack):
        self.health = health
        self.attack = attack
        self.is_alive = True
    
    def get_health(self):
        return self.health
    
    def set_health(self, health):
        self.health = health
    
    def get_attack(self):
        return self.attack
    
    def set_attack(self, attack):
        self.attack = attack

    def get_is_alive(self):
        if self.health > 0:
            return self.is_alive

    def fight(self, opponent):
        print(opponent)
        while self.get_is_alive() and opponent.get_is_alive():
            opponent.set_health(opponent.get_health() - self.get_attack())
            if opponent.get_is_alive():
                self.set_health(self.get_health() - opponent.get_attack())
        return self.get_is_alive()