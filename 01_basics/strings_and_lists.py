"""Шпаргалка по срезам строк и операциям со списками."""

num1 = 23
num2 = 42
del num1          # удаляет одну переменную
num1 = 23
del num1, num2    # удаляет сразу две переменные

text = "hello, python!"
print(text[0])        # первый символ
print(text[0:5])      # символы с 0 по 4 включительно
print(text[4:10])     # символы с 4 по 9
print(text[0:14])     # вся строка
print(text[7:])       # с 7-го символа до конца
print(text[:5])       # то же, что text[0:5]
print(text[:])        # копия всей строки
print(text[-1])       # последний символ
print(text[-1:-14])   # пустая строка: при шаге +1 начало правее конца
print(text[::2])      # каждый второй символ
print(text[::-1])     # строка задом наперёд
print(text + " nice to code")  # склейка строк
print(text[-1] * 10)  # десять восклицательных знаков

my_list = [True, 786, 3.14, "text", 70.2]
second_list = [123, "text"]

print(my_list)                # весь список
print(my_list[0])             # первый элемент
print(my_list[1:3])           # второй и третий элементы
print(my_list[2:])            # элементы начиная с третьего
print(second_list * 2)        # список, повторённый дважды
print(my_list + second_list)  # объединение списков
