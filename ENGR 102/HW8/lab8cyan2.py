# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.5 LAB: Python Program to Add a Key-Value Pair to the Dictionary
# Date:         10/18/2022
#

#declaring initial dictionaries
friendsAges = {"Adam": 19, "Bob": 20}
friendsAges2 = {"Kai": 23, "Cassie": 19}

#printing dictionary
print(f'Initial dictionaries has values:\n{friendsAges}\n{friendsAges2}\nNew dictionary concatenated with other now has values:')

#concatenating two dictionaries
friendsAges.update(friendsAges2)

#printing dictionary
print(friendsAges)