# Q1. sum of numbers 1 - 10
a = int(input("Enter number limit :"))
add = 0
x = 1
while x < a + 1:
    add = add + x
    x = x + 1
print(add)

# Q2 product of 1-10
a = int(input("Enter number limit :"))
add = 1
x = 1
while x < a + 1:
    add = add * x
    x = x + 1
print(add)

# Q3 Factorial of given numbers
num = int(input("Enter number to calculate factorial :"))
ans = 1
while num > 0:
    ans = ans * num
    num = num - 1
print("Factorial on given no. is :", ans)

# Q4 write a program to count given number
num = int(input("Enter number :"))
count = 0
while num > 1:
    count = count + 1
    num = num // 10
    print(num, end=",")
print()
print(count, "is no. of count in given number")

# Q5 WAP to count even digits of given number
num = int(input("Enter number :"))
count = 0
while num > 1:
    num = num // 10
    if num % 2 == 0:
        print(num, end=",")
        count = count + 1
print()
print(count, "is no. of count of even numbers")

# Q6 WAP count of odd digits
num = int(input("Enter number :"))
count = 0
while num > 1:
    num = num // 10
    if num % 2 != 0:
        print(num, end=",")
        count = count + 1
print()
print(count, "is no. of count of even numbers")

# Q7 WAP to reverse given number
num = int(input("Enter number :"))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(str(rev))
# Q8 WAP to check whether number is palindrome number.(2332)
num = int(input("Enter number to reverse :"))
c_num = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(str(rev))
if c_num == rev:
    print(c_num, "is palindrome number ")
else:
    print(c_num, "is not palindrome number")

# Q9 WAP to check whether the number is Armstrong number or not.(371)
num = int(input("Enter number to reverse :"))
c_num = num
addsum = 0
order = len(str(num))
while num > 0:
    digit = num % 10
    addsum = addsum + digit ** order
    num = num // 10
if c_num == sum:
    print(c_num, "is armstrong number ")
else:
    print(c_num, "is not armstrong number")

# Q10 WAp to check whether the given number is strong number or not.(145)
num = int(input("Enter number to reverse :"))
c_num = num
addsum = 0
order = len(str(num))
while num > 0:
    digit = num % 10
    facto = 1
    while digit > 0 :
        facto = facto * digit
        digit = digit - 1
    addsum = addsum + facto
    num = num // 10
if c_num == addsum:
    print("number is strong number")
else:
    print("number is not strong number")
