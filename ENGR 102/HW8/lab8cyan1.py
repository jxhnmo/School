# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.4 LAB: Python Program to Add a Key-Value Pair to the Dictionary
# Date:         10/18/2022
#

#declaring initial dictionary
friendsAges = {"Adam": 19, "Bob": 20}

#printing dictionary
print(friendsAges)

#receiving input for new key value pair
name, age = input("Input Name: "), input("Input Age: ")

#assigning value
friendsAges[name] = age

#printing dictionary
print(friendsAges)