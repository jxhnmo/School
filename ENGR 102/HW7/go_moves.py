# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo, Kate Kroeger, Sophie Schneider, Maria Mercado
# Section:      599
# Assignment:   7.1 LAB: go moves
# Date:         10/12/2022
#

#import
from math import *

#declaring row
row = [
    ['●','●','●','●','●','●','●','●','●'],
    ['●','●','●','●','●','●','●','●','●'],
    ['●','●','●','●','●','●','●','●','●'],
    ['●','●','●','●','●','●','●','●','●'],
    ['●','●','●','●','●','●','●','●','●'],
    ['●','●','●','●','●','●','●','●','●'],
    ['●','●','●','●','●','●','●','●','●'],
    ['●','●','●','●','●','●','●','●','●'],
    ['●','●','●','●','●','●','●','●','●']
]
count = 0

print("Go Game\nInstructions:\nAttempt to fill all spcaes with players letter. Black is O and white is o.\nChoose position for piece through x and y coordinates.\nStart:")
print(" 1,2,3,4,5,6,7,8,9")
for i in range(0,9):
    print(i + 1, end='')
    for j in range(0,9):
        print(f'{row[i][j]} ', end='')
    print()

print(f'Black goes first')

while row.count('O') + row.count('o') != 81:
    if count % 2 == 0:
        if count != 0: print(f'Black goes next')
        x = int(input("x value position: "))
        y = int(input("y value position: "))

        if row[y - 1][x - 1] == 'o':
            print(f'That space already has a white piece! Try again.')
            count -= 1
        else:
            row[y - 1][x - 1] = 'O'
    else:
        print(f'White goes next')
        x = int(input("x value position: "))
        y = int(input("y value position: "))

        if row[y - 1][x - 1] == 'O':
            print(f'That space already has a black piece! Try again.')
            count -= 1
        else:
            row[y - 1][x - 1] = 'o'

    count += 1

    print(" 1,2,3,4,5,6,7,8,9")
    for i in range(0, 9):
        print(i+1,end='')
        for j in range(0, 9):
            print(f'{row[i][j]} ', end='')
        print()