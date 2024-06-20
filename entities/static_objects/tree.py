from entities.entity import Entity
from map.coordinate import Coordinates


class Tree(Entity):
    """
    Класс Tree представляет статичный объект "Дерево", который наследуется от Entity.

    Attributes:
        coordinate (Coordinates): Координаты дерева на карте.
    """

    def __init__(self, coordinate: Coordinates):
        """
        Инициализация объекта дерева с заданными координатами.

        Args:
            coordinate (Coordinates): Координаты дерева.
        """
        super().__init__(coordinate)

    def __repr__(self):
        """
        Возвращает строковое представление дерева.

        Returns:
            str: Строковое представление дерева в виде эмодзи.
        """
        return "\U0001F332"

