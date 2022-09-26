#Напишите программу, 
# которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
UserNumber = float(input("Enter a number of Quater you want to check:"))
if UserNumber == 1:
    print ("X-coordinates: from 0 to ∞      Y-coordinates: from 0 to ∞)")
elif UserNumber == 2:
    print ("X-coordinates: from - ∞ to 0   Y-coordinates: from 0 to ∞)")     
elif UserNumber == 3:
    print ("X-coordinates: from - ∞ to 0  Y-coordinates: from 0 to  - ∞")
elif UserNumber == 4:
    print ("X-coordinates: from 0 to ∞  Y-coordinates: from 0 to  - ∞")
else:
    print ("There are only four quaters. No other way. Please FIX the mistake.")

