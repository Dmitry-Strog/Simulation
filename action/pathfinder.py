from collections import deque
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator


class PathFinder:
    def __init__(self, maps):
        self.maps = maps
        self.save_path = [[None] * maps.width for _ in range(maps.height)]

    def find_path(self, creature):
        start_coor = (creature.coordinate.row, creature.coordinate.column)
        if isinstance(creature, Herbivore):
            grass_coords = self.maps.get_list_grass()
            nearest_grass = self.find_nearest_grass(start_coor, grass_coords)
            if nearest_grass:
                self.bfs(start_coor, (nearest_grass.coordinate.row, nearest_grass.coordinate.column))
                return self.get_path(nearest_grass.coordinate)
        # elif isinstance(creature, Predator):
        #     pass

        return []

    def find_nearest_grass(self, start, grass_coords):
        """Вычисляем манхэттенское расстояние от начальной координаты до координаты текущего объекта Grass"""
        min_distance = float('inf')
        nearest_grass = None
        for grass in grass_coords:
            distance = abs(grass.coordinate.row - start[0]) + abs(grass.coordinate.column - start[1])
            if distance < min_distance:
                min_distance = distance
                nearest_grass = grass
        return nearest_grass

    def bfs(self, start, end):
        next_node = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([start])
        visit = {start}

        while queue:
            cur_node = queue.popleft()

            if cur_node == end:
                break

            x, y = cur_node

            for dx, dy in next_node:
                nx, ny = dx + x, dy + y
                if 0 <= nx < self.maps.height and 0 <= ny < self.maps.width and (nx, ny) not in visit:
                    queue.append((nx, ny))
                    visit.add((nx, ny))
                    self.save_path[nx][ny] = (x, y)

    def get_path(self, end):
        """ Получить путь списком """
        curr = (end.row, end.column)
        path = []
        while curr is not None:
            path.append(curr)
            curr = self.save_path[curr[0]][curr[1]]
        path.reverse()
        return path
