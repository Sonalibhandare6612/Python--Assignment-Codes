# Q1 WAP to convert 1D array into 2D array.
import numpy
arr1 = numpy.array([1,2,3,4,5,6,7,8,9])
arr2 = arr1.reshape(3,3)
print(arr2)
# Q2 WAP to convert 2D array to 1D array.
import numpy
arr1 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = arr1.flatten()
print(arr2)
# Q3 WAP to take input from the user into an array and remove duplicate numbers.
#                                input : [1,1,2,3,3,4,5,2,6,7]
#                                output : [1,2,3,4,5,6,7]
import array

arr1 = array.array('i', [1, 1, 2, 3, 3, 4, 5, 2, 6, 7])
arr1 = sorted(arr1)
print(arr1)
x = 0
while (x < len(arr1)):
    y = x + 1
    while (y < len(arr1)) and arr1[x] == arr1[y]:
        arr1.pop(y)
        y = y + 1
    x = x + 1
print(arr1)



# Q4 WAP to take 2D array of order 3 x 3 and check whether the matrix is an identity matrix or not.
import numpy
num = int(input("Enter no of rows , cols :"))
arr = numpy.zeros((num,num),int)
for x in range(num):
    for y in range(num):
        ele = int(input("Enter element :"))
        arr[x][y] = ele
print(arr)
flag = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j and arr[i][j] != 1:
            flag = 1
            break
        if i != j and arr[i][j] != 0:
            flag = 1
            break
if flag == 0:
    print("identity matrix")
else:
    print("not identity matrix")

# Q5 WAP to take 2D array of order 3 x 3 and swap 1st row with 3rd row and print it as before and after operation.
import numpy
num = int(input("Enter no of rows , cols :"))
arr = numpy.zeros((num,num),int)
for x in range(num):
    for y in range(num):
        ele = int(input("Enter element :"))
        arr[x][y] = ele

print("Before swap")
print(arr)
arr[[0, 2]] = arr[[2, 0]]
print("After swap")
print(arr)

# Q6 WAP to find third largest elements from an array
                    # input : [[1,3,5]
                    #         [4,3,9]
                    #         [8,6,11]]
                    # otput : 8 is third largest element in given array
import numpy
arr = numpy.array([[1, 3, 5], [4, 3, 9], [8, 6, 11]])
arr1 = arr.flatten()
arr1.sort()
print("Third largest element is", arr1[-3])
# Q7 WAP take 2D array of order 3 x 3 and sort that array in ascending order and print it as before and after operation
import numpy
num = int(input("Enter no of rows , cols :"))
arr = numpy.zeros((num,num),int)
for x in range(num):
    for y in range(num):
        ele = int(input("Enter element :"))
        arr[x][y] = ele
print(arr)
arr1 = numpy.sort(arr,axis=1)
print("Column sort is :")
print(arr1)
arr2 = numpy.sort(arr, axis=0)
print("Row sort is :")
print(arr2)

# Q8 WAP to create 2D array of integer elements. Take the no.of rows and columns values from user. And print a 2D array
#      of numbers whose first digit is N, take the N value from user.
             # enter no of rows : 2
             # enter no of cols : 2
             # enter value of N : 3
             #   3  30
             #   31 32
import numpy
num = int(input("Enter no of rows , cols :"))
statrnum = int(input("Enter Starting number :"))
arr = numpy.zeros((num, num), int)
a = statrnum
for x in range(num):
    for y in range(num):
        arr[x][y] = a
        if arr[x][y] == statrnum:
           a = a * 10 - 1
        a = a + 1

print(arr)
# Q9 WAP to move all the zeros at the end of array.
import numpy
num = int(input("Enter no of rows , cols :"))
arr = numpy.zeros((num,num),int)
for x in range(num):
    for y in range(num):
        ele = int(input("Enter element :"))
        arr[x][y] = ele
print(arr)
arr = numpy.eye(3,k=-2,dtype=int)
print(arr)


# Q10 WAP to convert all zeros to ones and ones to zeros.
import numpy
num = int(input("Enter no of rows , cols :"))
arr = numpy.zeros((num,num),int)
for x in range(num):
    for y in range(num):
        ele = int(input("Enter element :"))
        arr[x][y] = ele
print(arr)
for i in range(num):
    for j in range(num):
        if arr[i][j] == 0:
            arr[i][j] = 1
        elif arr[i][j] == 1:
            arr[i][j] = 0
print(arr)
