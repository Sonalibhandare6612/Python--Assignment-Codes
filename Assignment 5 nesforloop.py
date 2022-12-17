# Q1 WAP to print multiples of number Take input from user
a = int(input("Enter number :"))
b = int(input("Enter limit :"))
n = 1
c = int(b / a)
for x in range(c):
    out = a * n
    print(out, end=",")
    n = n + 1
# Q2 parren code to print suares of odd numbers
rows = int(input("Enter no of rows :"))
cols = int (input("Enter no of cols :"))
n = 1
for x in range(rows):
    for y in range(cols):
        if n % 2 != 0:
            print(n * n, end=" ")
        else:
            print(n, end=" ")
        n = n + 1
    print()

# Q3 pattern code
rows = int(input("Enter no of rows :"))
cols = int (input("Enter no of cols :"))
for x in range(rows):
    n = 69
    for y in range(cols):
        data = chr(n)
        print(data, end="     ")
        n = n - 1
    print()

# Q4 pattern code
rows = int(input("Enter no of rows :"))
cols = int (input("Enter no of cols :"))
for x in range(rows):
    for y in range(x + 1):
        if y % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

# Q5 Parrern code
rows = int(input("Enter no of rows :"))
cols = int (input("Enter no of cols :"))
for x in range(rows):
    n = x + 1
    p = n
    for y in range(x + 1):
        print(n, end=" ")
        n = n + p
    print()

# Q6 WAP to print table of 1 to n in reverse order. n limit take from user.
inp = int(input("Enter number limit :"))

for x in range(inp):
    n = 1
    for y in range(10):
        out = inp * n
        print(out, end=" ")
        n = n + 1
    inp = inp - 1
    print()

# Q7 WAP to print alternative numbers in reverse order between 15 to 30.
inp = int(input("Enter number limit :"))

for x in range(inp):
    n = 1
    for y in range(10):
        out = inp * n
        print(out, end=" ")
        n = n + 1
    inp = inp - 1
    print()

# Q8 WAP to print count of even numbers which are 5 in number 1 - 50
a = int(input("Enter start no :"))
b = int(input("Enter limit no. :"))
n = 1
for x in range(b):
    if n % 5 == 0:
        print(n, end=" ")
    n = n + 1

#Q9 WAP to print pattern

a = int(input("Enter no rows :"))
b = int(input("Enter no cols :"))
n = 1
for x in range(a):
    for y in range(x + 1):
        print(n, end=" ")
        n = n + 1
    print()
    n = n - 1

 # WAP to print series series of prime numbers from entered range. take start and end no from user.

a = int(input("Enter start no :"))
b = int(input("Enter limit no. :"))
for x in range(a, b + 1):
    flag = 0
    for i in range(2, x):
        if x % i == 0:
            flag = 1
    if flag == 0:
        print(x, end=" ")





