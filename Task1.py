# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

print ("Enter your number: ")
N = int(input())
for i in range (-N, N+1):
    print ( i, end="," )