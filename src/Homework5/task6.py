"""Вводится число найти его максимальный делитель,
 являющийся степенью двойки. 10(2) 16(16), 12(4).
"""

import math
print("Введите число")
n = int(input())
i = 1
while n >= 2 ** i:
    i += 1
degree = 2 ** (i - 1)

print("Ближайшая степень двойки к введенному числу", degree)

print(math.gcd(n, degree))
