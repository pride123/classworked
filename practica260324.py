#coding utf 8 
# Задача 1 
import random

array1 = [random.randint(1, 50) for _ in range(17)]
array2 = [random.randint(1, 50) for _ in range(25)]
array3 = []

for num in array1 + array2:
    if num not in array3:
        array3.append(num)

print("Первый массив:", array1)
print("Второй массив:", array2)
print("Третий массив с уникальными элементами:", array3)
#Задача 2 
import random

M = int(input("Введите размерность матрицы M: "))

matrix_B = []
for i in range(M):
    row = []
    for j in range(M):
        row.append(random.randint(0, 9))
    matrix_B.append(row)

print("Матрица B:")
for row in matrix_B:
    print(row)

non_zero_count = 0
for row in matrix_B:
    for elem in row:
        if elem != 0:
            non_zero_count += 1

print(f"Количество ненулевых элементов в матрице B: {non_zero_count}")


#Задача 3 
import random

M = 3  
D = [[random.randint(-10, 10) for _ in range(M)] for _ in range(M)]
print("Матрица D:")
for row in D:
    print(row)

negative_product = 1
for row in D:
    for elem in row:
        if elem < 0:
            negative_product *= elem

if negative_product == 1:
    print("В матрице нет отрицательных элементов.")
else:
    print("Произведение отрицательных элементов: ", negative_product)
#Задача 4 
import random

M = int(input("Введите размер M для матрицы B[M,M]: "))
B = []
positive_product = 1

for i in range(M):
    row = [random.randint(-10, 10) for _ in range(M)] 
    B.append(row)

print("Матрица B:")
for row in B:
    print(row)

for row in B:
    for element in row:
        if element > 0:
            positive_product *= element

if positive_product == 1:
    print("В матрице нет положительных элементов.")
else:
    print("Произведение положительных элементов:", positive_product)

#Задача 5 

import random

M = int(input("Введите размер M для матрицы B[M,M]: "))
B = []
min_element = float('inf')
min_row = 0
min_col = 0

for i in range(M):
    row = [random.randint(-10, 10) for _ in range(M)]  
    B.append(row)

print("Матрица B:")
for row in B:
    print(row)

for i in range(M):
    for j in range(M):
        if B[i][j] < min_element:
            min_element = B[i][j]
            min_row = i
            min_col = j

print("Минимальный элемент:", min_element)
print("Его координаты (строка, столбец):", min_row, ",", min_col)
