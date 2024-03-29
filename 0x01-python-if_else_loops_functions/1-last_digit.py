#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_digit_sign = -1 if number < 0 else 1
print(f"Last digit of {number} is {last_digit * last_digit_sign}", end=" ")
if (last_digit * last_digit_sign) > 5:
    print(f"and is greater than 5")
elif (last_digit * last_digit_sign) == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
