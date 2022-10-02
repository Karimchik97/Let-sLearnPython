# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму

n = int(input("Enter your number: "))
if n > 0:
    list = {}
    sum = 0
    for i in range(1, n+1):
        list[i] = round((1+1/i)**i, 2)
        sum += float(list[i])

    print(f"Here is the list: {list}")
    print(f"The sum of the elements is: {round(sum, 2)}")
else:
    print("Error. Let's try again!")