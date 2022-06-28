#!/usr/bin/python3
import random
number = random.randint(-20, 20)
if number == 0:
    print(number, 'is zero')
elif number > 0:
    print(number, 'is positive')
else:
    print(number, 'is negative')
