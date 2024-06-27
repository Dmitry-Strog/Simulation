import os
from time import sleep

from action.actions import Actions
from action.spawn_entity.generation_entity.spawn_grass import SpawnGrass
from action.spawn_entity.generation_entity.spawn_herbivore import SpawnHerbivore
from action.spawn_entity.generation_entity.spawn_predator import SpawnPredator
from action.spawn_entity.generation_entity.spawn_rock import SpawnRock
from action.spawn_entity.generation_entity.spawn_tree import SpawnTree
from map.map import Map
from map.render_Input import RenderInput


class Simulation:
    """
    Класс Simulation управляет основной логикой симуляции экосистемы.

    Attributes:
        maps (Map): Объект карты, представляющий текущее состояние мира.
        move_counter (int): Счетчик текущего хода симуляции.
        render (RenderInput): Объект для отображения текущего состояния карты в консоли.
        action (Actions): Объект для выполнения действий с существами и объектами на карте.

    Methods:
        next_turn():
            Производит один ход симуляции, отображая текущее состояние карты и обновляя состояние всех существ.

        start_simulation():
            Запускает бесконечный цикл симуляции и отображения состояния карты, пока на карте есть травоядные и хищники.

        pause_simulation():
            Приостанавливает бесконечный цикл симуляции и предлагает пользователю выбрать продолжить или выйти из игры.
    """

    def __init__(self):
        """
        Инициализация объекта Simulation.

        Args:
            map_population (dict): Словарь, определяющий начальное распределение существ и объектов на карте.
        """
        self.maps = Map(14, 18)  # Создаем карту размером 12x12
        self.move_counter = 0  # Счетчик текущего хода
        self.render = RenderInput(self.maps)  # Объект для отображения состояния карты
        self.action = Actions(self.maps)  # Объект для выполнения действий с существами и объектами
        self.map_populations = (
            SpawnHerbivore(self.maps),
            SpawnPredator(self.maps),
            SpawnGrass(self.maps),
            SpawnRock(self.maps),
            SpawnTree(self.maps),
        )
        self.action.init_actions(self.map_populations)  # Размещаем начальные существа и объекты на карте

    def next_turn(self):
        """
        Производит один ход симуляции.

        Отображает текущее состояние карты, выполняет ход всех существ и объектов,
        обновляет состояние карты после каждого хода.
        """
        self.render.display_map()  # Отображаем текущее состояние карты
        self.action.turn_actions()  # Выполняем ход всех существ и объектов на карте
        self.move_counter += 1  # Увеличиваем счетчик ходов
        self.render.update_move_counter(self.move_counter)  # Обновляем счетчик ходов в RenderInput
        sleep(1)  # Задержка для визуализации
        os.system('clear')  # Очищаем консоль перед следующим отображением

    def start_simulation(self):
        """
        Запускает бесконечный цикл симуляции и отображения состояния карты.

        Продолжает выполнение симуляции, пока на карте есть травоядные и хищники.
        """
        count = 0
        while True:
            # Проверяем условия завершения симуляции
            if not self.maps.get_list_herbivore():
                self.render.display_map()
                print("На карте не осталось травоядных!")
                break
            elif not self.maps.get_list_predators():
                self.render.display_map()
                print("Хищники умерли с голоду!")
                break
            # Приостанавливаем симуляцию каждые 15 ходов для возможности вмешательства
            if count == 15:
                self.pause_simulation()
                count = 0
            self.next_turn()  # Выполняем следующий ход симуляции
            self.action.check_and_add_grass(self.map_populations)  # Проверяем и добавляем траву на карту
            count += 1

    @staticmethod
    def pause_simulation():
        """
        Приостанавливает бесконечный цикл симуляции и предлагает пользователю выбрать продолжить или выйти из игры.
        """
        if not int(input("Нажмите '1' чтобы продолжить, '0' чтобы выйти \n")):
            print("Вы вышли из игры!")
            exit()


if __name__ == '__main__':
    # Создаем объект симуляции и запускаем симуляцию
    game = Simulation()
    game.start_simulation()
