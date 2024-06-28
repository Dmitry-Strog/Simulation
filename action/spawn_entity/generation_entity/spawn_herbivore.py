from action.spawn_entity.generation_entity.spawn_entity import SpawnEntity
from entities.dynamic_objects.herbivore import Herbivore


class SpawnHerbivore(SpawnEntity):
    """
    Класс SpawnHerbivore отвечает за создание и размещение объектов Herbivore (травоядные) на карте.

    Attributes:
        _maps (Map): Объект карты, на которой происходят все действия.
        _percentage (float): Процентное соотношение травоядных для размещения на карте.

    Methods:
        create_creature(coordinate):
            Создает объект Herbivore на заданных координатах.
    """

    def __init__(self, maps, percentage=0.03):
        """
        Инициализирует объект SpawnHerbivore с заданной картой и процентом размещения травоядных.

        Args:
            maps (Map): Объект карты.
            percentage (float): Процентное соотношение травоядных для размещения (по умолчанию 0.03).
        """
        super().__init__(maps, percentage)
        self._percentage = percentage

    def create_creature(self, coordinate):
        """
        Создает объект Herbivore на заданных координатах.

        Args:
            coordinate (Coordinates): Координаты для создания объекта Herbivore.

        Returns:
            Herbivore: Новый объект Herbivore на указанных координатах.
        """
        return Herbivore(coordinate)

