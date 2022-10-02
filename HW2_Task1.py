# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

N = int(input("Enter your number: "))
sum = 0
while (N != 0):
    sum = sum + N % 10
    N = N // 10
print("Desired value: " and  sum)
