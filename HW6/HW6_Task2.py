#  Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# import random 
# from fileinput import close

# N = int (input("Enter a number (the size of future list): "))
# if N > 0:
#     list1 = []
#     for i in range(N):
#         a = round(random.random() * 10, 2)
#         list.append(a)
#     else:
#         print(f"Generated list: {list1}")
#         if N != 1:
#             list2 = []
#             for k in range(len(list1)):
#                 list2.append(list1[k] - int(list1[k]))
#                 difference = round(max(list2) - min(list2), 2)
#             else:
#                 print(f"The difference between the Maximum and minimum values:\n{difference}")
#         else:
#             print("There is onle one element in the list")
# else:
#     print("Value must be > 0! Let's try again!")


lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(new_lst)
print(max(new_lst) - min(new_lst))