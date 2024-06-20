from collections import deque
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator


class PathFinder:
    """
    Класс PathFinder отвечает за поиск путей для существ на карте.

    Attributes:
        _maps (Map): Объект карты, на которой происходят все действия.
        _save_path (list): Двумерный список для сохранения путей.
    """

    def __init__(self, maps):
        """
        Инициализирует объект PathFinder с заданной картой.

        Args:
            maps (Map): Объект карты.
        """
        self._maps = maps
        self._save_path = [[None] * maps.width for _ in range(maps.height)]

    def find_path(self, creature):
        """
        Находит путь для существа на карте. Если существо - травоядное, ищет ближайшую траву.
        Если существо - хищник, ищет ближайшего травоядного.

        Args:
            creature (Creature): Существо, для которого необходимо найти путь.

        Returns:
            list: Список координат, представляющих путь.
        """
        start_coord = (creature.coordinate.row, creature.coordinate.column)
        if isinstance(creature, Herbivore):
            grass_coord = self._maps.get_list_grass()
            nearest_grass = self._find_nearest_grass(start_coord, grass_coord)
            if nearest_grass:
                self._bfs(start_coord, (nearest_grass.coordinate.row, nearest_grass.coordinate.column))
                return self._get_path(nearest_grass.coordinate)
        elif isinstance(creature, Predator):
            herbivore_coord = self._maps.get_list_herbivore()
            nearest_herbivore = self._find_nearest_grass(start_coord, herbivore_coord)
            if nearest_herbivore:
                self._bfs(start_coord, (nearest_herbivore.coordinate.row, nearest_herbivore.coordinate.column))
                return self._get_path(nearest_herbivore.coordinate)

        return []

    def _find_nearest_grass(self, start, targets):
        """
        Находит ближайший объект из списка целей (например, траву или травоядное) с использованием Манхеттенского
        расстояния.

        Args:
            start (tuple): Начальная координата.
            targets (list): Список объектов с координатами.

        Returns:
            object: Ближайший объект из списка целей.
        """
        min_distance = float('inf')
        nearest_target = None
        for target in targets:
            distance = abs(target.coordinate.row - start[0]) + abs(target.coordinate.column - start[1])
            if distance < min_distance:
                min_distance = distance
                nearest_target = target
        return nearest_target

    def _bfs(self, start, end):
        """
        Алгоритм поиска в ширину (BFS) для нахождения пути от начальной координаты до конечной.

        Args:
            start (tuple): Начальная координата.
            end (tuple): Конечная координата.
        """
        next_node = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque([start])
        visit = {start}

        while queue:
            cur_node = queue.popleft()
            if cur_node == end:
                break

            x, y = cur_node
            desired_entity = self._maps.get_entity(end)
            for dx, dy in next_node:
                nx, ny = dx + x, dy + y

                if 0 <= nx < self._maps.height and 0 <= ny < self._maps.width and (nx, ny) not in visit:
                    checking_entity = self._maps.get_entity((nx, ny))
                    if checking_entity is None or isinstance(checking_entity, type(desired_entity)):
                        queue.append((nx, ny))
                        visit.add((nx, ny))
                        self._save_path[nx][ny] = (x, y)

    def _get_path(self, end):
        """
        Восстанавливает путь от конечной координаты до начальной.

        Args:
            end (Coordinates): Конечная координата.

        Returns:
            list: Список координат, представляющих путь.
        """
        curr = (end.row, end.column)
        path = []
        while curr is not None:
            path.append(curr)
            curr = self._save_path[curr[0]][curr[1]]
        path.reverse()
        return path

