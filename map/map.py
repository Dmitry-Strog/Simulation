import random

from entities.dynamic_objects.creature import Creature
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator
from entities.static_objects.grass import Grass
from map.coordinate import Coordinates


class Map:
    """ Карта, содержит в себе коллекцию для хранения существ и их расположения.
    Советую не спешить использовать двумерный массив или список списков,
    а подумать какие ещё коллекции могут подойти."""

    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._collection_entity = {}

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def place_entity(self, coord, entity):
        """Размещение сущности"""
        self._collection_entity[coord] = entity
        entity.coordinate = coord

    def get_entity(self, coordinate):
        key = Coordinates(coordinate[0], coordinate[1])
        return self._collection_entity.get(key, None)

    def remove_entity(self, coordinate):
        """Удаление существа"""
        key = Coordinates(coordinate[0], coordinate[1])
        if key in self._collection_entity:
            del self._collection_entity[key]

    def is_entity(self, coordinate):
        """Проверка не свободная ли клетка"""
        return self._collection_entity.get(coordinate) is None

    def get_all_entity(self):
        return self._collection_entity.values()

    def get_list_creature(self):
        """ Получить список существ """
        return [entity for entity in self._collection_entity.values() if isinstance(entity, Creature)]

    def get_list_grass(self):
        """Получить список травы"""
        return [entity for entity in self._collection_entity.values() if isinstance(entity, Grass)]

    def get_list_herbivore(self):
        """Получить список травоядных"""
        return [entity for entity in self._collection_entity.values() if isinstance(entity, Herbivore)]

    def get_list_predators(self):
        """Получить список хищников"""
        return [entity for entity in self._collection_entity.values() if isinstance(entity, Predator)]
