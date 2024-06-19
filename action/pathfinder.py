from collections import deque
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator


class PathFinder:
    def __init__(self, maps):
        self._maps = maps
        self._save_path = [[None] * maps.width for _ in range(maps.height)]

    def find_path(self, creature):
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
        """Вычисляем манхэттенское расстояние от начальной координаты до координаты текущего объекта Grass"""
        min_distance = float('inf')
        nearest_target = None
        for target in targets:
            distance = abs(target.coordinate.row - start[0]) + abs(target.coordinate.column - start[1])
            if distance < min_distance:
                min_distance = distance
                nearest_target = target
        return nearest_target

    def _bfs(self, start, end):
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
        """ Получить путь списком """
        curr = (end.row, end.column)
        path = []
        while curr is not None:
            path.append(curr)
            curr = self._save_path[curr[0]][curr[1]]
        path.reverse()
        return path
