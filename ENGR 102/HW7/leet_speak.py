# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   Lab 7.2 Zybooks Lab 2 Leet Speak
# Date:         10/12/2022
#

#user input and initializing variables
original = input("Enter some text: ")
leetText = original

#dictionary for leet
dict={'a':'4','e':'3','o':'0','s':'5','t':'7'}

for key, value in dict.items():
    leetText = leetText.replace(key,value)

#output
print(f'In leet speak, "{original}" is: {leetText}')