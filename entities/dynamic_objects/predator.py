from entities.dynamic_objects.creature import Creature


class Predator(Creature):
    """ Хищник, наследуется от Creature. В дополнение к полям класса Creature, имеет силу атаки.
    На что может потратить ход хищник:
    Переместиться (чтобы приблизиться к жертве - травоядному)
    Атаковать травоядное. При этом количество HP травоядного уменьшается на силу атаки хищника.
    Если значение HP жертвы опускается до 0, травоядное исчезает """
    def __init__(self, x, y, speed, hp):
        super().__init__(x, y, speed, hp)

    def make_move(self):
        pass