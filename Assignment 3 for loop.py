# Q1 WAP to print first 10 numbers
inp = 10
num = 1
for x in range(inp):
    print(num, end=" ")
    num = num + 1

# Q2 WAP to print the first 100 numbers
inp = 100
num = 1
for x in range(inp):
    print(num, end=" ")
    num = num + 1

# Q3 WAP to print first 10 , 3 digit number
inp = 10
num = 100
for x in range(inp):
    print(num, end=" ")
    num = num + 1

# Q4 WAP to print even numbers 1 - 100
a = 1
for x in range(101):

    if a % 2 == 0:
        print(a)
    else:
        pass

    a = a + 1
# Q5 WAP to print odd number from 1 - 50

a = 1
for x in range(50):

    if a % 2 != 0:
        print(a)
    else:
        pass

    a = a + 1
# Q6 WAP to print reverse from 100 - 1
a = 100
for x in range(100):
    print(a)
    a = a - 1


# Q7 WAP to print table of 12
a = 12
for x in range(1, 11):
    print(a * x)


# OR
a = 1
for x in range(1 , 11):
    print(a * 12)
    a = a + 1

# Q8 WAP to print table of 12 in reverse order

a = 10
for x in range(1 , 11):
    print(a * 12)
    a = a - 1

# Q9 WAP to sum of first 10 numbers
a = 1
sumadd = 0
for x in range(10):
    print(a, end=" ")
    a = a + 1
    sumadd = sumadd + a
print()
print(sumadd, "is sum of all numbers")

# Q 10 WAP to print product of first 10 numbers

a = 1
prod = 1
for x in range(10):
    print(a, end=" ")
    prod = prod * a
    a = a + 1
print()
print(prod, "is product of all numbers")


