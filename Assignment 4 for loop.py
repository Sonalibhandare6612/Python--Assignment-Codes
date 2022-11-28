# Q1 WAP to print ASCII value of all characters
inp = input("Enter character :")
c = inp
print(ord(c))

# WAP to print patterns
#1.

rows = 3
cols = 3
num = 1
for x in range(rows):
    for y in range(cols):
        print(num, end=" ")
        num = num + 1
    print()

#2.
rows = 3
cols = 3
num = 1
for x in range(rows):
    for y in range(cols):
        print((num * num), end=" ")
        num = num + 1
    print()

#3.

rows = 3
cols = 3
num = 65
for x in range(rows):
    for y in range(cols):
        data = chr(num)
        print((data), end=" ")
        num = num + 1
    print()

#4.
rows = 3
cols = 4
for x in range(rows):
    num = 65
    for y in range(cols):
        data = chr(num)
        print(data, end=" ")
        num = num + 1
    print()

#5.

rows = 3
cols = 4
for x in range(rows):
    num = 68
    inp = 4
    for y in range(cols):
        data = chr(num)
        print(data, inp, end=" ")
        num = num - 1
        inp = inp - 1
    print()

#7.
rows = 4
cols = 4
for x in range(rows):
    for y in range(cols):
        if y % 2 == 0:
            print("$", end="   ")
        else:
            print("=", end="   ")
    print()

#8.

rows = 4
cols = 4
n = 1
for x in range(rows):
    for y in range(cols):
        if n % 2 == 0:
            print(n, end="   ")
        else:
            print(n * n, end="   ")
        n = n + 1
    print()
#9.
rows = 3
cols = 3
n = 1
for x in range(rows):
    for y in range(cols):
        print(n, end="  ")
        n = n + 2
    print()

#10.

rows = 3
cols = 3
n = 2
incr = 3
for x in range(rows):
    for y in range(cols):
        print(n, end=" ")
        n = n + incr
        incr = incr + 2
    print()
