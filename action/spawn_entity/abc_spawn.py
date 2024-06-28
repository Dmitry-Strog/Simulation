from abc import ABC, abstractmethod

from action.actions import Actions


class AbcSpawn(Actions, ABC):
    """
    Абстрактный класс AbcSpawn, наследующий от класса Actions и реализующий интерфейс для размещения сущностей на карте.

    Attributes:
        _maps (Map): Объект карты, на которой происходят все действия.
    """

    def __init__(self, maps):
        """
        Инициализирует объект AbcSpawn с заданной картой.

        Args:
            maps (Map): Объект карты.
        """
        super().__init__(maps)

    @abstractmethod
    def perform(self):
        """
        Абстрактный метод для размещения сущности на карте.

        Должен быть реализован в подклассах для конкретных типов сущностей.
        """
        raise NotImplementedError
