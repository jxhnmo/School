# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   1.12 LAB: Follow directions
# Date:         8/27/2022
#

#import
import math

#printing
print("This shows the evaluation of (x^2-1)/(x-1) evaluated close to x=1")
print("My guess is 2")

print((math.pow(1.1,2) - 1)/(1.1 - 1))
print((math.pow(1.01,2) - 1)/(1.01 - 1))
print((math.pow(1.001,2) - 1)/(1.001 - 1))
print((math.pow(1.0001,2) - 1)/(1.0001 - 1))
print((math.pow(1.00001,2) - 1)/(1.00001 - 1))
print((math.pow(1.000001,2) - 1)/(1.000001 - 1))
print((math.pow(1.0000001,2) - 1)/(1.0000001 - 1))
print((math.pow(1.00000001,2) - 1)/(1.00000001 - 1))

print("\nmy guess was perfect")