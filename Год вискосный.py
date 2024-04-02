#зАДАЧА 4
def is_year_leap ():
    year = int(input("Введите год"))
    if year %4:
        print("Год високосный")
    else:
        print("Не високосный")
    return year 
year = is_year_leap()