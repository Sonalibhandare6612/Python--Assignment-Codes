# Take Two numbers 1-100, find numbers divisible by 4 & 5 or 6 & 7. Print them and also give count of them.

count = 0
for x in range(1, 101):
    if (x % 4 == 0 and x % 5 == 0) or (x % 6 == 0 and x % 7 == 0):
        print(x)
        count = count + 1
print("count", + count)

# Take 3 input data from user (marks) compare them and print output. Ask user to continue process or not.
a = int(input("Enter Kunal age : "))
b = int(input("Enter Kirthi age : "))
c = int(input("Enter Surendra age : "))
print(a)
print(b)
print(c)
if (a > b) and (a > c):
    print("Kunal is elder than others")
elif (b > a) and (b > c):
    print("Kirthi is elder than others")
elif (c > a) and (c > b):
    print("Surendra is elder than others")
