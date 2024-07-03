from collections import Counter
from map.map import Map
from entities.static_objects.rock import Rock
from entities.static_objects.tree import Tree


class RenderInput:
    """
    Класс RenderInput отвечает за отображение текущего состояния карты в консоли.

    Attributes:
        maps (Map): Объект карты, содержащий информацию о расположении существ.
    """

    def __init__(self, maps: Map):
        """
        Инициализация объекта RenderInput.

        Args:
            maps (Map): Объект карты, содержащий информацию о расположении существ.
        """
        self._maps = maps
        self._board = self._create_map()
        self.move_counter = 0

    def display_map(self):
        """
        Отображает текущее состояние карты в консоли.
        """
        self._update_map()
        self._print_line()
        for row in self._board:
            print('| ' + ' '.join(row) + ' |')
        self._print_line()
        self._print_progress()
        self._print_line()
        print()

    def _print_line(self):
        """
        Выводит горизонтальную линию для отделения строк в консоли.
        """
        line = '-' * 2
        print(line + self._maps.width * '---' + line)

    def _print_progress(self):
        """
        Выводит информацию о текущем ходе и количестве каждого вида существ на карте.
        """
        my_dict = self._count_dict()
        output = ' '.join([f'{key} {value}' for key, value in sorted(my_dict.items())])

        if len(my_dict) == 2:
            output += "   "
        value = (self._maps.width - 8) * "   "
        print('| ' + f'Шаг:{self.move_counter} {value} {output}' + ' |')

    def _count_dict(self):
        """
        Подсчитывает количество каждого вида существ на карте.

        Returns:
            Counter: Словарь с количеством каждого вида существ.
        """
        count_entity = Counter()
        for entity in self._maps.get_all_entity():
            if not isinstance(entity, Rock) and not isinstance(entity, Tree):
                count_entity[entity.__str__()] += 1
        return count_entity

    def _create_map(self):
        """
        Создает пустую карту для отображения в консоли.

        Returns:
            list: Двумерный список, представляющий пустую карту.
        """
        return [['\u29C8 '] * self._maps.width for _ in range(self._maps.height)]

    def _update_map(self):
        """
        Обновляет карту, добавляя на нее существа.
        """
        self._board = self._create_map()
        for creature in self._maps.get_all_entity():
            row, column = creature.coordinate.row, creature.coordinate.column
            self._board[row][column] = str(creature)

    def update_move_counter(self, move_counter: int):
        """
        Обновляет значение счетчика ходов.

        Args:
            move_counter (int): Новое значение счетчика ходов.
        """
        self.move_counter = move_counter
