# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   11.2 LAB: count coins
# Date:         11/13/2022
#

#declaring variables
coins = 0
coins_1st = []
output = ''

with open('game.txt','r') as f: #opening the file
    words = f.readlines() #reading the file
    i = 0
    while i < len(words):
        data = words[i].split()
        instruction = data[0]
        number = int(data[1])

        if instruction == 'coin':
            coins += number
            coins_1st.append(number)
            output += str(number) + '\n'
            i += 1
        elif instruction == 'jump':
            i += number
        else:
            i += 1

output = output[:-1]
fileName2 = 'coins.txt'
fileOut = open(fileName2, 'w')
fileOut.write(output)

#print statement
print('Total coins collected:', coins)