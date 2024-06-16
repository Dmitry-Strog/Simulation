from entities.dynamic_objects.creature import Creature


class Predator(Creature):
    """ Хищник, наследуется от Creature. В дополнение к полям класса Creature, имеет силу атаки.
    На что может потратить ход хищник:
    Переместиться (чтобы приблизиться к жертве - травоядному)
    Атаковать травоядное. При этом количество HP травоядного уменьшается на силу атаки хищника.
    Если значение HP жертвы опускается до 0, травоядное исчезает """

    def __init__(self, coordinate, speed=1, hp=100, attack=20):
        super().__init__(coordinate, speed, hp, attack)
        self._max_hp = 100

    def eat(self, world_map, path):
        herbivore = path[-1]
        obj = world_map.get_entity(herbivore)
        obj.hp -= self.attack
        if obj.hp <= 0:
            world_map.remove_entity(herbivore)
            self.add_health()
            print(f"{self} - {self.hp} Убил {obj}")

    def add_health(self):
        self.hp += 20
        self.check_max_hp()

    def decrease_health(self):
        self.hp -= 10

    def __repr__(self):
        return "\U0001F43A"
