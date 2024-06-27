from action.spawn_entity.generation_entity.spawn_entity import SpawnEntity
from entities.dynamic_objects.predator import Predator


class SpawnPredator(SpawnEntity):
    def __init__(self, maps, percentage=0.02):
        super().__init__(maps, percentage)
        self._percentage = percentage

    def create_creature(self, coordinate):
        return Predator(coordinate)
