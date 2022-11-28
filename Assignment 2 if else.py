# Program for diamond shape pattern
rows = int(input("Enter number of rows :"))
for a in range(rows):
    for b in range(rows - a):
        print(" ", end=" ")
    for c in range(2 * a + 1):
        print("*", end=" ")
    print()
for x in range(rows, -1, -1):
    for y in range(rows - x):
        print(" ", end=" ")
    for z in range(2 * x + 1):
        print("*", end=" ")
    print()

# Q1 WAP to find reatest number
x = int(input("Enter number :"))
y = int(input("Enter number :"))
z = int(input("Enter number :"))
if y < x > z:
    print(x, "is greater number")
elif x < y > z:
    print(y, "is greater number")
elif x < z > y:
    print(z, "is greater number")
elif x == y == z:
    print("All number are equal")

# Q2 WAP to find minimum number

x = int(input("Enter number :"))
y = int(input("Enter number :"))
z = int(input("Enter number :"))
if y > x < z:
    print(x, "is smaller number")
elif x > y < z:
    print(y, "is smaller number")
elif x > z < y:
    print(z, "is smaller number")
elif x == y == z:
    print("All number are equal")

# Q3. WAP to check number is divisible by 5 and 11 or not

x = int(input("Enter number :"))
if (x % 5 == 0) and (x % 11 == 0):
    print("Number is divisible by 5 & 11")
else:
    print("Numbe ris not divisible by 5 & 11")

# WAP to find whether year is leap year or not.
x = int(input("Enter Year :"))
if (x % 4 == 0) or (x % 100 == 0) or (x % 400 == 0):
    print(x, "Year is leap year")
else:
    print(x, "The year is not leap year")

# Q4. WAP to check alphabet lies beetween I to s or i to s

x = input("Enter Character :")
if 'i' < x > 's':
    print("Number lies between i to s")
elif 'I' < x > 'S':
    print("Number lies between i to s")
else:
    print("Character does not lies between i to s")


# Q6 WAP to find input is alphabet or digit or special character

x = input("Enter Character :")
if x.isalpha():
    print("Input is alphabet")
elif x.isdigit():
    print("Input is number")
else:
    print("Input is special character")

# Q7 WAP to find character is uppercase or lowercase
x = input("Enter character :")
if x.isupper():
    print("Character is uppercase")
else:
    x.islower()
    print("Lowercase")

# Q8 WAP That takes the angles of trangles from the user and prints that triangle is valid or not
x = int(input("Enter Angle 1 of triangle : "))
y = int(input("Enter Angle 2 of triangle : "))
z = int(input("Enter Angle 3 of triangle : "))
if (x + y + z)== 180:
    print("Valid triangle")
else:
    print("Invalid triangle")


# Q9 calculate profit or loss. write program to take the cost price and selling price as input(take it hardcoded)
# and calculate it's a profit or loss
x = int(input("Enter Selling price : "))
y = int(input("Enter cost price: "))
z = x - y
if z > 0:
    print(z, "is profit")
elif z == 0:
    print(" no profit, no loss")
else:
    print(-z, "there is loss")

 # WAP to accept three numbers from user and check whether they are pythagorean triplets or not
x = int(input("Enter Input number : "))
y = int(input("Enter Input number : "))
z = int(input("Enter Input number : "))
if (x * x) + (y * y) == (z * z):
    print(" numbers are triplet")
else:
    print("numbers are not triplet")

