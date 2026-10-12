"""Условия: знак числа и сравнение двух переменных."""

# Задача 1. Знак числа
number = int(input("Введите число: "))
if number > 0:
    print("Число положительное")
elif number < 0:
    print(-1)
else:
    print(1)

# Задача 2. Преобразование числа в зависимости от знака
number = int(input("Введите любое число: "))
if number > 0:
    number = number / 100
    print("Положительное число делим на 100:", number)
elif number < 0:
    number = number + 1111111111111111
    print("К отрицательному числу прибавляем 1111111111111111:", number)
else:
    print("Ноль не подходит")

# Задача 3. Разность или сумма двух чисел
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
if first > second:
    result = first - second
elif first < second:
    result = first + second
else:
    result = first
print("Результат:", result)
