# Арифметические действия с числами-)))
# Даны 2 числа. 2 действиями вывести:
# Сумму и разность
print('Подсчитать сумму и разность чисел 3 и 8')
a = 3
b = 8
print(a + b)
print(a - b)

""" Дано число n. Вывести квадрат каждого числа, 
предшествующего числу n, не включая квадрат n"""

print('Вывести квадрыты чисел в интервале от 0 до 5, не включая 5')

n = 5
for number in range(n):
    print(number ** 2)

""" Напишите программу, вычисляющую по двум заданным 
катетам гипотенузу прямоугольного треугольника"""

print('Вычислить по сторонам треугольника его гипотенузу')

side_one = 5
side_two = 12
hypotenuse = (side_one ** 2) + (side_two ** 2)

hypotenuse = (hypotenuse ** 1/2)

hypotenuse = round(hypotenuse, 11)
print(hypotenuse)

"""Напишите программу, которая считывает строку,
состояющую из целых чисел (разделены пробелом) 
и выводит только те числа, которые стоят на 
чётных индексах"""

counter = '1 3 5 8 12 4 5 812 '
string = counter.split()
for i in range(0, len(string), 2):
    print(string[i], end=' ')

"""Напишите программу, которая считывает 
одно целое число N и выводит N строк, 
содержащих N звёздочек в каждой строке 
(без пробелов)"""

Number_ = 10
for i in range(Number_):
    print(Number_ * "*", end='\n')
