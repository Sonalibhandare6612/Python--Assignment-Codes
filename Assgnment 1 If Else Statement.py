# Q1.Write a program to find a maximun number from given two numbers, take input from user
x = int(input("Enter Number to compare :"))
y = int(input("Enter Number to compare :"))
if x > y:
    print(x, "is greater number between ", x,"&", y)
else:
    print(y, "is greater number between", x,"&", y)

# Q2. Write a program to find whether given input number is positive,negative or zero
x = int(input("Enter Number :"))
if x < 0:
    print(x, "is negative number")
elif x > 0:
    print(x, "is positive number")
else:
    print(x, "is 0")

# Q3. Write a program to find whether giver number is odd or even

x = int(input("Enter Number :"))
if x % 2 == 0:
    print(x, "is even number")
else:
    print(x, "is odd number")

# Q4. Write program to find whether given number is divisible by 5 or not

x = int(input("Enter Number :"))
if x % 2 == 0:
    print(x, "is even number")
else:
    print(x, "is odd number")

# Q5. Write program to display weekdays, input from 0 to 6

x = int(input("Enter Number from 0 to 6:"))
if x == 0:
    print("This is Sunday")
elif x == 1:
    print("This is Monday")
elif x == 2:
    print("This is Tuesday")
elif x == 3:
    print("This is Wednesday")
elif x == 4:
    print("This is Thursday")
elif x == 5:
    print("This is Friday")
else:
    print("This is Sunday")

# Q6. Write a program to check whether the character is alphabet or not.
x = int(input("Enter Number:"))
if (x > 65 or x < 90) and (x > 97 or x < 122):
    print("Number is character")
else:
    print("Number is not character")

 # Q7. Write program to take number of months and print the number of days in that month.
x = int(input("Enter number 1 to 12 for month to check no. of days :"))
if x == 1:
    print("January month has 31 days")
elif x == 2:
    print("February month has 28 days")
elif x == 3:
    print("March month has 31 days")
elif x == 4:
    print("April month has 30 days")
elif x == 5:
    print("May month has 31 days")
elif x == 6:
    print("June month has 30 days")
elif x == 7:
    print("July month has 31 days")
elif x == 8:
    print("August month has 31 days")
elif x == 9:
    print("September month has 30 days")
elif x == 10:
    print("October month has 31 days")
elif x == 11:
    print("November month has 30 days")
else:
    print("December month has 31 days")

# Q8. Write a program to check whether number is greater than 10 or not
x = int(input("Enter number to compare with 10:"))
if x > 10:
    print("Number is greater than 10")

else:
    print("Number is not greater than 10")

# Q9. Write a program to check whether the input character vowel or consonant

x = int(input("enter number between 65 to 90 and 97 to 122 to check :"))
if x == 97:
    print("Number is Vowel")
elif x == 101:
    print("Number is Vowel")
elif x == 105:
    print("Number is Vowel")
elif x == 111:
    print("Number is Vowel")
elif x == 117:
    print("Number is Vowel")
elif x == 65:
    print("Number is Vowel")
elif x == 69:
    print("Number is Vowel")
elif x == 73:
    print("Number is Vowel")
elif x == 79:
    print("Number is Vowel")
elif x == 85:
    print("Number is Vowel")
else:
    print("Number is consonant")

# Q10. Write a program to determine levels

x = int(input("enter number to check :"))
if 0 < x < 100:
    print("Genin")
elif 100 < x < 500:
    print("Chunin")
elif 500 < x < 1000:
    print("Jonin")
elif x > 1000:
    print("Hokage")
else:
    print("nothing")





