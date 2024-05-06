class Warrior:
    def __init__ (self, health, attack):
        self._health = health
        self._attack = attack
        self._is_alive = True
    
    def get_health(self):
        return self._health
    
    def set_health(self, health):
        self.health = health
    
    def get_attack(self):
        return self._attack
    
    def set_attack(self, attack):
        self._attack = attack
    
    def get_is_alive(self):
        return self._is_alive

    def fight(self):
        print("hi")
