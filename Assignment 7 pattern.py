# Q1 Pattern

# Q2 Pattern
rows = int(input("Enter no of rows :"))
cols = int(input("Enter no of cols :"))
num = 65
for x in range(rows):
    for y in range(cols):
        if (x == 0 and y == 1) or (x == 1 and y == 0) or (x == 1 and y == 2) or (x == 2 and y == 1):
            num = num + 32
            data = chr(num)
            num = num - 32
            print(data, end=" ")
        else:
            data = chr(num)
            print(data, end=" ")
        num = num + 1
    print()

 # Q3 pattern
rows = int(input("Enter no of rows :"))
cols = int(input("Enter no of cols :"))
for x in range(rows):
    num = 68
    n = 4
    for y in range(cols):
        data = chr(num)
        print(data, n, end="  ")
        num = num - 1
        n = n - 1

    print()

# Q4 Pattern
rows = int(input("Enter no of rows :"))
num = 100
c_num = num
for x in range(rows):
    num = c_num - x
    for y in range(rows - x):
        data = chr(num)
        print(data, end="  ")
        num = num - 1

    print()

# Q5 pattern
rows = int(input("Enter no of rows :"))
num = 69
c_num = num
n = 5
c_n = n
for x in range(rows):
    num = c_num - x
    n = c_n - x
    for y in range(rows - x):
        if x % 2 == 0:
            print(n, end=" ")
            n = n - 1
        else:
            data = chr(num)
            print(data, end=" ")
            num = num - 1
    print()

 # Q7 Pattern
rows = int(input("Enter no of rows :"))
num = 9
n = 1
for x in range(rows):
    for y in range(rows - x + 1):
        print(" ", end="   ")
    for z in range(x + 1):
        print(n * num, end="   ")
        n = n + 1
    print()

 # Q8 pattern
rows = int(input("Enter no of rows :"))
num = 97
n = 1
c_num = num
c_n = n
for x in range(rows):
    num = c_num + x
    n = c_n + x
    for y in range(rows - x + 1):
        print(" ", end=" ")
    for z in range(x + 1):
        if x % 2 == 0:
            data = chr(num)
            print(data, end=" ")
            num = num - 1
        else:
            print(n, end=" ")
            n = n - 1

    print()

# Q9 pattern
rows = int(input("Enter no of rows :"))
for x in range(rows):
    num = 97
    n = 1
    for y in range(rows - x + 1):
        print(" ", end=" ")
    for z in range(x + 1):
        if x % 2 == 0:
            data = chr(num)
            print(data, end=" ")
            num = num + 1
        else:
            print(n, end=" ")
            n = n + 1

    print()

 # Q10 pattern
rows = int(input("Enter no of rows :"))
n = 1
for x in range(rows):
    n = 1 + x
    for y in range(rows - x - 1):
        print(" ", end=" ")
    for z in range(x + 1):
        print(n, end=" ")
        n = n + x + 1
    print()