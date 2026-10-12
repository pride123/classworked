"""Матрицы: произведение положительных, поиск минимума, обмен минимума и максимума."""

import random


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{element:4}" for element in row))


# Задача 1. Произведение положительных элементов квадратной матрицы
m = int(input("Введите размер матрицы: "))
b = [[random.randint(-10, 10) for _ in range(m)] for _ in range(m)]
print_matrix(b)
product = 1
for row in b:
    for element in row:
        if element > 0:
            product *= element
print("Произведение положительных элементов:", product)

# Задача 2. Минимальный элемент и его координаты
m = int(input("Введите количество строк матрицы: "))
n = int(input("Введите количество столбцов матрицы: "))
b = [[random.randint(0, 100) for _ in range(n)] for _ in range(m)]
print_matrix(b)
min_row, min_col = 0, 0
for i in range(m):
    for j in range(n):
        if b[i][j] < b[min_row][min_col]:
            min_row, min_col = i, j
print("Минимальный элемент:", b[min_row][min_col])
print("Координаты (строка, столбец):", (min_row, min_col))

# Задача 3. Поменять местами минимальный и максимальный элементы
m = int(input("Введите количество строк матрицы: "))
n = int(input("Введите количество столбцов матрицы: "))
d = [[random.randint(0, 100) for _ in range(n)] for _ in range(m)]
print("Исходная матрица:")
print_matrix(d)
min_pos = (0, 0)
max_pos = (0, 0)
for i in range(m):
    for j in range(n):
        if d[i][j] < d[min_pos[0]][min_pos[1]]:
            min_pos = (i, j)
        if d[i][j] > d[max_pos[0]][max_pos[1]]:
            max_pos = (i, j)
(r1, c1), (r2, c2) = min_pos, max_pos
d[r1][c1], d[r2][c2] = d[r2][c2], d[r1][c1]
print("Изменённая матрица:")
print_matrix(d)
