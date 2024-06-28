from action.spawn_entity.generation_entity.spawn_entity import SpawnEntity
from entities.static_objects.grass import Grass


class SpawnGrass(SpawnEntity):
    """
    Класс SpawnGrass отвечает за создание и размещение объектов Grass (трава) на карте.

    Attributes:
        _maps (Map): Объект карты, на которой происходят все действия.
        _percentage (float): Процентное соотношение травы для размещения на карте.

    Methods:
        create_creature(coordinate):
            Создает объект Grass на заданных координатах.
    """

    def __init__(self, maps, percentage=0.08):
        """
        Инициализирует объект SpawnGrass с заданной картой и процентом размещения травы.

        Args:
            maps (Map): Объект карты.
            percentage (float): Процентное соотношение травы для размещения (по умолчанию 0.08).
        """
        super().__init__(maps, percentage)
        self._percentage = percentage

    def create_creature(self, coordinate):
        """
        Создает объект Grass на заданных координатах.

        Args:
            coordinate (Coordinates): Координаты для создания объекта Grass.

        Returns:
            Grass: Новый объект Grass на указанных координатах.
        """
        return Grass(coordinate)

