"""Найти самое длинное слово в введенном предложении.
   Учтите что в предложении есть знаки препинания"""


text = "какое морозное свежее утро"

for element in text.split():
    print(max(text.split(), key=len))