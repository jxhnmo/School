# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   7.4 LAB: Example 2 “Permutation of ABC”
# Date:         10/12/2022
#

for first in 'ABC':
    for second in 'ABC':
        if second != first:
            for third in 'ABC':
                if third != first and third != second:
                    print(first + second + third)