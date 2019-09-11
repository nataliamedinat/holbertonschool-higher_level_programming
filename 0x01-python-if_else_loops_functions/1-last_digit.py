#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if lastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastdigit), sep="")
elif lastdigit == 0:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, lastdigit), sep="")
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastdigit), sep="")
