# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
print ("Please, enter the number yoy want to check: ")
UserNumber = int(input())
if ((UserNumber % 10 == 0 or UserNumber % 15 == 0) and UserNumber % 30 != 0):
    print ("TRUE, the number a multiple of 5, 10 or 15, and not multiple of 30")
else:
    print("FALSE")