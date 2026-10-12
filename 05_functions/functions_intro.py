"""Знакомство с функциями: def, параметры, return."""


def difference(a, b):
    """Возвращает разность большего и меньшего числа (всегда неотрицательную)."""
    return abs(a - b)


for _ in range(3):
    first = float(input("Введите первое число: "))
    second = float(input("Введите второе число: "))
    print("Разность:", difference(first, second))
