# Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

N = int (input("Enter your mumber: "))
if N > 0:
    def fibonacci(N):
        a, b = 0, 1
        for i in range(N+1):
            yield a
            a, b = b, a + b
    data = list(fibonacci(N))
    def fibonacci(N):
        a, b = -1, -1
        for i in range(N):
            yield a
            a, b = b, a + b
    data1 = list(fibonacci(N))
    data2 = data1[::-1]
    print("Here is the list: ")
    res = data2 + data
    for i in range(0, len(res)):
            if i == len(res)-1:
                print(res[i])
            else:
                print(res[i], end=", ")
else:
    print("Value must be > 0! Let's try again!")