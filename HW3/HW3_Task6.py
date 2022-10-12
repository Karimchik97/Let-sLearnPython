# Реализуйте алгоритм задания случайных чисел без использования
# встроенного генератора псевдослучайных чисел. БЕЗ КАКИХ ЛИБО РАНДОМОВ

import datetime 

min_n = 10
max_n = 100

def get_rand():
    return datetime.datetime.now().microsecond%10

n = get_rand()

print(int(len(str(min_n))))
print(n)