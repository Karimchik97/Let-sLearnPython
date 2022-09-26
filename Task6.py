# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
X = int(input("Enter X coordinates: "))
Y = int(input("Enter Y coordinates: "))
 
if X == 0 or Y == 0:
    print ("Coordinates value must be different from 0 in this task:)")
elif X > 0 and Y > 0:
    print ("Quarter 1")       
elif X < 0 and Y > 0:
    print ("Quarter 2")
elif X < 0 and Y < 0:
    print ("Quarter 3")
else:
    print ("Quarter 4")