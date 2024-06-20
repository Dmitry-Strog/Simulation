from entities.entity import Entity
from map.coordinate import Coordinates


class Rock(Entity):
    """
    Класс Rock представляет статичный объект "Камень", который наследуется от Entity.

    Attributes:
        coordinate (Coordinates): Координаты камня на карте.
    """

    def __init__(self, coordinate: Coordinates):
        """
        Инициализация объекта камня с заданными координатами.

        Args:
            coordinate (Coordinates): Координаты камня.
        """
        super().__init__(coordinate)

    def __repr__(self):
        """
        Возвращает строковое представление камня.

        Returns:
            str: Строковое представление камня в виде эмодзи.
        """
        return "\U0001FAA8"
