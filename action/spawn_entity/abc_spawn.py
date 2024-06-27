import random
from abc import abstractmethod

from action.actions import Actions


class AbcSpawn(Actions):

    def __init__(self, maps):
        super().__init__(maps)

    @abstractmethod
    def perform(self):
        """ Метод для вызова у объекта spawn на карте"""
        raise NotImplementedError
