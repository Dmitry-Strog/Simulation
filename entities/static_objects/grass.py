from entities.entity import Entity
from map.coordinate import Coordinates


class Grass(Entity):
    """ Статичный объект Трава """

    def __init__(self, coordinate: Coordinates, hp=40):
        super().__init__(coordinate)
        self.hp = hp

    def __repr__(self):
        return "\U0001F331"