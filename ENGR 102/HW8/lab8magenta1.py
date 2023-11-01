# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.10 LAB:  Python Program to Generate all the Divisors of an Integer
# Date:         10/18/2022
#

#user input
number = int(input("Input an integer to find all possible divisors: "))
divisors = []

#checking for divisors up to the number provided
for i in range(1, number + 1):
    if number %  i == 0:
        divisors.append(i)

#output
print(f'{divisors} are all divisors for the integer {number}')