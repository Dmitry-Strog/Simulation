import random
from action.pathfinder import PathFinder
from map.coordinate import Coordinates
from map.map import Map
from map.render_Input import RenderInput


class Actions:
    def __init__(self, maps: Map, map_population: dict):
        self.maps = maps
        self.map_population = map_population

    def init_actions(self):
        """ Выставить существа на карту"""
        for name_cls, count in self.map_population.items():
            for _ in range(count):
                while True:
                    x = random.randint(0, self.maps.height - 1)
                    y = random.randint(0, self.maps.width - 1)
                    coordinate = Coordinates(x, y)

                    if self.maps.is_entity(coordinate):
                        self.maps.place_entity(coordinate, name_cls(coordinate))
                        break

    def turn_actions(self):
        """Выполнение 1 хода"""
        for value in self.maps.get_list_creature():
            if value in self.maps.get_list_creature():
                path = PathFinder(self.maps).find_path(value)
                value.make_move(self.maps, path)

    def add_glass(self):
        pass