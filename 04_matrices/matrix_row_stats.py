#UTF-8
#Задача 1 
def lol():
    import random
    A = [[random.randint(-100, 100) for j in range(4)] for i in range(7)]
    positive_sums = [sum(filter(lambda x: x > 0, row)) for row in A]
    print("Суммы положительных элементов каждой строки:")
    print(positive_sums)

lol()
#Задача 2 
import random

def create_matrix(M):
    A = [[random.randint(0, 9) for j in range(M)] for i in range(M)]
    return A

def count_nonzero_elements(row):
    return sum(1 for element in row if element != 0)

M = 5
A = create_matrix(M)

print("Матрица A:")
for row in A:
    print(row)

nonzero_counts = [count_nonzero_elements(row) for row in A]

print("Количество ненулевых элементов в каждой строке:")
print(nonzero_counts)

#Задача 3 
import random

def create_matrix(M, N):
    A = [[random.randint(0, 9) for _ in range(N)] for _ in range(M)]
    return A

def find_min_elements(row):
    return min(row)

M = 5
N = 4
A = create_matrix(M, N)

print("Матрица A:")
for row in A:
    print(row)

min_elements = [find_min_elements(row) for row in A]

print("Минимальные элементы в каждой строке:")
print(min_elements)
#Задача 4

import random

def frfr(M, N):
    A = [[random.randint(0, 9) for _ in range(N)] for _ in range(M)]
    return A

def lolkek(row):
    return sum(1 for elem in row if elem != 0)

M = 5
N = 4
A = frfr(M, N)

print("Матрица A:")
for row in A:
    print(row)

lolkek = [count_nonzero_elements(row) for row in A]

print("Количество ненулевых элементов в каждой строке:")
print(lolkek)

