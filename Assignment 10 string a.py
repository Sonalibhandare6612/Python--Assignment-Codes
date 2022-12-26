# Q1 WAP that accepts a sentences from the user.And print that sentences.
str1 = input("Enter sentence :")
print(str1)
# Q2 WAP that accepts a string from user which contains characters from 'b' to 'y'.
str1 = input("Enter sentence :")
str2 = " "
for x in range(len(str1)):
    if 'b' < str1[x] < 'y' or 'B' < str1[x] < 'Y':
        str2 = str2 + str1[x]
print(str2)
# Q3 WAP that accepts sentences from user and print a no of small letters, capital letters, and digits into it.
str1 = input("Enter sentence :")
str2 = " "
smlletter = 0
capletter = 0
digit = 0
for x in range(len(str1)):
    if 'A' <= str1[x] <= 'Z':
        capletter = capletter + 1
    elif 'a' <= str1[x] <= 'z':
        smlletter = smlletter + 1
    elif '0' <= str1[x] <= '9':
        digit = digit + 1
print(str2)
print("there are", capletter, "capital letters in string")
print("there are", smlletter, "small letters in string")
print("there are", digit, "digits in string")

# Q4 WAP that accepts sentences from user and print length of sentences (implement strlen()).
str1 = input("Enter sentence :")
num = 0
for x in range(len(str1)):
    if 'a' <= str1[x] <= 'z' or 'A' <= str1[x] <= 'Z' or '0' <= str1[x] <= '9' or str1[x] == ' ':
        num = num + 1
print(num, "is length of string")
print(str1)
print(len(str1))

# Q5 WAP that takes sentences from user and prints a no of white spaces into it.
str1 = input("Enter sentence :")
num = 0
for x in range(len(str1)):
    if str1[x] == ' ':
        num = num + 1
print(num, "are white spaces in string")
print(str1)

# Q6 WAP to take sentence from user and print no. of words into it.
str1 = input("Enter sentence :")
num = 0
for x in range(len(str1)):
    if str1[x] == ' ':
        num = num + 1
num = num + 1
print(num, "are words in string")
print(str1)

# Q7 WAP to take sentence from user and print no of words of even and odd length of words from sentences.
str1 = input("Enter sentence :")
num = 0
for x in range(len(str1)):
    if str1[x] == ' ':
        num = num + 1
num = num + 1
print(num, "are words in string")
print(str1)

# Q8 WAP to take sentence from user and print last word from sentences.
str1 = input("Enter sentence :")
words = str1.split()
a = words[-1]
print(a)

# Q9 WAP to take sentence from user and position no. of any word and print word present at this position.
str1 = input("Enter sentence :")
res = ''
num = int(input("enter N number :"))
for x in range(num,len(str1)):
    if str1[x] == '':
        break
    res = str1[x]
print(str(res))

# Q10 WAP to convert string from uppercase to lowercase.
str1 = input("Enter sentence :")
str2 = str1.lower()
print(str2)

# Q11 WAP to convert string from lowercase to uppercase.
str1 = input("Enter sentence :")
str2 = str1.upper()
print(str2)

# Q12 WAP to toggle case of given input string.
str1 = input("Enter sentence :")
str2 = str1.swapcase()
print(str2)

# Q13 WAP to check whether given strings are anagram strings or not.
str1 = input("Enter sentence :")
str2 = input("Enter sentence :")
str1 = str1.lower()
str2 = str2.lower()
if len(str2) == len(str1):
    sortstr1 = sorted(str1)
    sortstr2 = sorted(str2)
    if sortstr2 == sortstr1:
        print("These are anagram strings")
    else:
        print("not anagram strings")
else:
    print("length of strings is not same")


# Q14 WAP that accepts strings from user and copies the string into some another strings.
str1 = input("Enter sentence :")
str2 = str1
print(str2)

# Q15 WAP that accepts strings from user and copies the first N characters into some destination string.
str1 = input("Enter sentence :")
num = int(input("enter N number :"))
str2 = str1[0:num]
print(str2)

# Q16 WAP  that accepts strings from user and accept the number N then copy the last N characters into other string.
str1 = input("Enter sentence :")
num = int(input("enter N number :"))
str2 = str1[num-1:]
print(str2)


# Q17 WAP  that accepts two strings from user and append second string to first string
str1 = input("Enter string1 :")
str2 = input("Enter string2 :")
strans = str1 + str2
print(strans)

# Q18 WAP  that accepts two strings from user and appends N characters of second string to first string.
str1 = input("Enter string1 :")
str2 = input("Enter string2 :")
N = int(input("Enter N value"))
strresult = str1 + str2[0:N]
print(strresult)

# Q19 WAP  that accepts two strings from user and compares two strings.If both strings are equal then return 0,
# otherwise return difference between first mismatched characters.
str1 = input("Enter string1 :")
str2 = input("Enter string2 :")
if str1 == str2:
    print("0")
else:
    for x in range(len(str1)):
        a = ord(str1[x]) - ord(str2[x])
        if a > 0:
            print("Difference between two strings is ", a)
            break

# Q20 WAP  that accepts two strings from user and compares only first N characters of two strings.If both strings
# are equal till the first N characters then return 0 otherwise return the difference between first mismatched
# characters.
str1 = input("Enter string1 :")
str2 = input("Enter string2 :")
N = int(input("Enter N value :"))
if str1[0:N+1] == str2[0:N+1]:
    print("0")
else:
    for x in range(len(str1[0:N+1])):
        a = ord(str1[x]) - ord(str2[x])
        if a > 0:
            print("Difference between first mismatch characters is ", a)
            break

# Q21 WAP  that accepts two strings from user and compares two string without case sensitivity.If both are equal
# then return 0.Otherwise return difference between first mismatched characters.
strx = input("Enter string1 :")
stry = input("Enter string2 :")
str1 = strx.lower()
str2 = stry.lower()
N = int(input("Enter N value :"))
if str1[0:N+1] == str2[0:N+1]:
    print("0")
else:
    for x in range(len(str1[0:N+1])):
        a = ord(str1[x]) - ord(str2[x])
        if a > 0:
            print("Difference between first mismatch characters is ", a)
            break

# Q22 WAP that accepts strings from user and reverse this string without taking other string
str1 = input("Enter string1 :")
num = len(str1)
for x in range(-1,-(num+1),-1):
    print(str1[x], end="")

# Q23. WAP that accepts strings from user and reverse string till the first N characters without taking second str.
str1 = input("Enter string1 :")
N = int(input("Enter value of N :"))
num = len(str1)
for x in range((N-1),-1,-1):
    print(str1[x], end="")
print()
print("input string is :", str1)

# Q24  WAP that accepts strings from user and reverse string till the last N characters without taking second str.
str1 = input("Enter string1 :")
N = int(input("Enter value of N :"))
num = len(str1)
for x in range(-1,-(N+1),-1):
    print(str1[x], end="")
print()
print("input string is :", str1)

# Q25 WAP  that accepts strings from user and then accepts a range and then reverse a string in that range
# without taking another string.
str1 = input("Enter string1 :")
N1 = int(input("Enter value of N from:"))
N2 = int(input("Enter value of N to:"))
num = len(str1)
for x in range(-(num-N2+1),-(num-N1+2),-1):
    print(str1[x], end="")
print()
print("input string is :", str1)

# Q26 WAP  that accepts strings from user and reverse words from strings.
str1 = input("Enter string :")
str2 = str1.split()
print(str2)
print(len(str2))
for x in range(len(str2)):
    strx = str2[x]
    print(strx[-1::-1], end=" ")

# Q27 WAP  that accepts strings from user and reverse words in strings of even length.
str1 = input("Enter string :")
str2 = str1.split()
print(str2)
print(len(str2))
for x in range(len(str2)):
    strx = str2[x]
    n = len(strx)
    if n % 2 == 0:
        print(strx[-1::-1], end=" ")
    else:
        print(strx[0:], end=" ")

# Q28 WAP  that sets all characters in a strings to a specific character.
str1 = input("Enter string :")
str2 = input("Enter string replace character :")
str3 = " "
print(str1)
for x in range(len(str1)):
    str3 = str3 + str2
print(str3)


# Q29 WAP  that sets the first N characters in a strings to a specific character.
str1 = input("Enter string :")
str2 = input("Enter character to replace :")
str3 = " "
N = int(input("Enter value of N :"))
print(str1)
for x in range(0,N):
    str3 = str3 + str2
str1 = str3 + str1[N:]
print(str1)

# Q30  WAP  that sets the last N characters in a strings to a specific character.
str1 = input("Enter string :")
str2 = input("Enter character to replace :")
str3 = " "
N = int(input("Enter value of N :"))
print(str1)
a = len(str1) - N
for x in range(a,len(str1)):
    str3 = str3 + str2
str1 = str1[0:a] + str3
print(str1)

# Q31. WAP that accepts strings from user and searches for the first occurrence of a specific characters in
# the strings and returns the position at which the character is found.
str1 = input("Enter string :")
str2 = input("Enter character to find :")
for x in range(len(str1)):
    if str1[x] == str2:
        print("character found at ", x, "index")

# Q32 WAP that accepts strings from user and searches for the last occurrence of a specific characters in
# # the strings and returns the position at which the character is found.
str1 = input("Enter string :")
str2 = input("Enter character to find :")
print(str1.rfind(str2))





















