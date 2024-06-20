from map.coordinate import Coordinates


class Entity:
    """Корневой абстрактный класс для всех существ и объектов существующих в симуляции."""

    def __init__(self, coordinate: Coordinates):
        self.coordinate = coordinate

