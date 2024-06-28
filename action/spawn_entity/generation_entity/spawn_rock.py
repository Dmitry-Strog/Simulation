from action.spawn_entity.generation_entity.spawn_entity import SpawnEntity
from entities.static_objects.rock import Rock


class SpawnRock(SpawnEntity):
    """
    Класс SpawnRock отвечает за создание и размещение объектов Rock (камни) на карте.

    Attributes:
        _maps (Map): Объект карты, на которой происходят все действия.
        _percentage (float): Процентное соотношение камней для размещения на карте.

    Methods:
        create_creature(coordinate):
            Создает объект Rock на заданных координатах.
    """

    def __init__(self, maps, percentage=0.1):
        """
        Инициализирует объект SpawnRock с заданной картой и процентом размещения камней.

        Args:
            maps (Map): Объект карты.
            percentage (float): Процентное соотношение камней для размещения (по умолчанию 0.1).
        """
        super().__init__(maps, percentage)
        self._percentage = percentage

    def create_creature(self, coordinate):
        """
        Создает объект Rock на заданных координатах.

        Args:
            coordinate (Coordinates): Координаты для создания объекта Rock.

        Returns:
            Rock: Новый объект Rock на указанных координатах.
        """
        return Rock(coordinate)

