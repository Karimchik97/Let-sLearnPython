# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

string = "aaaaaaaaaaaabbbbbbbcccccc"
zipString = f"{string.count('a')}a{string.count('b')}b{string.count('c')}c"

print(zipString)

unZip = ''
zip = ''

for i in zipString:
    if i.isdigit():
        zip += i
    else:
        unZip += str(int(zip) * i)
        zip = ''
print(unZip)