from entities.dynamic_objects.creature import Creature


class Herbivore(Creature):
    """ Травоядное, наследуется от Creature. Стремятся найти ресурс (траву), может потратить свой ход на движение
    в сторону травы, либо на её поглощение. """

    def __init__(self, coordinate, speed=1, hp=60, attack=20):
        super().__init__(coordinate, speed, hp, attack)

    def eat(self, world_map, path):
        grass = path[-1]
        obj = world_map.get_entity(grass)
        obj.hp -= self.attack

    def __repr__(self):
        return "H"
