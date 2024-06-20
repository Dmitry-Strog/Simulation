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
        _map_population (dict): Словарь, определяющий количество каждого типа существа на карте.
        _grass_percentage (float): Процентное значение, определяющее минимальный порог травы на карте.
    """

    def __init__(self, maps: Map, map_population: dict):
        """
        Инициализирует объект Actions с заданной картой и населением карты.

        Args:
            maps (Map): Объект карты.
            map_population (dict): Словарь, где ключи - классы существ, а значения - их количество.
        """
        self._maps = maps
        self._map_population = map_population
        self._grass_percentage = 0.03

    def init_actions(self):
        """
        Размещает существа на карте в случайные свободные клетки в соответствии с map_population.
        """
        for name_cls, count in self._map_population.items():
            for _ in range(count):
                while True:
                    x, y = self._get_random_coordinates(self._maps.height, self._maps.width)
                    coordinate = Coordinates(x, y)
                    if self._maps.is_entity(coordinate):
                        self._maps.place_entity(coordinate, name_cls(coordinate))
                        break

    def turn_actions(self):
        """
        Выполняет один ход для каждого существа на карте, находя для них путь и заставляя их двигаться.
        """
        for value in self._maps.get_list_creature():
            if value in self._maps.get_list_creature():
                path = PathFinder(self._maps).find_path(value)
                value.make_move(self._maps, path)

    @staticmethod
    def _get_random_coordinates(height: int, width: int) -> tuple:
        """
        Генерирует случайные координаты на основе высоты и ширины карты.

        Args:
            height (int): Высота карты.
            width (int): Ширина карты.

        Returns:
            tuple: Случайные координаты (x, y).
        """
        x = random.randint(0, height - 1)
        y = random.randint(0, width - 1)
        return x, y

    def check_and_add_grass(self):
        """
        Проверяет процентное соотношение клеток с травой на карте и добавляет траву, если её количество ниже
        заданного порога.
        """
        total_cells = self._maps.width * self._maps.height
        grass_cells = len(self._maps.get_list_grass())

        if (grass_cells / total_cells) < self._grass_percentage:
            self._add_grass(total_cells * self._grass_percentage)

    def _add_grass(self, number_grass: int):
        """
        Добавляет траву на карту в случайные свободные клетки.

        Args:
            number_grass (int): Количество клеток с травой, которые нужно добавить.
        """
        for _ in range(int(number_grass)):
            x, y = self._get_random_coordinates(self._maps.height, self._maps.width)
            coordinate = Coordinates(x, y)
            if self._maps.is_entity(coordinate):
                self._maps.place_entity(coordinate, Grass(coordinate))

