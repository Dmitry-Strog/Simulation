import random
from time import sleep

from action.pathfinder import PathFinder
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator
from map.coordinate import Coordinates
from map.map import Map
from map.render_Input import RenderInput


class Actions:
    def __init__(self):
        self.map = Map(12, 12)
        self.render = RenderInput(self.map)

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
        self.render.display_map()

    def turn_actions(self):
        """Выполнение 1 хода"""
        while True:

            for value in self.map.get_list_creature():
                x = list([value.hp])
                if value.hp == 0:
                    print('Error')
                path = PathFinder(self.map).find_path(value)
                value.make_move(self.map, path)

            print([(i, i.hp) for i in self.map.get_list_creature()], "- Коолекция существ")
            print()
            print("Следующий ход:")

            if not self.map.get_list_herbivore():
                self.render.display_map()
                print("На карте не осталось травоядных!")
                print([(i, i.hp) for i in self.map.get_list_creature()], "- Коолекция существ")  # Дебаг принт
                break
            self.render.display_map()


