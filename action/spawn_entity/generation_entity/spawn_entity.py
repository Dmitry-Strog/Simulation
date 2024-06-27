import random
from abc import abstractmethod

from action.spawn_entity.abc_spawn import AbcSpawn
from map.coordinate import Coordinates


class SpawnEntity(AbcSpawn):

    def __init__(self, maps, percentage=0):
        super().__init__(maps)
        self._maps = maps
        self._percentage = percentage

    def perform(self):
        self.generation_entity()

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

    def generation_entity(self):
        self._add_entity(self.matrix_size() * self._percentage)

    def _add_entity(self, number_grass: int):
        for _ in range(int(number_grass)):
            x, y = self._get_random_coordinates(self._maps.height, self._maps.width)
            coordinate = Coordinates(x, y)
            if self._maps.is_entity(coordinate):
                self._maps.place_entity(coordinate, self.create_creature(coordinate))

    @abstractmethod
    def create_creature(self, coordinate):
        raise NotImplemented

    def matrix_size(self):
        return self._maps.width * self._maps.height
