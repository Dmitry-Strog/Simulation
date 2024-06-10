from entities.entity import Entity
from map.coordinate import Coordinates


class Rock(Entity):
    """ Статичный объект Камень """

    def __init__(self, coordinate: Coordinates):
        super().__init__(coordinate)

    def __repr__(self):
        return "R"
