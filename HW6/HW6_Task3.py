# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# string = "aaaaaaaaaaaabbbbbbbcccccc"
# zipString = f"{string.count('a')}a{string.count('b')}b{string.count('c')}c"

# print(zipString)

# unZip = ''
# zip = ''

# for i in zipString:
#     if i.isdigit():
#         zip += i
#     else:
#         unZip += str(int(zip) * i)
#         zip = ''
# print(unZip)


#                           MAP 
# ------------------------------------------------------

stringList = ["aaabbbccc", "aaaaaaaabbccc", "abbbccc"]

def zipElem(string):
    return  f"{string.count('a')}a{string.count('b')}b{string.count('c')}c"

zippedList = list(map(zipElem,stringList))

print(zippedList)

unZip = ''
zip = ''

for i in zippedList:
    if i.isdigit():
        zip += i
    else:
        unZip += str(int(zip) * i)
        zip = ''
print(unZip)

