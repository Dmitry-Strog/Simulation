from action.spawn_entity.generation_entity.spawn_entity import SpawnEntity
from entities.dynamic_objects.predator import Predator


class SpawnPredator(SpawnEntity):
    """
    Класс SpawnPredator отвечает за создание и размещение объектов Predator (хищники) на карте.

    Attributes:
        _maps (Map): Объект карты, на которой происходят все действия.
        _percentage (float): Процентное соотношение хищников для размещения на карте.

    Methods:
        create_creature(coordinate):
            Создает объект Predator на заданных координатах.
    """

    def __init__(self, maps, percentage=0.01):
        """
        Инициализирует объект SpawnPredator с заданной картой и процентом размещения хищников.

        Args:
            maps (Map): Объект карты.
            percentage (float): Процентное соотношение хищников для размещения (по умолчанию 0.02).
        """
        super().__init__(maps, percentage)
        self._percentage = percentage

    def create_creature(self, coordinate):
        """
        Создает объект Predator на заданных координатах.

        Args:
            coordinate (Coordinates): Координаты для создания объекта Predator.

        Returns:
            Predator: Новый объект Predator на указанных координатах.
        """
        return Predator(coordinate)

