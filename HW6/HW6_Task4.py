# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input("Enter your number: "))
# k = 0
# for i in range(1, n):
#     k = i * (i+1)
#     print(k)

# ENUMERATE

n = int(input("Enter your number: "))
list = [i * (i+1) for i in range(1, n)]
list2 = enumerate(list,1)
print(list(list2))
# print(list(enumerate(list, 1)))




