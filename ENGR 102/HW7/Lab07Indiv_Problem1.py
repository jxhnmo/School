# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   7.1 LAB: Problem 1 Repeating Number Lists
# Date:         10/12/2022
#

#initializing vars
listGeneration = 'Yes'
count = 0
list = []
tempList = []

while listGeneration != 'No':
    #user input
    x = int(input("Input minimum value in list: "))
    y = int(input("Input maximum value in list: "))
    z = int(input("Input step value in list: "))

    #appending user input into temp list
    tempList.append(x)
    tempList.append(y)
    tempList.append(z)

    #generating values and appending into temp list
    for j in range(tempList[0], tempList[1] + 1, tempList[2]):
        tempList.append(j)

    #appending temp list into list and checking if user wants to create more lists
    list.append(tempList)
    listGeneration = input("Do you wish to make more lists? (Yes/No)")
    count += 1

#output
print("Lists you made:")
for i in range(0, count):
    print(f'List {i + 1}:\nMin Value: {list[i][0]}   Max Value: {list[i][1]}   Step Value: {list[i][2]}')
    for j in range(3, len(list[i])):
        print(f'{list[i][j]}', end='')
        if j != len(list[i]) - 1:
            print(f', ', end='')
    print()