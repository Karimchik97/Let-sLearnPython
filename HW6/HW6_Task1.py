# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open ("HW5\\text.txt","r",encoding="UTF-8") as data:
#       list = data.read()
#       list = list.split(" ")
#       print(list)

# newList = []

# for i in range(len(list)-1):
#     if (list[i].lower().find("абв") == -1):
#         newList+= list[i]+ " "
# print(" ".join(newList))

# data = open (r"HW5\\text1.txt", "w", encoding="UTF-8")
# data.write(" ".join(newList))
# data.close()

# def rm_pattern(usr_data: str, pattern: str) -> str:

# WITH LIST COMPREHENTION
#---------------------------------------------


with open ("HW5\\text.txt","r",encoding="UTF-8") as data:
      list = data.read()
      list = list.split(" ")
      print(list)

newList = [word for word in list if 'абв' not in word]

print(" ".join(newList))

data = open (r"HW6\\text.txt", "w", encoding="UTF-8")
data.write(" ".join(newList))
data.close()


