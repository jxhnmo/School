# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   7.2 LAB: Problem 2 Repeating Word
# Date:         10/12/2022
#

#user input
user = input("Would you like to create a list that repeats itself n times? (Yes/No): ")

#check if user wants to create repeated phrase
if user == "Yes":
    #user input
    word = input("Input word to be repeated: ")
    amount = int(input("Input times to be repeated: "))
    #print phrase n times
    print(word * amount)