#Задача 1 # -*- coding: utf-8 -*-
import random
M = int(input("Введите размер матрицы: "))
B = [[random.randint(-10, 10) for _ in range(M)] for _ in range(M)]
for row in B:
    for element in row:
        print(element, end=" ")
    print()
product = 1
for row in B:
    for element in row:
        if element > 0:
            product *= element
print("Произведение положительных элементов:", product)
#ЗАдача 2 
import random
M = int(input("Введите количество строк матрицы: "))
N = int(input("Введите количество столбцов матрицы: "))
B = [[random.randint(0, 100) for _ in range(N)] for _ in range(M)]
for row in B:
    for element in row:
        print(element, end=" ")
    print()
min_element = B[0][0]
min_element_row = 0
min_element_col = 0
for i in range(M):
    for j in range(N):
        if B[i][j] < min_element:
            min_element = B[i][j]
            min_element_row = i
            min_element_col = j
print("Минимальный элемент:", min_element)
print("Координаты минимального элемента:", (min_element_row, min_element_col))
#Задача 3
import random
M = int(input("Введите количество строк матрицы: "))
N = int(input("Введите количество столбцов матрицы: "))
D = [[random.randint(0, 100) for _ in range(N)] for _ in range(M)]
print("Исходная матрица:")
for row in D:
    for element in row:
        print(element, end=" ")
    print()
min_element = D[0][0]
min_element_row = 0
min_element_col = 0
max_element = D[0][0]
max_element_row = 0
max_element_col = 0
for i in range(M):
    for j in range(N):
        if D[i][j] < min_element:
            min_element = D[i][j]
            min_element_row = i
            min_element_col = j
        if D[i][j] > max_element:
            max_element = D[i][j]
            max_element_row = i
            max_element_col = j
D[min_element_row][min_element_col], D[max_element_row][max_element_col] = D[max_element_row][max_element_col], D[min_element_row][min_element_col]
print("Измененная матрица:")
for row in D:
    for element in row:
        print(element, end=" ")
    print()
    


