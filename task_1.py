""" 
Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
6782 -> 23
0,56 -> 11 
"""

print('Программа, которая принимает на вход число и показывает сумму его цифр.')
number = float(input("Введите число: "))
while number != int(number):
    number *= 10
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print(int(sum))

""" 
n = int(input('Введите число: '))
sum = 0
while n > 0:
    sum = sum + n % 10
    n = n / 10
print (sum) """

"""
num = float(input("Введите число: "))
def sum(num):
    while num != int(num):
        num *= 10
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

print(int(sum))
"""

#sum(map(int,(input('Введите вещественное число: ')))
