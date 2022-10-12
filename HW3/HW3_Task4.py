# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

userNumber = int(input("Enter your number: "))
N = userNumber
binum = ""
while N > 0:
    binum = str(N % 2) + binum
    N //= 2
print(f"Число {userNumber} в двоичной системе это {binum}.")