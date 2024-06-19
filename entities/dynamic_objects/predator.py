from entities.dynamic_objects.creature import Creature


class Predator(Creature):
    """ Хищник, наследуется от Creature. В дополнение к полям класса Creature, имеет силу атаки.
    На что может потратить ход хищник:
    Переместиться (чтобы приблизиться к жертве - травоядному)
    Атаковать травоядное. При этом количество HP травоядного уменьшается на силу атаки хищника.
    Если значение HP жертвы опускается до 0, травоядное исчезает """

    def __init__(self, coordinate, speed=1, hp=100, attack=20, health_increase=20, health_decrease=10):
        super().__init__(coordinate, speed, hp, attack, health_increase, health_decrease)
        self._max_hp = 100
        self._health_increase = health_increase
        self._health_decrease = health_decrease

    def __repr__(self):
        return "\U0001F43A"
