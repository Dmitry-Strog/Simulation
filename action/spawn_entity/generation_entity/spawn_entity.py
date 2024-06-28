from abc import abstractmethod
import random

from action.spawn_entity.abc_spawn import AbcSpawn
from map.coordinate import Coordinates


class SpawnEntity(AbcSpawn):
    """
    Класс SpawnEntity наследуется от AbcSpawn и отвечает за размещение сущностей на карте в случайных координатах.

    Attributes:
        _maps (Map): Объект карты, на которой происходят все действия.
        _percentage (float): Процентное соотношение сущностей, которые нужно разместить на карте.

    Methods:
        perform():
            Вызывает метод для генерации сущностей на карте.

        _get_random_coordinates(height, width):
            Генерирует случайные координаты на основе высоты и ширины карты.

        generation_entity():
            Запускает процесс добавления сущностей на карту на основе заданного процента.

        _add_entity(number_grass):
            Добавляет указанное количество сущностей на карту в случайные свободные клетки.

        create_creature(coordinate):
            Абстрактный метод для создания сущности на заданных координатах. Должен быть реализован в подклассах.

        matrix_size():
            Возвращает общее количество клеток на карте.
    """

    def __init__(self, maps, percentage=0):
        """
        Инициализирует объект SpawnEntity с заданной картой и процентом размещения сущностей.

        Args:
            maps (Map): Объект карты.
            percentage (float): Процентное соотношение сущностей для размещения.
        """
        super().__init__(maps)
        self._maps = maps
        self._percentage = percentage

    def perform(self):
        """Вызывает метод для генерации сущностей на карте."""
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
        """Запускает процесс добавления сущностей на карту на основе заданного процента."""
        self._add_entity(self.matrix_size() * self._percentage)

    def _add_entity(self, number_grass: float):
        """
        Добавляет указанное количество сущностей на карту в случайные свободные клетки.

        Args:
            number_grass (int): Количество сущностей для добавления на карту.
        """
        for _ in range(int(number_grass)):
            x, y = self._get_random_coordinates(self._maps.height, self._maps.width)
            coordinate = Coordinates(x, y)
            if self._maps.is_entity(coordinate):
                self._maps.place_entity(coordinate, self.create_creature(coordinate))

    @abstractmethod
    def create_creature(self, coordinate):
        """
        Абстрактный метод для создания сущности на заданных координатах.

        Args:
            coordinate (Coordinates): Координаты для создания сущности.

        Raises:
            NotImplementedError: Если метод не реализован в подклассах.
        """
        raise NotImplementedError

    def matrix_size(self):
        """
        Возвращает общее количество клеток на карте.

        Returns:
            int: Общее количество клеток (высота * ширина).
        """
        return self._maps.width * self._maps.height
