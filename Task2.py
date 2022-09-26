# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
print ("Enter a fractional number: ")
UserNumber = float(input())
DesiredValue = int((UserNumber * 10) % 10) 
print (DesiredValue)
