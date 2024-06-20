from entities.entity import Entity
from map.coordinate import Coordinates


class Grass(Entity):
    """
    Класс Grass представляет статичный объект "Трава", который наследуется от Entity.

    Attributes:
        coordinate (Coordinates): Координаты травы на карте.
        hp (int): Количество здоровья травы.
    """

    def __init__(self, coordinate: Coordinates, hp=40):
        """
        Инициализация объекта травы с заданными координатами и количеством здоровья.

        Args:
            coordinate (Coordinates): Координаты травы.
            hp (int, optional): Начальное количество здоровья травы. По умолчанию 40.
        """
        super().__init__(coordinate)
        self.hp = hp

    def __repr__(self):
        """
        Возвращает строковое представление травы.

        Returns:
            str: Строковое представление травы в виде эмодзи.
        """
        return "\U0001F331"

