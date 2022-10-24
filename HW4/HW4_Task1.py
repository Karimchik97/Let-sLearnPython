# Вычислить число pi c заданной точностью *d*

d = input("Enter number precision(fractional number in the range from 0.1 to 0.0000000001): ")
if 0.1 >= float(d) >= 0.0000000001:
    n = abs(d.find('.') - len(d))-1
    h = int(n)
    k = 1
    x = 0
    import random
    for k in range(1, 1000000):
        x = x+4*((-1)**(k+1))/(2*k-1)
    print(f"There is what you want:*{d}*: {round(x,h)}")
else:
    print("Error, enter number precision(fractional number in the range from 0.1 to 0.0000000001)!")