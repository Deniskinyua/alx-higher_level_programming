#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = repr(number)
last_digit = x[-1]
y = int(last_digit)
word = f"The last digit of {number} is {last_digit}"
if y > 5:
    print(f"{word} and is greater than 5")
elif y == 0:
    print(f"{word} and is 0")
elif y > 0 < 6:
    print(f"{word} and is less than 6 and not 0")
