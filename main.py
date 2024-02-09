while True:
    email = input("Введите письмо:")
    if len(email) > 25:
        print("Письмо отправлено!:")
        break
    else:
        print("Письмо должно содержать больше 25 символов. Пж допиши больше")
#
w = print("персонаж идет прямо")
a = print("персонаж идет в лево")
s = print("Персонаж идет назад")
d = print("персонаж идет вправо")
while True:
    choice = input("Выберете вариант ответа W,S,A,D")
    if choice.upper() == 'A':
        print("Вы выбрали вариант влево")
    elif choice.upper() == 'W':
        print("Вы выбрали идти вверх")
    elif choice.upper() == 'S':
        print("Вы идете вниз")
    elif choice.upper() == 'D':
        print("Вы идете вправо")
    else:
        print("Нене")