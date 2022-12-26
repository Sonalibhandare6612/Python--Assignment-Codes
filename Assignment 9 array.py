# Q1 WAP that takes a character array as input.But only print characters, do no print special characters.
#        input : a c h $ g @
#        output : a c h g

import numpy

num = int(input("Enter no of elements :"))
arr = numpy.zeros(num, str)
for x in range(num):
    ele = input("Enter elements :")
    if 'a' <= ele <= 'z' or 'A' <= ele <= 'Z':
        arr[x] = ele
    else:
        pass
print(arr)

# Q2 WAP to sort the array in ascending order.Take input from user.
import numpy

num = int(input("Enter no of elements :"))
arr = numpy.zeros(num, str)
for x in range(num):
    ele = int(input("Enter elements :"))
    arr[x] = ele
print(arr)
arr1 = numpy.sort(arr)
print("Sorted array is :")
print(arr1)

# Q3 WAP to find the number of even and odd elements in given array of integers.
import numpy

num = int(input("Enter no of elements :"))
arr = numpy.zeros(num, int)
even = 0
odd = 0
for x in range(num):
    ele = int(input("Enter elements :"))
    arr[x] = ele
    if ele % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(arr)
print("there are", even, "even numbers in given array")
print("there are", odd, "odd numbers in given array")

# Q4 WAP to take 1-D array from user and calculate cube of elements at even indexes and squares at odd indexes.
# Reflect those calculations in array.
import numpy

num = int(input("Enter no of elements :"))
arr = numpy.zeros(num, int)

for x in range(num):
    ele = int(input("Enter elements :"))
    arr[x] = ele
print(arr)
result_arr = numpy.zeros(num, int)
for y in range(len(arr)):
    if y % 2 == 0:
        a = arr[y] ** 3
        result_arr[y] = a
    elif y % 2 != 0:
        b = arr[y] * arr[y]
        result_arr[y] = b

print(result_arr)

# Q5 WAP to merge two given arrays.
import array

arr1 = array.array('i', [1, 2, 3, 4, 5])
arr2 = array.array('i', [6, 8, 2, 4, 3])
lst1 = arr1.tolist()
lst2 = arr2.tolist()
lst = lst1 + lst2
arr = array.array('i', [])
arr.fromlist(lst)
print(arr)

# Q6 WAP to create an array of 'n' integer elements. Where the 'n' value should be taken from the user.
#  insert the values from user and find prime numbers from array.
# input:
# n = 5
# Enter elements in array:
# 2, 3, 6, 9, 5, 7

import array

arr1 = array.array('i', [])
num = int(input("Enter length of string :"))
for x in range(num):
    ele1 = int(input("Enter element:"))
    arr1.append(ele1)
print(arr1)
for y in range(len(arr1)):
    num = arr1[y]
    if num > 0:
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                print(num, "is prime number")

# Q7 WAP to create an array of 'n' integer elements. Where the 'n' value should be taken fron user.
#   insert the values from the user find the strong number from them.
# input: n = 5
# enter elements in the array:
#  2, 145, 6, 3, 123, 2
# output : 145


# Q8 WAP to take input from user and find armstrong number in the array.
# input : 1,5,22,65,153,371
# output: 1,5,153
import array
arr = array.array('i',[])
num = int(input("Enter no. of elements :"))
for i in range(num):
    ele = int(input("Enter element:"))
    arr.append(ele)
print(arr)
for j in arr:
    num = j
c_num = num
x = len(str(num))
asum = 0
while num > 0:
    digit = num % 10
    asum = asum + digit ** x
    num = num // 10
print(asum)
if c_num == asum:
    print(asum,"is Armstrong number")
else:
    print("not armstrong number")

# Q9 WAp to take two 1-D arrays from the user and calculate addition of elements at the same indexes from both arrays.
# store the sum in the third array and print all three arrays.
import array

arr1 = array.array('i', [])
arr2 = array.array('i', [])
result_arr = array.array('i', [])
n = int(input("Enter 'N' value :"))
for x in range(n):
    ele1 = int(input("Enter element for arr1:"))
    arr1.append(ele1)
    ele2 = int(input("Enter element for arr2 :"))
    arr2.append(ele2)
print(arr1)
print(arr2)
for y in range(len(arr1)):
    a = arr1[y] + arr2[y]
    result_arr.append(a)

print("result of sum is:")
print(result_arr)

# Q10 WAP to take two 1-D character arrays from user. Compare elements at the same indexes and print positive
#  differences between them.
# input :
#   C O R E
#   T E C H
# OUTPUT:
# T - C = 17
# O - E = 10
import array

arr1 = array.array('u', [])
arr2 = array.array('u', [])
num = int(input("Enter length of string :"))
for x in range(num):
    ele1 = input("Enter element:")
    arr1.append(ele1)
print(arr1)
for y in range(num):
    ele2 = input("Enter element:")
    arr2.append(ele2)
print(arr2)
for z in range(len(arr1)):
    if len(arr1) == len(arr2):
        a = ord(arr2[z]) - ord(arr1[z])
        if a > 0:
            print(arr2[z], "-", arr1[z], "=", a)
