from map.map import Map


class RenderInput:
    def __init__(self, map: Map):
        self.map = map
        self.board = self.create_map()

    def display_map(self):
        """Отображает карту в консоли"""
        self.update_map()
        for row in self.board:
            print('  '.join(row))
        print()

    def create_map(self):
        """ Создание поле карты"""
        return [['\u29C8 '] * self.map.height for _ in range(self.map.width)]

    def update_map(self):
        """Обновляет карту, размещая существа"""
        self.board = self.create_map()  # Очистить карту
        for coordinates, creature in self.map.collection_entity.items():
            self.board[coordinates.row][coordinates.column] = str(creature)
