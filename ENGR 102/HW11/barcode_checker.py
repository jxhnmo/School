# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   11.1 LAB: barcode checker
# Date:         11/13/2022
#

# import
from math import *

def valid(code):
    sum1, sum2 = 0, 0
    for i in range(len(code) - 1):  # cycling through to seperate
        if i % 2 == 0:
            sum1 += int(code[i])
        else:
            sum2 += int(code[i])

    lastDig = ((sum2 % 10) * 3)
    x = ((sum1 % 10) + lastDig) % 10
    lastSub = 10 - x  # takes the last digit and subtracts it from 10
    if int(code[-1]) == lastSub:
        return True
    else:
        return False

# input file name
fileName = input("Enter the name of the file: ")

#declaring variables
count = 0

# opening files
with open(fileName, 'r') as f:
    with open('valid_barcodes.txt', 'a') as o:
        barcodes = f.read().strip().split('\n') # split file into array
# run through each line on provided barcodes file
        for ln in barcodes:
            if valid(ln):
                count += 1
                o.write(f'{ln}\n') # writing into new file

print(f'There are {count} valid barcodes')