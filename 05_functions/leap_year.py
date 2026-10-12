"""Функция, проверяющая, високосный ли год."""


def is_leap_year(year):
    """Год високосный, если делится на 4, но не на 100, либо делится на 400."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


if __name__ == "__main__":
    year = int(input("Введите год: "))
    if is_leap_year(year):
        print("Год високосный")
    else:
        print("Год не високосный")
