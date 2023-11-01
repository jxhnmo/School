# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   7.7 LAB: Zybooks Lab 3 Vector Math
# Date:         10/12/2022
#

from math import *

#user input and var initialization
vectorA = [float(x) for x in input("Enter the elements for vector A: ").split()]
vectorB = [float(x) for x in input("Enter the elements for vector B: ").split()]
tempVal1 = tempVal2 = dotProduct = 0
sum = []
diff = []

#magnigude of vectors (sqrt of sum of each element squared)]
for i in range(len(vectorA)):
    tempVal1 += vectorA[i] ** 2
    tempVal2 += vectorB[i] ** 2
magA = sqrt(tempVal1)
magB = sqrt(tempVal2)
print(f'The magnitude of vector A is {magA:.5f}')
print(f'The magnitude of vector B is {magB:.5f}')

#calculating sum and difference and dotproduct of vectors
for i in range(len(vectorA)):
    sum.append(float(vectorA[i] + vectorB[i]))
    diff.append(float(vectorA[i] - vectorB[i]))
    dotProduct += vectorA[i] * vectorB[i]

#printing values
print(f'A + B is [', end='')
for i in range(len(sum)):
    if sum[i] * 10 % 1 != 0:
        print(f'{sum[i]:.2f}', end='')
    else:
        print(f'{sum[i]:.1f}', end='')
    if i != len(sum) - 1:
        print(f', ', end='')
print(f']')

print(f'A - B is [', end='')
for i in range(len(diff)):
    if diff[i] * 10 % 1 != 0:
        print(f'{diff[i]:.2f}', end='')
    else:
        print(f'{diff[i]:.1f}', end='')
    if i != len(diff) - 1:
        print(f', ', end='')
print(f']')

print(f'The dot product is {dotProduct:.2f}')