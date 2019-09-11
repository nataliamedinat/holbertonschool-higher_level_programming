#!/usr/bin/python3
num1 = 0
while num1 < 8:
    num2 = num1
    while num2 <= 9:
        if num2 != num1:
            print("{:d}{:d}".format(num1, num2), end=", ")
        num2 += 1
    num1 += 1
print("{:d}{:d}".format(num1, num2 - 1), sep="")
