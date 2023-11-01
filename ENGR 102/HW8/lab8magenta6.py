# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.15 LAB:  Python Program to Find the Smallest Divisor of an Integer
# Date:         10/18/2022
#

#user input
n = int(input("Enter an integer: "))
divisors = []

#checking for divisors up to the number provided
for i in range(1, n + 1):
    if n %  i == 0:
        divisors.append(i)

#output
print(f'{divisors[1]} is the smallest divisor for the integer {n}')