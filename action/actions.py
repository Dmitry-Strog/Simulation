import random
from time import sleep

from action.pathfinder import PathFinder
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator
from entities.entity import Entity
from map.coordinate import Coordinates
from map.map import Map


class Actions:
    def __init__(self):
        self.map = Map(12, 12)

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
        while True:

            for value in self.map.get_list_creature():

                if isinstance(value, Herbivore):
                    path = PathFinder(self.map).find_path(value)
                    value.make_move(self.map, path)

                elif isinstance(value, Predator):
                    path = PathFinder(self.map).find_path(value)
                    value.make_move(self.map, path)
                if value.hp <= 0:
                    self.map.remove_entity((value.coordinate.row, value.coordinate.column))
            print("=================================================================================")
            print([(i, i.hp) for i in self.map.get_list_creature()], "- Коолекция существ")
            # if not self.map.get_list_grass():
            #     self.map.display_map()
            #     print("Всю травку скушали!")
            #     print([(i, i.hp)for i in self.map.collection_entity.values()], "- Коолекция существ")  # Дебаг принт
            #     break
            if not self.map.get_list_herbivore():
                self.map.display_map()
                print("На карте не осталось травоядных!")
                print([(i, i.hp) for i in self.map.get_list_creature()], "- Коолекция существ")  # Дебаг принт
                break
            sleep(1)
            self.map.display_map()


