# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.11 LAB: Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
# Date:         10/18/2022
#

#creating list of numbers
numList = [4, 2, 3, 6, 10, 3, 12, 3, 66, 5, -5, -3, -11]
evens, odds, negatives = 0, 0, 0

for i in range(len(numList)):
    if (numList[i] % 2) == 0:
        evens += numList[i]
    elif (numList[i] < 0):
        negatives += numList[i]
    else:
        odds += numList[i]

print(f'Original List: {numList}\nSum of Negatives: {negatives}\nSum of Evens: {evens}\nSum of Odds: {odds}')