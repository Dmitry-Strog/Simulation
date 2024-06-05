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
        self.map = self.create_map()

    def create_map(self):
        """ Создание поле карты"""
        return [['.'] * self.height for _ in range(self.width)]

    def place_entity(self, coord, entity):
        """Размещение сущности"""
        self.collection_entity[coord] = entity
        entity.coordinate = coord

    def get_entity(self, coor):
        key = Coordinates(coor[0], coor[1])
        return self.collection_entity[key]

    def remove_entity(self, entity):
        """Удаление существа"""
        key = Coordinates(entity[0], entity[1])
        if key in self.collection_entity:
            del self.collection_entity[key]
        else:
            print("Координата не найдена")

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

    def update_map(self):
        """Обновляет карту, размещая существа"""
        self.map = self.create_map()  # Очистить карту
        for coordinates, creature in self.collection_entity.items():
            self.map[coordinates.row][coordinates.column] = str(creature)

    def display_map(self):
        """Отображает карту в консоли"""
        self.update_map()  # Обновить карту перед отображением
        for row in self.map:
            print('[' + ']['.join(row) + ']')
        print()


