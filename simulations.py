from time import sleep

from action.actions import Actions
from entities.dynamic_objects.herbivore import Herbivore
from entities.static_objects.grass import Grass

if __name__ == '__main__':
    map_population = {
        Herbivore: 2,
        Grass: 15,
    }
    game = Actions()
    game.init_actions(map_population)
    game.turn_actions()
