#Задача 1 
a = int(input())
b = int(input())
print(max(a,b))
#задача 2 
a = int(input())
b = int(input())
c = int(input())
if a+b > c and a + c > b and b + c >a:
    print("Да")
else:
    print("Нет")
#Задача 3
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Да")
else:
    print("Нет")
