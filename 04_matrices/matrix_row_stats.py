"""Статистика по строкам матрицы: суммы, количество ненулевых, минимумы."""

import random


def create_matrix(rows, cols, low=0, high=9):
    return [[random.randint(low, high) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    print("Матрица A:")
    for row in matrix:
        print(row)


def count_nonzero(row):
    return sum(1 for element in row if element != 0)


# Задача 1. Сумма положительных элементов каждой строки матрицы 7x4
a = create_matrix(7, 4, -100, 100)
print_matrix(a)
print("Суммы положительных элементов каждой строки:")
print([sum(x for x in row if x > 0) for row in a])

# Задача 2. Количество ненулевых элементов в каждой строке квадратной матрицы
a = create_matrix(5, 5)
print_matrix(a)
print("Количество ненулевых элементов в каждой строке:")
print([count_nonzero(row) for row in a])

# Задача 3. Минимальный элемент каждой строки
a = create_matrix(5, 4)
print_matrix(a)
print("Минимальные элементы в каждой строке:")
print([min(row) for row in a])

# Задача 4. Количество ненулевых элементов в каждой строке матрицы 5x4
a = create_matrix(5, 4)
print_matrix(a)
print("Количество ненулевых элементов в каждой строке:")
print([count_nonzero(row) for row in a])
