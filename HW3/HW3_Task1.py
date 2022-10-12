# Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

N = int (input("Enter a number (the size of future list): "))
if N > 0:
    list = random.sample(range(100), N)
    print(f"Here is the generted list {list}")
    if N == 1:
        print("There are NO elements in list in ODD positions")
    else:
        print("The elements in ODD positions: ")
    for i in range(1, len(list), 2):
            if i == N-1 or i == N-2:
                print(list[i])
            else:
                print(list[i], end=", ")
    else:
        print(f"sum of elements in ODD position: {sum(list[1::2])}") 
else:
    print("Value must be > 0! Let's try again!")

