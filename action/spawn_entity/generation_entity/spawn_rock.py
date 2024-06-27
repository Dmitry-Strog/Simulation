from action.spawn_entity.generation_entity.spawn_entity import SpawnEntity
from entities.static_objects.rock import Rock


class SpawnRock(SpawnEntity):
    def __init__(self, maps, percentage=0.1):
        super().__init__(maps, percentage)
        self._percentage = percentage

    def create_creature(self, coordinate):
        return Rock(coordinate)
