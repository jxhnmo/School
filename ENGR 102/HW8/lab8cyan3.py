# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   8.6 LAB:  Python Program to Check if a Given Key Exists in a Dictionary or Not
# Date:         10/18/2022
#

#declaring initial dictionaries
friendsAges = {"Adam": 19, "Bob": 20, "Kai": 23, "Cassie": 19}

#printing dictionary
print(friendsAges)

#taking input and checking for person
name = input('Input a name to check for age: ')
if friendsAges.get(name) == None:
    print('Person not found.')
else:
    print(f'Person found. Their age is: {friendsAges[name]}')