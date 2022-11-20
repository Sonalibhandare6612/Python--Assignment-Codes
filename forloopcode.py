
i = int(input("Do you want to compare enter 1? "))
while (i == 1):
    a = int(input("Enter Kunal mark :"))
    b = int(input("Enter Meera mark :"))
    c = int(input("Enter Ketan mark :"))
    if (a > b) and (a > c):
            print("Kunal has greater marks")
    elif (a > b) and (a > c):
            print("Meera has greater marks")
    else :
            (a > b) and (a > c)
            print("Ketan has greater marks")
    user = int(input("Enter 1 to continue"))

  # write code to display pattern below
  #  1 2 3 4
  #  5 6 7 8
  #  9 10 11 12
  #  13 . . .

rows = int(input("Enter number of rows :"))
cols = int(input("Enter number of cols :"))
num = 1
for x in range(rows):
    for y in range(cols):
        print(num, end=" ")
        num = num + 1
    print()


# write code for this pattern
#   1 4 9                         17 15 13
#  16 25 36                       11  9  7
# 49 64 81                        5   3  1

numros = 3
numcols = 3
inp = 17
for s in range(numros):
    for t in range(numcols):
        print(inp, end="  ")
        inp = inp - 2
    print()

diff = 3
tos = 1
for p in range(numros):
    for q in range(numcols):            #
        print(tos, end="  ")
        tos = tos + diff
        diff = diff + 2
    print()

    # display pattern and do addition of all numbers in matrix
#    1 2 3 4
#    5 6 7 8
#    9 10 11 12
#    13 14 15 16

thisrow = 4
thiscol = 4
num = 0
sumadd = 0
for m in range(thisrow):
    for n in range(thiscol):
        print(num, end=" ")

        sumadd = num + sumadd
        num = num + 1

    print()
print("Addition of all numbers in matrix is :", sumadd)

# print following patter and do addition of only diagonal numbers.
#     \1\  2  3
#     4 \5\ 6
#   7  8  \9\

rows = 3
cols = 3
num = 1
sum = 0
for m in range(rows):
    for n in range(cols):
        print(num, end=" ")
        if m == n:
            sum = sum + num

        num = num + 1
    print()
print("Addition of diagonal number is :", sum)

# diagonal characters print
rows = 4
cols = 4
inp = 97
for x in range(rows):
    for y in range(cols):
        if x <= y:
            data = chr(inp)
            print(data, end=" ")
        inp = inp + 1
    print()

# print this pattern
 #   A B C
 #   * * *
 #   1 2 3
 #   D E F
 #   4 5 6
 #   * * *

rows = 6
cols = 3
num = 65
n = 1
for x in range(rows):
    for y in range(cols):
        if x % 3 == 0:
            data = chr(num)
            print(data, end=" ")
            num = num + 1
        elif x % 2 == 0:
            print(n, end=" ")
            n = n + 1
        else:
            print("*", end=" ")

    print()


 # Diamond shape Program

rows = 5
for x in range(rows):
    for y in range(rows - x - 1):
        print(" ", end=" ")
    for z in range((x * 2) + 1):
        print("*", end=" ")
    print()
for x in range(rows - 1):
    for y in range(x + 1):
        print(" ", end=" ")

    for z in range((2 * (rows - x)) - 3):
        print("*", end=" ")
    print()