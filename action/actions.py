import random

from action.pathfinder import PathFinder
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator
from entities.entity import Entity
from map.coordinate import Coordinates
from map.map import Map


class Actions:
    def __init__(self):
        self.map = Map(8, 8)

    def init_actions(self, dict_enity):
        """ Выставить существа на карту"""
        for name_cls, count in dict_enity.items():
            for _ in range(count):
                while True:
                    x = random.randint(0, self.map.height - 1)
                    y = random.randint(0, self.map.width - 1)
                    coordinate = Coordinates(x, y)

                    if self.map.is_entity(coordinate):
                        self.map.place_entity(coordinate, name_cls(coordinate))
                        break

        print(list(self.map.collection_entity.values()), "- Коолекция существ")  # Дебаг принт
        self.map.display_map()

    def turn_actions(self):
        """Выполнение 1 хода"""
        while int(input("Нажми 1 - Сделать ход, 0 Закончить игру \n Ответ: ")) == 1:

            for value in self.map.get_list_creature():
                if isinstance(value, Herbivore):
                    path = PathFinder(self.map).find_path(value)
                    value.make_move(self.map, path)

                elif isinstance(value, Predator):
                    pass
                    # path = PathFinder(self.map).find_path(value)
                    # value.make_move(self.map, path)
                    # self.map.display_map()
            if not self.map.get_list_grass():
                print("Всю травку скушали!")
                break
            self.map.display_map()
        # else:
        #     return print("Stop Game")


