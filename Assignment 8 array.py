# Q1 WAP to find even numbers from given array.
import array
inp = int(input("Enter no. of elements in array :"))
arr1 = array.array('i', [])
for x in range(inp):
    ele = int(input("Enter element :"))
    if ele % 2 == 0:
        arr1.append(ele)
print(arr1)

# Q2 WAP to find odd numbers in given array.
import array
inp = int(input("Enter no. of elements in array :"))
arr1 = array.array('i', [])
for x in range(inp):
    ele = int(input("Enter element :"))
    if ele % 2 != 0:
        arr1.append(ele)
print(arr1)

# Q3 WAP to find prime number in given array.
import array
arr = array.array('i', [])
inp = int(input("Enter no. of elements in array :"))
for x in range(inp):
    ele = int(input("Enter element :"))
    arr.append(ele)
print(arr)
for y in arr:
    if y > 1:
        for z in range(2,y):
            if y % z == 0:
                break
        else:
            print(y, end=" ")
# Q4 WAP to sum alternate numbers in given array.
import array
inp = int(input("Enter no. of elements in array :"))
arr1 = array.array('i', [])
addsum = 0
for x in range(inp):
    ele = int(input("Enter element :"))
    arr1.append(ele)
    if x % 2 == 0:
        addsum = addsum + ele
print(arr1)
print(addsum)
# Q5 WAP to find occurrence of given number from the array.
import array
inp = int(input("Enter no. of elements in array :"))
arr1 = array.array('i', [])
for x in range(inp):
    ele = int(input("Enter element :"))
    arr1.append(ele)
print(arr1)
a = int(input("Enter no. to find Occurance :"))
flag = 0
count = 0
for y in range(inp):
    if arr1[y] == a:
        flag = 1
        count = count + 1
if flag == 0:
    print("Number not found ")
else:
    print("this no. found ", count, "Times")

# Q6 WAP to find min and max number from the array.
import array
inp = int(input("Enter no. of elements in array :"))
arr1 = array.array('i', [])
for x in range(inp):
    ele = int(input("Enter element :"))
    arr1.append(ele)
print(arr1)
max = 0
for y in range(inp):
    if arr1[y] > max:
        max = arr1[y]
print("maximum number is", max)
min = arr1[0]
for z in range(inp):
    if (min >= arr1[z]):
        min = arr1[z]

print("minimum number is", min)

# Q7 WAp to search given element and print its index
import array
inp = int(input("Enter no. of elements in array :"))
arr1 = array.array('i', [])
for x in range(inp):
    ele = int(input("Enter element :"))
    arr1.append(ele)
print(arr1)
a = int(input("Enter number to find index :"))
flag = 0
for i in range(len(arr1)):
    if a == arr1[i]:
        flag = 1
        print("number found at", i, "position")
        break
if flag == 0:
    print("number not found")


# Q8 WAP to reverse an array.
import array
inp = int(input("Enter no. of elements in array :"))
arr1 = array.array('i', [])
for x in range(inp):
    ele = int(input("Enter element :"))
    arr1.append(ele)
print(arr1)
a = len(arr1)
print(arr1[-1::-1])
# Q9 WAP to find duplicates from given array.
import array
inp = int(input("Enter no. of elements in array :"))
arr1 = array.array('i', [])
for x in range(inp):
    ele = int(input("Enter element :"))
    arr1.append(ele)
print(arr1)
for i in range(len(arr1)):
    for j in range(i + 1, len(arr1)):
        if arr1[i] == arr1[j]:
            print(arr1[j], end=" ")
# Q10 WAP to swap two consecutive numbers in the array
               #  input: [1,2,3,4,5,6,7,8]
               #  output : [2,1,4,3,6,5,8,7]
import array

arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
temp = 0
for x in range(0, 8, 2):
    temp = arr[x]
    arr[x] = arr[1 + x]
    arr[1 + x] = temp
print(arr)


