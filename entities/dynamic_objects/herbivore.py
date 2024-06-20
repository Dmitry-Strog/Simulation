from entities.dynamic_objects.creature import Creature


class Herbivore(Creature):
    """
    Класс Herbivore представляет травоядное существо, которое наследуется от Creature.
    Имеет предопределенные атрибуты для травоядных существ, такие как скорость, здоровье, атака и значения изменения здоровья.

    Attributes:
        coordinate (Coordinates): Координаты травоядного существа на карте.
        speed (int): Скорость травоядного существа, определяющая, сколько клеток оно может пройти за один ход.
        hp (int): Текущее количество здоровья травоядного существа.
        attack (int): Сила атаки травоядного существа.
        _max_hp (int): Максимальное количество здоровья у травоядного существа.
        _health_increase (int): Количество здоровья, которое восстанавливается при поедании пищи.
        _health_decrease (int): Количество здоровья, которое теряется при каждом ходе.
    """

    def __init__(self, coordinate, speed=1, hp=60, attack=20, health_increase=10, health_decrease=5):
        """
        Инициализация травоядного существа с заданными координатами, скоростью, здоровьем, атакой, увеличением и
        уменьшением здоровья.

        Args:
            coordinate (Coordinates): Координаты травоядного существа.
            speed (int, optional): Скорость травоядного существа. По умолчанию 1.
            hp (int, optional): Начальное количество здоровья. По умолчанию 60.
            attack (int, optional): Сила атаки. По умолчанию 20.
            health_increase (int, optional): Количество здоровья, которое восстанавливается при поедании пищи.
            По умолчанию 10.
            health_decrease (int, optional): Количество здоровья, которое теряется при каждом ходе. По умолчанию 5.
        """
        super().__init__(coordinate, speed, hp, attack, health_increase, health_decrease)
        self._max_hp = 60
        self._health_increase = health_increase
        self._health_decrease = health_decrease

    def __repr__(self):
        """
        Возвращает строковое представление травоядного существа.

        Returns:
            str: Строковое представление травоядного существа в виде эмодзи.
        """
        return "\U0001F410"

