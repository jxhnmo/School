# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   1.11 LAB: Print math
# Date:         8/27/2022
#

"""
Author: John Mo
UIN: 432008972
Class: ENGR 102 599
Professor: Galina Tsvetkova
Project: 1.11 LAB: Print math
"""

#imports
import math

#calculations
f = 3 * 5.5
w = 0.025 * 2 * math.sin(math.radians(25))
r = 5 * math.pow(2, (-3/3.8))
p = (5 * 8.314 * 415)/(0.25 * 1000)

#printing
print(f"Force is {f} N")
print(f"Wavelength is {w} nm")
print(f"Radon-222 left is {r} g")
print(f"Pressure is {p} kPa")