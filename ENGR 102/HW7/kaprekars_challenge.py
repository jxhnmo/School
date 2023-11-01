# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   7.9 LAB: Zybooks Lab 5 Kaprekars Constant Challenge
# Date:         10/12/2022
#

from math import *

#user input and initializing vars
totalCount = 0

for num in range(9999):
    #print(num)      #test
    count = 0
    tempNum = num


    while tempNum != 6174 and count < 9:
        #seperating the digits into a list
        digits = [0] * 4
        for i in range(4):
            digits[i] = tempNum % 10
            tempNum = int(tempNum / 10)

        #print(digits)      #test

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
        count += 1
        #print(asc)      #test
        #print(desc)
        #print(tempNum)

    if tempNum == 6174:
        totalCount += count
    else:
        totalCount += 1
    count = 0
    #print('\n\n')      #test
print(f'Kaprekar\'s routine takes {totalCount} total iterations for all four-digit numbers')