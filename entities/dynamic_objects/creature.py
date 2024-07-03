from entities.entity import Entity
from map.coordinate import Coordinates


class Creature(Entity):
    """
    Класс Creature представляет существо в мире. Существо имеет скорость, здоровье (HP), атаку, а также параметры
    увеличения и уменьшения здоровья.

    Attributes:
        coordinate (Coordinates): Координаты существа на карте.
        speed (int): Скорость существа, определяющая, сколько клеток оно может пройти за один ход.
        hp (int): Текущее количество здоровья существа.
        _attack (int): Сила атаки существа.
        _max_hp (int): Максимальное количество здоровья у существа.
        _health_increase (int): Количество здоровья, которое восстанавливается при поедании пищи.
        _health_decrease (int): Количество здоровья, которое теряется при каждом ходе.
    """

    def __init__(self, coordinate: Coordinates, speed, hp, attack, health_increase, health_decrease):
        """
        Инициализация существа с заданными координатами, скоростью, здоровьем, атакой, увеличением и уменьшением здоровья.

        Args:
            coordinate (Coordinates): Координаты существа.
            speed (int): Скорость существа.
            hp (int): Начальное количество здоровья.
            attack (int): Сила атаки.
            health_increase (int): Количество здоровья, которое восстанавливается при поедании пищи.
            health_decrease (int): Количество здоровья, которое теряется при каждом ходе.
        """
        super().__init__(coordinate)
        self.speed = speed
        self.hp = hp
        self._attack = attack
        self._max_hp = hp
        self._health_increase = health_increase
        self._health_decrease = health_decrease

    def make_move(self, world_map, path):
        """
        Выполняет ход существа по заданному пути.

        Args:
            world_map (Map): Карта мира, на которой происходит перемещение.
            path (list): Путь, по которому должно двигаться существо.
        """
        if not path:
            print(self, "Не найден путь")
            return

        if self.hp <= 0:
            world_map.remove_entity((self.coordinate.row, self.coordinate.column))
            return

        if self.speed + 1 >= len(path):
            self.eat(world_map, path)
        else:
            next_position = path[self.speed]
            world_map.place_entity(Coordinates(next_position[0], next_position[1]), self)
            world_map.remove_entity(path[0])
            self.decrease_health()
            self.is_alive_creature(world_map, (self.coordinate.row, self.coordinate.column))

    def eat(self, world_map, path):
        """
        Метод атаки существа. Существо атакует цель на конечной позиции пути.

        Args:
            world_map (Map): Карта мира, на которой происходит атака.
            path (list): Путь, по которому существо двигалось для атаки.
        """
        target = path[-1]
        obj = world_map.get_entity(target)
        obj.hp -= self._attack
        if obj.hp <= 0:
            world_map.remove_entity(target)
            self.add_health()
            print(f"{self}({self.hp}) Съел {obj}")

    def is_alive_creature(self, world_map, coor: tuple):
        """
        Проверяет, живо ли существо, и удаляет его, если оно мертво.

        Args:
            world_map (Map): Карта мира, на которой происходит проверка.
            coor (tuple): Координаты существа.
        """
        if self.hp <= 0:
            print(self, 'Умер с голоду')
            world_map.remove_entity(coor)

    def check_max_hp(self):
        """
        Проверка, чтобы hp существа не превышало максимальное значение.
        """
        if self.hp > self._max_hp:
            self.hp = self._max_hp

    def add_health(self):
        """
        Увеличивает здоровье существа на значение health_increase и проверяет, чтобы оно не превышало максимальное
        значение.
        """
        self.hp += self._health_increase
        self.check_max_hp()

    def decrease_health(self):
        """
        Уменьшает здоровье существа на значение health_decrease.
        """
        self.hp -= self._health_decrease

