# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   7.4 LAB: Example 1 “Print multiplication table”
# Date:         10/12/2022
#

# 10 x 10 multiplication table
print("       1   2   3   4   5   6   7   8   9  10")
print('   +-----------------------------------------')
for row in range(1,11):
    if row < 10:
        print(' ', end='')
    print(row,'| ', end='')
    for column in range(1,11):
        product = row * column
        if product < 100:
            print(end=' ')
        if product < 10:
            print(end=' ')
        print(product, end=' ')
    print()

