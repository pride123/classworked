# Задача 1
m = int(input("Введите массу тела"))
v = int(input("Введите объём тела"))
p = m / v 
print("Ответ плотность тела равна",p)
# Задача 2
a = int(input("Введите число"))
b = int(input("Введите число"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# Задача 3
a = int(input("Введите положит число 1"))
b = int(input("Введите положит число 2"))
CA = a + b/2
CG = a*b ** 0.5 
print("Сред ариф", CA)
print("Сред гео",CG)
# Задача 4
n = int(input("Кол-во жителей"))
a = int(input("Площадь государства"))
p = n/a
print("Плотность населения равна", p)
# Задача 5
a =int(input("Ребра"))
b =int(input("Ребра"))
c =int(input("Ребра"))
S = 2*(a + b + c)
V = a*b*c
print("Площадь поверхности",S)
print("Оъём поверхности",V)