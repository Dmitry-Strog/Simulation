from collections import Counter

from entities.static_objects.rock import Rock
from entities.static_objects.tree import Tree
from map.map import Map


class RenderInput:
    def __init__(self, maps: Map):
        self._maps = maps
        self._board = self._create_map()

    def display_map(self, move_counter: int):
        """Отображает карту в консоли"""
        self._update_map()
        self._print_line()
        for row in self._board:
            print('| ' + ' '.join(row) + ' |')
        self._print_line()
        self._print_progress(move_counter)
        self._print_line()
        print()

    def _print_line(self):
        line = '-' * 2
        print(line + self._maps.width * '---' + line)

    def _print_progress(self, move_counter):
        my_dict = self._count_dict()
        output = ' '.join([f'{key} {value}' for key, value in sorted(my_dict.items())])
        print('| ' + f'Шаг:{move_counter}        Существа {output}' + ' |')

    def _count_dict(self):
        count_entity = Counter()
        for entity in self._maps.get_all_entity():
            if not isinstance(entity, Rock) and not isinstance(entity, Tree):
                count_entity[entity.__str__()] += 1
        return count_entity

    def _create_map(self):
        """ Создание поле карты"""
        return [['\u29C8 '] * self._maps.width for _ in range(self._maps.height)]

    def _update_map(self):
        """Обновляет карту, размещая существа"""
        self._board = self._create_map()  # Очистить карту
        for creature in self._maps.get_all_entity():
            row, column = creature.coordinate.row, creature.coordinate.column
            self._board[row][column] = str(creature)
