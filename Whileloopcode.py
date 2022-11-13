# Take Range of 1-100, then print output numbers divisible by 4 & 5 or 6 & 7. Also print count.

a = 1
b = 100
count = 0
while a < b+1:
    if (a % 4 == 0 and a % 5 == 0) or (a % 6 == 0 and a % 7 == 0):
        print(a)
    count = count + 1
    a = a + 1
    print("count", + count)

# Write code to take input age of 3 person and compare them.
s = int(input("Type value 1 to continue :"))
p = int(input("Enter Ravi age"))
q = int(input("Enter Seema age"))
r = int(input("Enter Riya age"))
t = 1
while s == t:
    if (p > q) and (p > r):
        print("Ravi is elder than others")
    elif (q > p) and (q > r):
        print("Seema is elder than others")
    elif (r > p) and (r > q):
        print("Riya is elder than others")
    s = s + 1
