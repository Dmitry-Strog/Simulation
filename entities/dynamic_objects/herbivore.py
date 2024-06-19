from entities.dynamic_objects.creature import Creature


class Herbivore(Creature):
    """ Травоядное, наследуется от Creature. Стремятся найти ресурс (траву), может потратить свой ход на движение
    в сторону травы, либо на её поглощение. """

    def __init__(self, coordinate, speed=1, hp=60, attack=20, health_increase=10, health_decrease=5):
        super().__init__(coordinate, speed, hp, attack, health_increase, health_decrease)
        self._max_hp = 60
        self._health_increase = health_increase
        self._health_decrease = health_decrease

    def __repr__(self):
        return "\U0001F410"
