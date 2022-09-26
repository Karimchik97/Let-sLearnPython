# Напишите программу,которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.


print ("Please, enter an integer from 1 to 7: ")
UserNumber = int(input())
if (UserNumber == 1):
    print ("It's Monday. You have to work!:)")
elif (UserNumber == 2):
    print ("It's Tuesday. You have to work!:)")
elif (UserNumber == 3):
    print ("It's Wednesday. You have to work!:)")
elif (UserNumber == 4):
    print ("It's Thursday. You have to work!:)")
elif (UserNumber == 5):
    print ("It's Friday. You still have to work, but weekend is near!:)")
elif (UserNumber == 6):
    print ("It's Saturday. You can sleep for a long time!It's day off!!!:)")
elif (UserNumber == 7):
    print ("It's Sunday. Day off! Have fun:)")
else:
    print("Error. Please, enter an integer from 1 to 7.")
