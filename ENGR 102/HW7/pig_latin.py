# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   Lab 7.1 Pig Latin
# Date:         10/12/2022
#

#user input
string = input('Enter word(s) to convert to Pig Latin: ')
words = string.split()

for i, word in enumerate(words):
#if first letter is a vowel
    if word[0] in 'aeiouy':
        words[i] = words[i] + "yay"
    else:
#if it doesnt start with a vowel
        vowel = False
        for j, letter in enumerate(word):
            if letter in 'aeiouy':
                words[i] = word[j:] + word[:j] + "ay"
                vowel = True
                break

        if vowel == False:
            words[i] = words[i]+ "ay"
final = ''.join(words)

#output
print("In Pig Latin,",  f'"{string}"' " is: ",  final)