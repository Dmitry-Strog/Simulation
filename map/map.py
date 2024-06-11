import random

from entities.dynamic_objects.creature import Creature
from entities.dynamic_objects.herbivore import Herbivore
from entities.static_objects.grass import Grass
from map.coordinate import Coordinates


class Map:
    """ Карта, содержит в себе коллекцию для хранения существ и их расположения.
    Советую не спешить использовать двумерный массив или список списков,
    а подумать какие ещё коллекции могут подойти."""
    def __init__(self, height, width):
        self.height = height  # высота карты
        self.width = width  # ширина карты
        self.collection_entity = {}

    def place_entity(self, coord, entity):
        """Размещение сущности"""
        self.collection_entity[coord] = entity
        entity.coordinate = coord

    def get_entity(self, coor):
        key = Coordinates(coor[0], coor[1])
        return self.collection_entity.get(key, None)

    def remove_entity(self, entity):
        """Удаление существа"""
        key = Coordinates(entity[0], entity[1])
        if key in self.collection_entity:
            del self.collection_entity[key]

    def is_entity(self, coor):
        """Проверка не занята ли клетка"""
        if self.collection_entity.get(coor) is None:
            return True

    def get_list_creature(self):
        """ Получить список существ """
        population_creatures = []
        for value in self.collection_entity.values():
            if isinstance(value, Creature):
                population_creatures.append(value)
        return population_creatures

    def get_list_grass(self):
        """Получить список травы"""
        list_grass = []
        for entity in self.collection_entity.values():
            if isinstance(entity, Grass):
                list_grass.append(entity)
        return list_grass

    def get_list_herbivore(self):
        """Получить список травы"""
        list_herbivore = []
        for entity in self.collection_entity.values():
            if isinstance(entity, Herbivore):
                list_herbivore.append(entity)
        return list_herbivore



