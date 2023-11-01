# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   7.8 LAB: Zybooks Lab 4 Kaprekars Constant
# Date:         10/12/2022
#

from math import *

#user input and initializing vars
num = input("Enter a four-digit integer: ")
variations = [num]
count = 0
tempNum = int(num)


while tempNum != 6174 and count < 9:
    #seperating the digits into a list
    digits = [0] * 4
    for i in range(4):
        digits[i] = tempNum % 10
        tempNum = int(tempNum / 10)

    #sorting digits
    digits.sort()
    asc = 0
    for i in range(4):
        asc = asc * 10 + digits[i]

    digits.sort()
    desc = 0
    for i in range(3, -1, -1):
        desc = desc * 10 + digits[i]

    tempNum = abs(asc - desc)
    variations.append(tempNum)

    count += 1

count += 1
if digits[0] != digits[1] and digits[1] != digits [2] and digits[2] != digits[3]: #check for 4 repeating numbers
    for i in range(0, count):           #printing
        print(f'{variations[i]}', end='')
        if i != count - 1:
            print(f' > ', end='')
    print(f'\n{num} reaches 6174 via Kaprekar\'s routine in {count - 1} iterations')
else:
    print(f'{num} > 0\n{num} reaches 0 via Kaprekar\'s routine in 1 iterations')