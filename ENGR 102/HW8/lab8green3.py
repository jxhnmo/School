# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.3 LAB: Python Program to Calculate the Length of a String Without Using a Library Function
# Date:         10/19/2022
#

#user input
string = input("Input a string: ")
count = 0

#finding how many characters there are in string
for i in string:
    count += 1

#output
print(f'There are {count} characters in the string "{string}"')