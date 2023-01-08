# capitalize method implementaation
str1 = "swapnali"
if 'a' <= str1[0] <= 'z':
    str2 = chr(ord(str1[0]) - 32) + str1[1:]
    print(str2)
else:
    print(str1)

# center method implementation
str1 = input("Enter string : ")
str2 = ""
str_length = int(input("Enter length of total str : "))
fill_char = input("Enter char to fill space : ")
a = (str_length - len(str1))
b = int(a / 2)
if a % 2 != 0:
    c = b + 1
else:
    c = b
if str_length >= len(str1):
    for p in range(c):
        str2 = fill_char + str2
    str2 = str2 + str1
    for q in range(b):
        str2 = str2 + fill_char
    print(str2)
else:
    print(str1)


# count method implementation

str1 = input("Enter String : ")
comp_char = (input("Enter Char to find in string : "))
count = 0
for x in range(len(str1)):
    if str1[x] == comp_char:
        count = count + 1
print(comp_char, "is found in this string", count, "times")
if count == 0:
    print("char not found in this string")

# endswith method implementation
str1 = input("Enter String : ")
comp_char = (input("Enter str to find in string : "))
b = len(comp_char)
str2 = ""
for x in range(-b, 0):
    str2 = str2 + str1[x]
if comp_char == str2:
    print("True")
else:
    print("False")

# find method implementation
str1 = input("Enter String : ")
comp_char = (input("Enter char to find in string : "))
b = len(comp_char)
str2 = ""
count = 0
for x in range(len(str1)):
    if comp_char == str1[x]:
        count = count + 1
        print("found at index", x)
if count == 0:
    print("not found")

# rfind method implementation
str1 = input("Enter String : ")
comp_char = (input("Enter char to find in string : "))
b = len(comp_char)
str2 = ""
flag = 0
for x in range(len(str1)):
    if comp_char == str1[x]:
        flag = 1
        break
print("found at index", x)
if flag == 0:
    print("not found")

# join method implementation
str1 = input("Enter String :")
str2 = input("enter join string :")
str3 = ""
for x in range(len(str1)):
    str3 = str3 + str2 + str1[x]
print(str3)

# lower method implementation
str1 = input("Enter String :")
str2 = ""
flag = 0
for x in range(len(str1)):
    if 'A' <= str1[x] <= 'Z':
        flag = 1
        str2 = str2 + chr(ord(str1[x]) + 32)
print(str2)
if flag == 0:
    print(str1)

