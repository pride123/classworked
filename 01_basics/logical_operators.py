"""Логические операторы and / or и сравнение строк."""

a = 4
b = 3

both_false = (a < 15) and (a > 15)
b_is_large = (b > 15) and (b > 30)
any_positive = (a >= 2) or (b >= 1)
one_matches = (b == 3) or (a == 4)

print(both_false)    # False
print(b_is_large)    # False
print(any_positive)  # True
print(one_matches)   # True

# Строки сравниваются посимвольно, по кодам символов
str1 = "a"
str2 = "b"
both_less_than_c = str1 < "c" and str2 < "c"
print(both_less_than_c)  # True
