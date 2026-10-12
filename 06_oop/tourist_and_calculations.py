"""Класс Tourist и набор задач на вычисления и обработку массивов."""

import random


class Tourist:
    def __init__(self, surname, country, tour_country, year, trip_year, cost):
        self.surname = surname
        self.country = country
        self.tour_country = tour_country
        self.year = year
        self.trip_year = trip_year
        self.cost = cost

    def show(self):
        print("Фамилия:", self.surname)
        print("Страна проживания:", self.country)
        print("Страна тура:", self.tour_country)
        print("Год рождения:", self.year)
        print("Год поездки:", self.trip_year)
        print("Стоимость, руб:", self.cost)


# Задача 1. Создание объектов класса
tourist1 = Tourist("Иванов", "Россия", "Италия", 2000, 2021, 1500.50)
tourist1.show()

print("\nНовый турист:")
tourist2 = Tourist(
    input("Введите фамилию: "),
    input("Введите страну проживания: "),
    input("Введите страну тура: "),
    int(input("Введите год рождения: ")),
    int(input("Введите год поездки: ")),
    float(input("Введите стоимость, руб: ")),
)
print()
tourist2.show()

# Задача 2. Вычисление выражения A*(B/3.14) + (C*3 + 5)
a = float(input("\nВведите A: "))
b = float(input("Введите B: "))
c = float(input("Введите C: "))
print("A*(B/3.14) + (C*3 + 5) =", a * (b / 3.14) + (c * 3 + 5))

# Задача 3. Вычисление выражения R*Y³ + Y/5
r, y = map(float, input("Введите R и Y через пробел: ").split())
print("R*Y³ + Y/5 =", r * y ** 3 + y / 5)

# Задача 4. Целая и дробная часть, корень и остаток от деления на 5
a = float(input("Введите A: "))
print("Целая часть:", int(a))
print("Дробная часть:", a - int(a))
print("Квадратный корень:", abs(a) ** 0.5)
print("Остаток от деления на 5:", a % 5)

# Задача 5. Перевод минут в часы и минуты
total_minutes = int(input("Введите количество минут: "))
print("Время:", total_minutes // 60, "ч", total_minutes % 60, "мин")

# Задача 6. Массив C и массив D = C² - 5
array_c = [random.randint(1, 9) for _ in range(10)]
array_d = [x ** 2 - 5 for x in array_c]
print("Массив C (горизонтально):")
print("\t".join(map(str, array_c)))
print("Массив D (вертикально):")
for element in array_d:
    print(element)

# Задача 7. Самая большая и самая маленькая планета по радиусу, км
planet_radii = [2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622, 1188]
print("Радиусы планет:")
for radius in planet_radii:
    print(radius)
print("Самая большая планета:", max(planet_radii))
print("Самая маленькая планета:", min(planet_radii))

# Задача 8. Индексы нулевых элементов массива
values = [5, 0, 3, 0, 0, 7, 8, 0, 2, 0, 4, 1]
print("Массив из 12 элементов:", values)
zero_indexes = [i for i, value in enumerate(values) if value == 0]
print("Индексы нулевых элементов:", zero_indexes)
