# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int (input("Enter an integer: > 0: "))
if n > 0:
    f = []
    a = 2
    while a * a <= n:
        if n % a == 0:
            f.append(a)
            n//=a
        else:
            a += 1
    f.append(n)
    f = list(set(f))
    print(f"There is the list of prime factors of {n}: {f}")
else:
    print("Error! Let's try again!")