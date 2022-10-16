# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от-100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

from random import randint as rI


def createEquation():
    global degree = int(input("Введите максимальную степень многочлена: "))
    equation = ''

for d in range(degree, -1, -1):
    coef = rI(-20,20)
if d == degree:
    if coef > 0:
        equation += str(coef) + 'x^' + str(d)
    if coef < 0:
        equation += '-' + str(abs(coef)) + 'x^' + str(d)
    else:
    if coef > 0:
        equation += ' + ' + str(coef) + 'x^' + str(d)
    if coef < 0:
        equation += ' - ' + str(abs(coef)) + 'x^' + str(d)

return equation + ' = 0'