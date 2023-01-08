# write a program to print addition of all elements in matrix without using matrix function.
import numpy
rows = int(input("Enter rows:"))
cols = int(input("Enter cols:"))
arr = numpy.zeros((rows, cols), dtype=int)
print(arr)
addsum = 0
for x in range(rows):
    for y in range(cols):
        val = int(input("Enter element"))
        arr[x][y] = val
        addsum = addsum + val

print(arr)
print(addsum)


# write a program to print max number in  all elements in matrix without using matrix function max.
import numpy
rows = int(input("Enter rows:"))
cols = int(input("Enter cols:"))
arr = numpy.zeros((rows, cols), dtype=int)
print(arr)
cmp = 1
for x in range(rows):
    for y in range(cols):
        val = int(input("Enter element"))
        arr[x][y] = val
        if val >= cmp:
            cmp = val
        else:
            pass
print(arr)
print(cmp)

# write a program to print min number in  all elements in matrix without using matrix function min.
import numpy
rows = int(input("Enter rows:"))
cols = int(input("Enter cols:"))
arr = numpy.zeros((rows, cols), dtype=int)
print(arr)
cmpr = 1
for x in range(rows):
    for y in range(cols):
        val = int(input("Enter element"))
        arr[x][y] = val
        if val <= cmpr:
            cmpr = val
        else:
            pass
print(arr)
print(cmpr)

# write a program to print average of all elements in matrix without using matrix function average.
import numpy
rows = int(input("Enter rows:"))
cols = int(input("Enter cols:"))
arr = numpy.zeros((rows, cols), dtype=int)
print(arr)
sumadd = 0
for x in range(rows):
    for y in range(cols):
        val = int(input("Enter element"))
        arr[x][y] = val
        sumadd = sumadd + val

print(arr)
print(sumadd)
arv = rows * cols
averg = sumadd / arv
print(averg)