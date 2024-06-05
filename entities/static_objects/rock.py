from entities.entity import Entity


class Rock(Entity):
    """ Статичный объект Камень """
    def __init__(self, x, y):
        super().__init__(x, y)