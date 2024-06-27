import random

from action.pathfinder import PathFinder
from entities.static_objects.grass import Grass
from map.coordinate import Coordinates
from map.map import Map


class Actions:
    """
    Класс Actions отвечает за управление действиями на карте, включая размещение существ, выполнение ходов и
    управление травой.

    Attributes:
        _maps (Map): Объект карты, на которой происходят все действия.
    """

    def __init__(self, maps: Map):
        """
        Инициализирует объект Actions с заданной картой и населением карты.

        Args:
            maps (Map): Объект карты.
        """
        self._maps = maps

    def init_actions(self, map_population):
        """
        Размещает существа на карте в случайные свободные клетки.
        """
        for entity in map_population:
            entity.perform()

    def turn_actions(self):
        """
        Выполняет один ход для каждого существа на карте, находя для них путь и заставляя их двигаться.
        """
        for value in self._maps.get_list_creature():
            if value in self._maps.get_list_creature():
                path = PathFinder(self._maps).find_path(value)
                value.make_move(self._maps, path)

    def check_and_add_grass(self, map_population):
        """
        Проверяет процентное соотношение клеток с травой на карте и добавляет траву, если её количество ниже
        заданного порога.
        """
        obj_grass = map_population[2]
        total_cells = self._maps.width * self._maps.height
        grass_cells = len(self._maps.get_list_grass())

        if (grass_cells / total_cells) < 0.02:
            obj_grass.perform()
