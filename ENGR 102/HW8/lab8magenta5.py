# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.14 LAB: Python Program to Find the Area of a Triangle Given All Three Sides
# Date:         10/18/2022
#

#import
from math import *

#user input
side1 = int(input("Input side 1 length: "))
side2 = int(input("Input side 2 length: "))
side3 = int(input("Input side 3 length: "))

#calculating area based on herons formula
p = (side1 + side2 + side3) / 2
area = sqrt(p * (p - side1) * (p - side2) * (p - side3))

#printing
print(f'Area of triangle with sides of {side1}, {side2}, and {side3} is {area}u^2')