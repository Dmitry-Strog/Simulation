from collections import Counter

from entities.dynamic_objects.herbivore import Herbivore
from entities.static_objects.rock import Rock
from entities.static_objects.tree import Tree
from map.map import Map


class RenderInput:
    def __init__(self, map: Map):
        self.map = map
        self.board = self.create_map()

    def display_map(self, move_counter, len_creature):
        """Отображает карту в консоли"""
        self.update_map()
        self.print_line()
        for row in self.board:
            print('| ' + ' '.join(row) + ' |')
        self.print_line()
        self.print_progress(move_counter, len_creature)
        self.print_line()
        print()

    def print_line(self):
        line = '-' * 3
        print(line + self.map.width * '---' + line)

    def print_progress(self, move_counter, len_creature):
        my_dict = self.count_dict()
        output = ' '.join([f'{key} {value}' for key, value in sorted(my_dict.items())])
        print('| ' + f'Шаг:{move_counter}        Существа {output}' + ' |')

    def count_dict(self):
        count_entity = Counter()
        for entity in self.map.collection_entity.values():
            if not isinstance(entity, Rock) and not isinstance(entity, Tree):
                count_entity[entity.__str__()] += 1
        return count_entity

    def create_map(self):
        """ Создание поле карты"""
        return [['\u29C8 '] * self.map.height for _ in range(self.map.width)]

    def update_map(self):
        """Обновляет карту, размещая существа"""
        self.board = self.create_map()  # Очистить карту
        for coordinates, creature in self.map.collection_entity.items():
            self.board[coordinates.row][coordinates.column] = str(creature)
