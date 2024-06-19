from abc import abstractmethod

from entities.entity import Entity
from map.coordinate import Coordinates


class Creature(Entity):
    """ Абстрактный класс, наследуется от Entity. Существо, имеет скорость (сколько клеток может пройти за 1 ход),
    количество HP. Имеет абстрактный метод make_move() - сделать ход. Наследники будут реализовывать этот метод каждый
    по-своему. """

    def __init__(self, coordinate: Coordinates, speed, hp, attack, health_increase, health_decrease):
        super().__init__(coordinate)
        self.speed = speed
        self.hp = hp
        self.attack = attack
        self._max_hp = hp
        self._health_increase = health_increase
        self._health_decrease = health_decrease

    def make_move(self, world_map, path):

        if not path:
            print(self, "Не найден путь")
            return

        if self.hp <= 0:
            world_map.remove_entity((self.coordinate.row, self.coordinate.column))
            return

        if self.speed + 1 >= len(path):
            self.eat(world_map, path)
        else:
            next_position = path[self.speed]
            world_map.place_entity(Coordinates(next_position[0], next_position[1]), self)
            world_map.remove_entity(path[0])
            self.decrease_health()
            self.is_alive_creature(world_map, (self.coordinate.row, self.coordinate.column))

    def eat(self, world_map, path):
        target = path[-1]
        obj = world_map.get_entity(target)
        obj.hp -= self.attack
        if obj.hp <= 0:
            world_map.remove_entity(target)
            self.add_health()
            print(f"{self}({self.hp}) Съел {obj}")

    def is_alive_creature(self, world_map, coor: tuple):
        """Проверяет, живо ли существо и удаляет его, если оно мертво."""
        if self.hp <= 0:
            print(self, 'Умер с голоду')
            world_map.remove_entity(coor)

    def check_max_hp(self, ):
        """Проверка, чтобы hp существа не превышало максимальное значение."""
        if self.hp > self._max_hp:
            self.hp = self._max_hp

    def add_health(self):
        self.hp += self._health_increase
        self.check_max_hp()

    def decrease_health(self):
        self.hp -= self._health_decrease
