#Задача 1 
def select_numbers_less_than_P(P):
    n = 1
    while True:
        number = (n + 1) ** 0.5
        if number < P:
            print(number)
        else:
            break
        n += 1

P = 5  # Заданное число P
select_numbers_less_than_P(P)
#Задача 2
def print_numbers_between(A, B):
    for number in range(A+1, B):
        print(number)

A = 3  # Заданное число A
B = 8  # Заданное число B
print_numbers_between(A, B)
#ЗАДАЧА 3
def print_numbers_between_descending(A, B):
    for number in range(B-1, A, -1):
        print(number)

A = 3  # Заданное число A
B = 8  # Заданное число B
print_numbers_between_descending(A, B)
#Задача 4 
N = 10  # Заданное целое число N
smallest_K = (N + 2) // 3  # Наименьшее целое число K
result = smallest_K * 3  # Значение 3K

print(f"Наименьшее целое число K: {smallest_K}")
print(f"Значение 3K: {result}")
#Задача 5
N = 10  # Заданное целое число N

K = (N - 1) // 3  # Наибольшее целое число K, удовлетворяющее неравенству 3K < N

print(f"Наибольшее целое число K: {K}")
