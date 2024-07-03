from entities.dynamic_objects.creature import Creature


class Predator(Creature):
    """
    Класс Predator представляет хищное существо, которое наследуется от Creature. Имеет предопределенные атрибуты для
    хищных существ, такие как скорость, здоровье, атака и значения изменения здоровья.

    Attributes:
        coordinate (Coordinates): Координаты хищного существа на карте.
        speed (int): Скорость хищного существа, определяющая, сколько клеток оно может пройти за один ход.
        hp (int): Текущее количество здоровья хищного существа.
        attack (int): Сила атаки хищного существа.
        _max_hp (int): Максимальное количество здоровья у хищного существа.
        _health_increase (int): Количество здоровья, которое восстанавливается при поедании пищи.
        _health_decrease (int): Количество здоровья, которое теряется при каждом ходе.
    """

    def __init__(self, coordinate, speed=1, hp=100, attack=20, health_increase=20, health_decrease=5):
        """
        Инициализация хищного существа с заданными координатами, скоростью, здоровьем, атакой, увеличением и
        уменьшением здоровья.

        Args:
            coordinate (Coordinates): Координаты хищного существа.
            speed (int, optional): Скорость хищного существа. По умолчанию 1.
            hp (int, optional): Начальное количество здоровья. По умолчанию 100.
            attack (int, optional): Сила атаки. По умолчанию 20.
            health_increase (int, optional): Количество здоровья, которое восстанавливается при поедании пищи.
            По умолчанию 20.
            health_decrease (int, optional): Количество здоровья, которое теряется при каждом ходе. По умолчанию 5.
        """
        super().__init__(coordinate, speed, hp, attack, health_increase, health_decrease)
        self._max_hp = 100
        self._health_increase = health_increase
        self._health_decrease = health_decrease

    def __repr__(self):
        """
        Возвращает строковое представление хищного существа.

        Returns:
            str: Строковое представление хищного существа в виде эмодзи.
        """
        return "\U0001F43A"
