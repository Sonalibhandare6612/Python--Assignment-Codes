#  append method implementation.
num = int(input("Enter no. of elements in list"))
lst1 = [0,0,0,0,0]
for i in range(num):
    ele = int(input("Enter Element :"))
    lst1[-i] = ele
print(lst1)

# copy method implementation.
num = int(input("Enter no. of elements in list"))
lst1 = [0,0,0,0,0]
for i in range(num):
    ele = int(input("Enter Element :"))
    lst1[-i] = ele
print(lst1)
lst2 = lst1
print(lst2)

# count method implementation.
lst1 = [2,3,4,5,6,3,2,2,2]
inp = int(input("Enter element for count:"))
flag = 0
count = 0
for i in range(len(lst1)):
    if inp == lst1[i]:
        flag = 1
        count += 1
if flag == 0:
    print("0")
else:
    print(count)

# extend method implementation
lst1 = [2,4,5,6,7]
lst2 = [30,40]
a = len(lst1) + len(lst2)
for i in range(len(lst2)):
    lst1.append(lst2[i])

print(lst1)


# index method implementation
lst1 = [2,3,4,5,6,3,2,2,2]
inp = int(input("Enter element for count:"))
flag = 0
for i in range(len(lst1)):
    if inp == lst1[i]:
        print(i, end="  ")
        flag = 1
if flag == 0:
    print("None")

# insert method implementation

lst1 = [2, 3, 4, 5, 6, 3, 2, 2, 2]
inp = int(input("Enter index:"))
num = int(input("Enter element"))
lst2 = []
for i in range(len(lst1)):
    if inp == i:
        lst2.append(num)
        break
for x in range(inp, len(lst1)):
    lst2.append(lst1[x])
lst3 = []
for z in range(inp):
    lst3.append(lst1[z])
for s in range(len(lst2)):
    lst3.append(lst2[s])
print(lst3)


# pop method implementation.

lst1 = [2,3,4,5]
lst2 = []
for i in range(len(lst1)-1):
    lst2.append(lst1[i])
print(lst2)


# remove method implementation.

lst1 = [2,3,4,5,6,7]
inp = int(input("Enter index to remove element:"))
lst2 = []
for i in range(len(lst1)):
    if i == inp:
        pass
    else:
        lst2.append(lst1[i])
print(lst2)

# reverse method implementation.
lst1 = [2,3,4,5,6,7]
#print(lst1[-1::-1])
lst2 = []
for i in range(1,len(lst1)+1):
    lst2.append(lst1[-i])
print(lst2)





