import random
from action.pathfinder import PathFinder
from entities.static_objects.grass import Grass
from map.coordinate import Coordinates
from map.map import Map
from map.render_Input import RenderInput


class Actions:
    def __init__(self, maps: Map, map_population: dict):
        self.maps = maps
        self.map_population = map_population
        self._grass_percentage = 0.03

    def init_actions(self):
        """ Выставить существа на карту"""
        for name_cls, count in self.map_population.items():
            for _ in range(count):
                while True:
                    x, y = self.get_random_coordinates(self.maps.height, self.maps.width)
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

    @staticmethod
    def get_random_coordinates(height, width):
        x = random.randint(0, height - 1)
        y = random.randint(0, width - 1)
        return x, y

    def check_and_add_grass(self):
        """ Проверяет количество клеток с травой на карте и добавляет траву, если
        её количество опускается ниже заданного порога. """
        total_cells = self.maps.width * self.maps.height
        grass_cells = len(self.maps.get_list_grass())

        if (grass_cells / total_cells) < self._grass_percentage:
            self.add_grass(total_cells * self._grass_percentage)

    def add_grass(self, number_glass):
        for _ in range(int(number_glass)):
            x, y = self.get_random_coordinates(self.maps.height, self.maps.width)
            coordinate = Coordinates(x, y)
            if self.maps.is_entity(coordinate):
                self.maps.place_entity(coordinate, Grass(coordinate))
