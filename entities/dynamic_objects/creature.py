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
        self._max_hp = hp

    def make_move(self, world_map, path):

        if not path:
            print(self, "Не найден путь")
            return

        if self.hp > 0:
            if self.speed + 1 >= len(path):
                self.eat(world_map, path)
                obj = world_map.get_entity(path[-1])
                if obj.hp <= 0:
                    if self.is_check_max_hp():
                        self.add_health()
                    print(f"{self} - {self.hp} Убил {obj}")
                    world_map.remove_entity(path[-1])
            else:
                # Сделать шаг по пути
                var = path[self.speed]
                if world_map.is_entity(Coordinates(var[0], var[1])):
                    world_map.place_entity(Coordinates(var[0], var[1]), self)
                    world_map.remove_entity(path[0])
                    print("hp до", self.hp, self)
                    self.decrease_health()
                    self.is_alive_creature(world_map, (self.coordinate.row, self.coordinate.column))
                    print("hp после", self.hp, self)
                else:
                    print(f"{self} Нет пути!")
        else:
            world_map.remove_entity((self.coordinate.row, self.coordinate.column))

    @abstractmethod
    def eat(self, world_map, path):
        """Метод Атаки сущетсва"""
        pass

    def is_alive_creature(self, world_map, coor: tuple):
        if self.hp <= 0:
            print(self, 'Умер с голоду')
            world_map.remove_entity(coor)

    def is_check_max_hp(self, ):
        """Проверка hp существа"""
        if self.hp < self._max_hp:
            return True
        return False

    @abstractmethod
    def add_health(self):
        """Добавить существу hp"""
        pass

    @abstractmethod
    def decrease_health(self):
        """Уменьшить здоровье hp"""
        pass
