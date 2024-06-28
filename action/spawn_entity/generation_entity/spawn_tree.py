from action.spawn_entity.generation_entity.spawn_entity import SpawnEntity
from entities.static_objects.tree import Tree


class SpawnTree(SpawnEntity):
    """
    Класс SpawnTree отвечает за создание и размещение объектов Tree (деревья) на карте.

    Attributes:
        _maps (Map): Объект карты, на которой происходят все действия.
        _percentage (float): Процентное соотношение деревьев для размещения на карте.

    Methods:
        create_creature(coordinate):
            Создает объект Tree на заданных координатах.
    """

    def __init__(self, maps, percentage=0.1):
        """
        Инициализирует объект SpawnTree с заданной картой и процентом размещения деревьев.

        Args:
            maps (Map): Объект карты.
            percentage (float): Процентное соотношение деревьев для размещения (по умолчанию 0.1).
        """
        super().__init__(maps, percentage)
        self._percentage = percentage

    def create_creature(self, coordinate):
        """
        Создает объект Tree на заданных координатах.

        Args:
            coordinate (Coordinates): Координаты для создания объекта Tree.

        Returns:
            Tree: Новый объект Tree на указанных координатах.
        """
        return Tree(coordinate)

