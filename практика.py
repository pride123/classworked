class Tourist:
    def __init__(self, surname, country, tour_country, year, trip_year, cost):
        self.surname = surname
        self.country = country
        self.tour_country = tour_country
        self.year = year
        self.trip_year = trip_year
        self.cost = cost
tourist1 = Tourist("Россия", "Франция", "Италия", 2020, 2021, 1500.50)
print("Имя:", tourist1.surname)
print("Страна:", tourist1.country)
print("Страна для путешевствий:", tourist1.tour_country)
print("Год:", tourist1.year)
print("Год поездки:", tourist1.trip_year)
print("Цена: Руб", tourist1.cost)
print("\nНовая дата:")
surname = input("Введите имя: ")
country = input("Введите страну: ")
tour_country = input("Введите страну для тура: ")
year = int(input("Введите Год: "))
trip_year = int(input("год поездки: "))
cost = float(input("Сколько надо: руб"))

tourist2 = Tourist(surname, country, tour_country, year, trip_year, cost)

print("\nNew data:")
print("Surname:", tourist2.surname)
print("Country:", tourist2.country)
print("Tour Country:", tourist2.tour_country)
print("Year:", tourist2.year)
print("Trip Year:", tourist2.trip_year)
print("Cost: $", tourist2.cost)


#Задача 2
A = float(input("Введите значение A: "))
B = float(input("Введите значение B: "))
C = float(input("Введите значение C: "))

result = A * (B / 3.14) + (C * 3 + 5)

print("\nРезультат A*(B/3.14) + (C*3 + 5):", result)
#Задача 3
R, Y = map(float, input("Ввести значение R,Y: ").split())
result = R * Y**3 + (Y / 5)
print("Результат этих вычислений R*Y³ + (Y/5):", result)
#Задача 4 
A = float(input("Введите A: "))
integer_part = int(A)
fractional_part = A - integer_part
sqrt_value = A ** 0.5
remainder = A % 5
print("Интегрировать значение A:", integer_part)
print("Часть A:", fractional_part)
print(" A:", sqrt_value)
print(" 5:", remainder)
#Задача 5
minutes = int(input("Введите числа и минуты в формате 0:00: "))

# Вычисление часов и минут
hours = minutes // 60
minutes_remainder = minutes % 60

# Вывод времени в часах и минутах
print("Время:", hours, "Часы", minutes_remainder, "минуты")
