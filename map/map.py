import random

from entities.dynamic_objects.creature import Creature
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator
from entities.static_objects.grass import Grass
from map.coordinate import Coordinates


class Map:
    """
    Класс Map представляет карту, на которой располагаются различные сущности.

    Attributes:
        height (int): Высота карты.
        width (int): Ширина карты.
        _collection_entity (dict): Словарь для хранения сущностей на карте.
    """

    def __init__(self, height, width):
        """
        Инициализация объекта карты с заданными размерами.

        Args:
            height (int): Высота карты.
            width (int): Ширина карты.
        """
        self._height = height
        self._width = width
        self._collection_entity = {}

    @property
    def height(self):
        """
        Возвращает высоту карты.

        Returns:
            int: Высота карты.
        """
        return self._height

    @property
    def width(self):
        """
        Возвращает ширину карты.

        Returns:
            int: Ширина карты.
        """

        return self._width

    def place_entity(self, coord, entity):
        """
        Размещает сущность на указанных координатах.

        Args:
            coord (Coordinates): Координаты, на которых размещается сущность.
            entity (Entity): Объект сущности, которую нужно разместить.
        """
        self._collection_entity[coord] = entity
        entity.coordinate = coord

    def get_entity(self, coordinate):
        """
        Возвращает сущность по заданным координатам.

        Args:
            coordinate (tuple): Кортеж с координатами (row, column).

        Returns:
            Entity or None: Сущность на указанных координатах или None, если клетка пуста.
        """
        key = Coordinates(coordinate[0], coordinate[1])
        return self._collection_entity.get(key, None)

    def remove_entity(self, coordinate):
        """
        Удаляет сущность с указанных координат.

        Args:
            coordinate (tuple): Кортеж с координатами (row, column).
        """
        key = Coordinates(coordinate[0], coordinate[1])
        if key in self._collection_entity:
            del self._collection_entity[key]

    def is_entity(self, coordinate):
        """
        Проверяет, свободна ли указанная клетка на карте.

        Args:
            coordinate (tuple): Кортеж с координатами (row, column).

        Returns:
            bool: True, если клетка свободна (нет сущности), иначе False.
        """
        return self._collection_entity.get(coordinate) is None

    def get_all_entity(self):
        """
        Возвращает все сущности на карте.

        Returns:
            list: Список всех сущностей на карте.
        """
        return list(self._collection_entity.values())

    def get_list_creature(self):
        """
        Возвращает список всех существ на карте.

        Returns:
            list: Список всех существ на карте.
        """
        return [entity for entity in self._collection_entity.values() if isinstance(entity, Creature)]

    def get_list_grass(self):
        """
        Возвращает список всех объектов травы на карте.

        Returns:
            list: Список всех объектов травы на карте.
        """
        return [entity for entity in self._collection_entity.values() if isinstance(entity, Grass)]

    def get_list_herbivore(self):
        """
        Возвращает список всех травоядных на карте.

        Returns:
            list: Список всех травоядных на карте.
        """
        return [entity for entity in self._collection_entity.values() if isinstance(entity, Herbivore)]

    def get_list_predators(self):
        """
        Возвращает список всех хищников на карте.

        Returns:
            list: Список всех хищников на карте.
        """
        return [entity for entity in self._collection_entity.values() if isinstance(entity, Predator)]

