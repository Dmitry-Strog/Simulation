from abc import abstractmethod

from entities.entity import Entity
from map.coordinate import Coordinates


class Creature(Entity):
    """ Абстрактный класс, наследуется от Entity. Существо, имеет скорость (сколько клеток может пройти за 1 ход),
    количество HP. Имеет абстрактный метод make_move() - сделать ход. Наследники будут реализовывать этот метод каждый
    по-своему. """

    def __init__(self, coordinate: Coordinates, speed, hp, attack):
        super().__init__(coordinate)
        self.speed = speed
        self.hp = hp
        self.attack = attack

    def make_move(self, world_map, path):
        if not path:
            print(self, "Не найден путь")
            return
        if self.speed + 1 >= len(path):
            print(self, "Кушаю")
            self.eat(world_map, path)
            obj = world_map.get_entity(path[-1])
            if obj.hp <= 0:
                world_map.remove_entity(path[-1])

        else:
            # Сделать шаг по пути
            var = path[self.speed]
            if world_map.is_entity(Coordinates(var[0], var[1])):
                world_map.place_entity(Coordinates(var[0], var[1]), self)
                world_map.remove_entity(path[0])
            else:
                print(f"{self} Нет пути!")

    @abstractmethod
    def eat(self, world_map, path):
        """Метод Атаки сущетсва"""
        pass
