"""Массивы и матрицы: уникальные элементы, подсчёты, произведения, минимум."""

import random


def random_matrix(rows, cols, low, high):
    return [[random.randint(low, high) for _ in range(cols)] for _ in range(rows)]


def print_matrix(name, matrix):
    print(f"Матрица {name}:")
    for row in matrix:
        print(row)


# Задача 1. Уникальные элементы двух массивов
array1 = [random.randint(1, 50) for _ in range(17)]
array2 = [random.randint(1, 50) for _ in range(25)]
array3 = []
for num in array1 + array2:
    if num not in array3:
        array3.append(num)
print("Первый массив:", array1)
print("Второй массив:", array2)
print("Уникальные элементы:", array3)

# Задача 2. Количество ненулевых элементов
m = int(input("Введите размерность матрицы M: "))
matrix_b = random_matrix(m, m, 0, 9)
print_matrix("B", matrix_b)
non_zero_count = sum(1 for row in matrix_b for elem in row if elem != 0)
print("Количество ненулевых элементов:", non_zero_count)

# Задача 3. Произведение отрицательных элементов
matrix_d = random_matrix(3, 3, -10, 10)
print_matrix("D", matrix_d)
negatives = [elem for row in matrix_d for elem in row if elem < 0]
if negatives:
    product = 1
    for elem in negatives:
        product *= elem
    print("Произведение отрицательных элементов:", product)
else:
    print("В матрице нет отрицательных элементов.")

# Задача 4. Произведение положительных элементов
m = int(input("Введите размер M для матрицы B[M,M]: "))
matrix_b = random_matrix(m, m, -10, 10)
print_matrix("B", matrix_b)
positives = [elem for row in matrix_b for elem in row if elem > 0]
if positives:
    product = 1
    for elem in positives:
        product *= elem
    print("Произведение положительных элементов:", product)
else:
    print("В матрице нет положительных элементов.")

# Задача 5. Минимальный элемент и его координаты
m = int(input("Введите размер M для матрицы B[M,M]: "))
matrix_b = random_matrix(m, m, -10, 10)
print_matrix("B", matrix_b)
min_row, min_col = 0, 0
for i in range(m):
    for j in range(m):
        if matrix_b[i][j] < matrix_b[min_row][min_col]:
            min_row, min_col = i, j
print("Минимальный элемент:", matrix_b[min_row][min_col])
print("Его координаты (строка, столбец):", min_row, ",", min_col)
