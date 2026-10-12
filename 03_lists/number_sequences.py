"""Циклы while и for: последовательности чисел и целочисленное деление."""


# Задача 1. Вывести числа √2, √3, √4, ... пока они меньше P
def print_roots_less_than(p):
    n = 2
    while n ** 0.5 < p:
        print(n ** 0.5)
        n += 1


print_roots_less_than(5)


# Задача 2. Числа строго между A и B по возрастанию
def print_numbers_between(a, b):
    for number in range(a + 1, b):
        print(number)


print_numbers_between(3, 8)


# Задача 3. Числа строго между A и B по убыванию
def print_numbers_between_descending(a, b):
    for number in range(b - 1, a, -1):
        print(number)


print_numbers_between_descending(3, 8)

# Задача 4. Наименьшее целое K, при котором 3K >= N
N = 10
smallest_k = (N + 2) // 3
print(f"Наименьшее K, для которого 3K >= {N}: {smallest_k} (3K = {smallest_k * 3})")

# Задача 5. Наибольшее целое K, при котором 3K < N
N = 10
largest_k = (N - 1) // 3
print(f"Наибольшее K, для которого 3K < {N}: {largest_k}")
