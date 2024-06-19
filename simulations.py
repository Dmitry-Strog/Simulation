import os
from time import sleep

from action.actions import Actions
from entities.dynamic_objects.herbivore import Herbivore
from entities.dynamic_objects.predator import Predator
from entities.static_objects.grass import Grass
from entities.static_objects.rock import Rock
from entities.static_objects.tree import Tree
from map.map import Map
from map.render_Input import RenderInput


class Simulation:
    def __init__(self, map_population):
        self.maps = Map(12, 12)
        self.move_counter = 0
        self.render = RenderInput(self.maps)
        self.action = Actions(self.maps, map_population)
        self.action.init_actions()

    def next_turn(self):
        """Про симулировать и отрендерить один ход"""
        self.render.display_map(self.move_counter)
        self.action.turn_actions()
        self.move_counter += 1
        sleep(1)
        os.system('clear')

    def start_simulation(self):
        """Запустить бесконечный цикл симуляции и рендеринга"""
        count = 0
        while True:
            if not self.maps.get_list_herbivore():
                self.render.display_map(self.move_counter)
                print("На карте не осталось травоядных!")
                break
            elif not self.maps.get_list_predators():
                self.render.display_map(self.move_counter)
                print("Хищники умерли с голоду!")
                break
            if count == 10:
                self.pause_simulation()
                count = 0
            self.next_turn()
            self.action.check_and_add_grass()
            count += 1

    @staticmethod
    def pause_simulation():
        """Приостановить бесконечный цикл симуляции и рендеринга"""
        if not int(input("Нажмите '1' что бы продолжить '0' что бы выйти \n")):
            print("Вы вышли из игры!")
            exit()


if __name__ == '__main__':
    map_populations = {
        Herbivore: 6,
        Predator: 2,
        Grass: 10,
        Rock: 12,
        Tree: 14,
    }
    game = Simulation(map_populations)
    game.start_simulation()
