from entities.entity import Entity


class Tree(Entity):
    """ Статичный объект Дерево """
    def __init__(self, x, y):
        super().__init__(x, y)
