# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.8 LAB:  Python Program to Find the Second Largest Number in a List
# Date:         10/18/2022
#

#creating list of numbers
numList = [4, 2 ,3, 6, 10, 3, 12, 3, 66, 5]

#finding max
firstMax = max(numList)

numList.remove(firstMax)

secondMax = max(numList)

numList.append(firstMax)

#printing max
print(f'Second largest number in list {numList} is {secondMax}')
