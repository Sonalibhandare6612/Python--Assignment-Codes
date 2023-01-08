'''
# Write a program to count number of characters and numbers in given input.
inp = (input("Enter string :"))
cstr = 0
nstr = 0
for x in range(len(inp)):
    if 'a' < inp[x] > 'z' or 'A' < inp[x] > 'Z':
        cstr = cstr + 1
    else:
        '0' < inp[x] > '9'
        nstr = nstr + 1
print()
print("there are", cstr, "characters")
print("there are", nstr, "numbers")

# Write a program take one string from user, then take one character as input ang find how many times
#   this character is present in this string or not.

inp = input("Enter string :")
inc = input("enter character to compare :")
count = 0
flag = 0
for x in range(len(inp)):
    if inp[x] == inc:
        count = count + 1
        flag = 1
        print("this character has came", count, "times")
if flag == 0:
    print("character not found")

    #  1 2 3 4
    #    5 6 7
    #      8 9
    #        10
    #     11 12
    #  13 14 15
    # 16 17 18 19
    # program for above pattern
rows = 4
num = 1
for x in range(rows):
    for y in range(x):
        print(" ", end=" ")
    for z in range(rows - x):
        print(num, end=" ")
        num = num + 1
    print()
for a in range(rows - 1):
    for b in range(rows - 2 - a):
        print(" ", end=" ")
    for z in range(a + 2):
        print(num, end=" ")
        num = num + 1
    print()
'''

# Q1 Pattern
for x in range(4):
    n = x + 1
    for y in range(4):
        print(n, end=" ")
        n = n + 3
    print()

