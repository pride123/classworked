"""Операции со списками: remove, del, insert, sort и разбор чисел по группам."""

# Задание 1. Удалить из списка все числа (элементы не-фигуры)
shapes = ["круг", 0.25, "квадрат", "треугольник", 15, "круг", "овал", "10"]
shapes.remove(0.25)
shapes.remove(15)
shapes.remove("10")
print(shapes)

# Задание 2. Удалить срез элементов
letters = ["A", "B", "C", "D", "E", "F", "G"]
del letters[1:5]
print(letters)

# Задание 3. Вставить элементы в нужные позиции
numbers = [1, 4]
numbers.insert(1, 2)
numbers.insert(2, 3)
print(numbers)

# Задание 4. Сортировка по возрастанию и по убыванию
values = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
values.sort()
print(values)
values.sort(reverse=True)
print(values)

# Задание 5. Разложить введённые числа на положительные, нули и отрицательные
positives = []
zeros = []
negatives = []
count = int(input("Введите количество чисел: "))
for _ in range(count):
    number = int(input("Введите число: "))
    if number > 0:
        positives.append(number)
    elif number == 0:
        zeros.append("*")
    else:
        negatives.append(number)

print("Сумма отрицательных:", sum(negatives))
if positives:
    print("Среднее положительных:", sum(positives) / len(positives))
else:
    print("Положительных чисел нет")
print("Количество нулей (звёздочек):", len(zeros), zeros)
