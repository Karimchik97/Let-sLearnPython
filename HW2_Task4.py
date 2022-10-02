# Реализуйте алгоритм перемешивания списка.

list = [12, 56, 28, 574, 983, 793, 5342, 62726, 5,73]

list_shuffled = []

for i in range (0, len(list)):
    k = random.randrange(0, len(list))
    list_shuffled.append(list[k])
    list.remove(list[k])
print (list_shuffled)

