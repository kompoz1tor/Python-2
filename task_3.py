""" 
Задание 3 Реализуйте алгоритм перемешивания списка. 
"""
import random
from random import randint

list = []
for i in range(5):
    list.append(randint(-10, 10))
print(f'Исходный список: {list}')

n = len(list)

for i in range(n):
    j = random.randint(0, n-1)
    element = list.pop(j)
    list.append(element)
print(f'Перемешанный список: {list}')