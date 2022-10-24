# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

with open (r"HW4/numbers.txt", "r") as data:
    numbers = data.read()

print(numbers)
list = []
for c in numbers:
    if c not in list:
        if numbers.count(c) == 1:
            list.append(int(c))
print(f"There is a list of non-repeating elements: {list}")