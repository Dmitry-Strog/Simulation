from action.spawn_entity.generation_entity.spawn_entity import SpawnEntity
from entities.dynamic_objects.herbivore import Herbivore


class SpawnHerbivore(SpawnEntity):
    def __init__(self, maps, percentage=0.03):
        super().__init__(maps, percentage)
        self._percentage = percentage

    def create_creature(self, coordinate):
        return Herbivore(coordinate)
