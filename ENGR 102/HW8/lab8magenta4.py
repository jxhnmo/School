# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.13 LAB: Python Program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in aGiven Range of Numbers
# Date:         10/18/2022
#

#user input
small = int(input('Finding numbers divisible by 7 and multiple of 5 in a given range of numbers.\nInput min value of range: '))
large = int(input('Input max value of range: '))
divSeven = []
mulFive = []

#finding values from given range
for i in range(small, large):
    if i % 7 == 0:
        divSeven.append(i)
    elif i % 5 == 0:
        mulFive.append(i)

#printing
print(f'In the range {small} to {large}, these numbers were divisble by seven:\n{divSeven}\nand these numbers were multiples of five:\n{mulFive}')