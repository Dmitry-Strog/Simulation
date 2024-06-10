from entities.entity import Entity
from map.coordinate import Coordinates


class Tree(Entity):
    """ Статичный объект Дерево """

    def __init__(self, coordinate: Coordinates):
        super().__init__(coordinate)

    def __repr__(self):
        return "T"
