from entities.dynamic_objects.creature import Creature


class Herbivore(Creature):
    """ Травоядное, наследуется от Creature. Стремятся найти ресурс (траву), может потратить свой ход на движение
    в сторону травы, либо на её поглощение. """

    def __init__(self, coordinate, speed=1, hp=60, attack=20):
        super().__init__(coordinate, speed, hp, attack)
        self._max_hp = 60

    def eat(self, world_map, path):
        grass = path[-1]
        obj = world_map.get_entity(grass)
        obj.hp -= self.attack
        if obj.hp <= 0:
            world_map.remove_entity(grass)
            self.add_health()
            print(f"{self} - {self.hp} Убил {obj}")

    def add_health(self):
        self.hp += 10
        self.check_max_hp()

    def decrease_health(self):
        self.hp -= 5

    def __repr__(self):
        return "\U0001F410"
