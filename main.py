from Warrior import Warrior
from Knight import Knight
from Defender import Defender
from Vampire import Vampire
from Lancer import Lancer
from Healer import Healer

warrior1 = Warrior(50, 5)
knight1 = Knight(50, 7)
defender1 = Defender(60, 3, 2)
vampire1 = Vampire(40, 4, 0.5)
lancer1 = Lancer(50, 6)
healer1 = Healer(60, 0)

print(f"Warrior Attack: {warrior1.get_attack()}")
print(f"Knight Attack: {knight1.get_attack()}")
print(f"Defender Attack: {defender1.get_attack()}")
print(f"Vampire Attack: {vampire1.get_attack()}")
print(f"Lancer Attack: {lancer1.get_attack()}")
print(f"Healer Attack: {healer1.get_attack()}")