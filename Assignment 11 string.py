# Q1 WAP to search given string in array of string.Print index if string is found.
import numpy
arr = numpy.array(["Riya","Ajay","Priya","Raj","Isha"])
inp = input("Enter string to compare :")
flag = 0
for i in range(len(arr)):
    if inp == arr[i]:
        flag = 1
        print("String found at index ", i, end=" ")
if flag == 0:
    print("string not found")

# Q2 WAP to reverse given string.
str1 = input("Enter string :")
print(str1)
print("Reversed string is :",str1[-1::-1])

# Q3 WAP to reverse only words of string.
str1 = input("Enter string :")
print(str1)
str2 = str1.split()
print(str2)
for x in range(len(str2)):
    strx = str2[x]
    str3 = strx[-1::-1]
    print(str3, end=" ")

# Q4 WAP to concatenate N number of strings without using library function. (take N number of strings.)
N = int(input("Enter no. of strings :"))
str2 = " "
for x in range(N):
    ele = input("Enter string :")
    str2 = str2 + ele
print(str2)


# Q5 WAP to capitalize the first letter of each word in given string.
str1 = input("Enter element in string :")
str2 = str1.split()
print(str1)
for x in range(len(str2)):
    strx = str2[x]
    capstr = chr(ord(strx[0]) - 32)
    strx = capstr + strx[1:]
    print(strx, end=" ")

# Q6 WAP to check whether given string is palindrome or not.(racecar)
str1 = input("Enter string :")
print(str1)
c_str = str1
revstr = str1[-1::-1]
if revstr == c_str:
    print("Given string is palindrome string")
else:
    print("Given string is not palindrome string")

# Q7 WAP to count frequency of each letter in string.
str1 = input("Enter string :")
print(str1)
for x in range(len(str1)):
    a = str1.count(str1[x])
    print(str1[x], "-", a)

# Q8 WAP to remove the occurrences of a specified letter character.
str1 = input("Enter string :")
print(str1)
N = input("Enter specified letter to remove :")
str2 = " "
for x in range(len(str1)):
    a = str1[x]
    if a == N:
         pass
    else:
        str2 = str2 + a
print(str2)



# Q9 WAP to remove duplicate characters from string.
strs = input("Enter string :")
print(strs)
strs = ''.join(sorted(set(strs), key=strs.index))
print(strs)


# Q10 WAP to sort strings on their length. You should accept an array of string and return a sorted array based upon
# length of string.

import numpy
arr = numpy.array(["Raj","Yami","Riya","Ajay","Seeta", "Jay"])
arr2 = (sorted(arr,key=len))
print(arr2)



















