# Напишите программу, которая найдёт произведение пар чисел списка
# (Список создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random

from math import prod
N = int (input("Enter a number (the size of future list)"))
if N > 0:

    list = random.sample(range(10), N)
    print(f"Generated list: {list}")
    if N == 1:
        print("Element has no pair")
    else:
        chet = 1
        list = []
        middle = 0
    if N % 2 != 0:
        chet = 0
        middle = round(N/2) + 1
    else:
        middle = round(N/2)
    list1 = []
    for i in range(middle):
        if chet !=1 and i == middle:
            list1.append(list[i]^2)
        else:
            list1.append(list[i]*list[N-1-i])
    print(f"Multiplication of elements of list: {list1}")
else:
    print("Value must be > 0! Let's try again!")