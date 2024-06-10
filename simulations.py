from action.actions import Actions
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator
from entities.static_objects.grass import Grass
from entities.static_objects.rock import Rock
from entities.static_objects.tree import Tree

if __name__ == '__main__':
    map_population = {
        Herbivore: 4,
        Predator: 2,
        Grass: 8,
        Rock: 10,
        Tree: 10,
    }
    game = Actions()
    game.init_actions(map_population)
    game.turn_actions()
