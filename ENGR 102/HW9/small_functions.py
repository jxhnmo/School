# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   9.1 LAB: small functions
# Date:         10/30/2022
#

# import
from math import *

# creating functions
def parta(sphere_radius, hole_radius):
    # full volume - hole volume
    bead_vol = (4 / 3) * pi * (sphere_radius ** 2 - hole_radius ** 2) ** (3 / 2)
    return bead_vol


def partb(n):
    if n % 4 == 2:
        return False
    numbers = []
    i = 1
    flag = False
    while not flag:
        j = i - 1
        while j >= 0:
            if ((i * i) - (j * j)) == n:
                for k in range(j + 1, i + 1):
                    numbers.append((2 * k) - 1)  # appending numbers into list
                flag = True
                break
            j -= 1
        i += 1
    if len(numbers) == 1:
        return False
    return numbers  # return list of numbers


def partc(char, name, univ, email):
    # finding longest line
    l = int(len(name))
    if len(name) < len(univ):
        l = int(len(univ))
    elif len(univ) < len(email):
        l = int(len(email))
    l += 6

    # return format
    return f"{char * l}\n{char}{name:^{l - 2}}{char}\n{char}{univ:^{l - 2}}{char}\n{char}{email:^{l - 2}}{char}\n{char * l}"


def partd(list):
    # numerical order
    list.sort()
    # max and minimum
    max = list[len(list) - 1]
    min = list[0]
    # median of even numbered list
    if len(list) % 2 == 0:
        median = (list[len(list) // 2 - 1] + list[len(list) // 2]) / 2
    else:
        median = list[len(list) // 2]
    return (min, median, max)


def parte(times, distances):
    v_list = []
    # finding velocities for each value
    for i in range(len(distances) - 1):
        velocity = (distances[i + 1] - distances[i]) / (times[i + 1] - times[i])
        v_list.append(velocity)
    # returning velocity list
    return v_list


def partf(list):
    # run through each item
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == 2026:
                # returning product of two numbers that add to 2026
                return list[i] * list[j]
    return False
# parta()


# print(partc('*', 'Dr. Ritchey', 'Texas A&M University', 'snritchey@tamu.edu'))
