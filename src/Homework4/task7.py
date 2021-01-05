""" Даны два натуральных числа.
 Вычислите их наибольший общий делитель при помощи
алгоритма Евклида (мы не знаем функции и рекурсию)
"""


a = 12
b = 18

while a != 0 and b != 0:
    if a > b:
        a = a % b

    else:
        b = b % a

print("Наибольший общий делитель чисел", a + b)
