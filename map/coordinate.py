class Coordinates:
    """
    Класс Coordinates представляет координаты на двумерной карте.

    Attributes:
        row (int): Строчная координата.
        column (int): Колоночная координата.
    """

    def __init__(self, row: int, column: int):
        """
        Инициализация объекта координат с заданными строковой и колоночной координатами.

        Args:
            row (int): Строчная координата.
            column (int): Колоночная координата.
        """
        self.row = row
        self.column = column

    def __eq__(self, other):
        """
        Проверяет эквивалентность текущих координат с другими координатами.

        Args:
            other (Coordinates): Другие координаты для сравнения.

        Returns:
            bool: True, если координаты эквивалентны, иначе False.
        """
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        """
        Возвращает хэш-код объекта, необходим для использования координат в качестве ключей словаря.

        Returns:
            int: Хэш-код текущих координат.
        """
        return hash((self.row, self.column))

    def __str__(self):
        """
        Возвращает строковое представление текущих координат в формате (row, column).

        Returns:
            str: Строковое представление текущих координат.
        """
        return f"({self.row}, {self.column})"

