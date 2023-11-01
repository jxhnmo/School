# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.12 LAB:  Python Program to Print Largest Even and Largest Odd Number in a List
# Date:         10/18/2022
#

#creating list of numbers
numList = [4, 2, 3, 6, 10, 3, 12, 3, 66, 5]
evens = []
odds = []

for i in range(len(numList)):
    if (numList[i] % 2) == 0:
        evens.append(numList[i])
    else:
        odds.append(numList[i])

print(f'Original List: {numList}\nLargest Even: {max(evens)}\nLargest Odd: {max(odds)}')