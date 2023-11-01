# imports
import numpy as np
import matplotlib.pyplot as plt

'''
with open('data.txt', 'r+') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split()
        print(line)
'''
'''
mydict = {'Apple' : 3, 'Pear' : 5, 'Banana' : 2}
mydict['boobs'] = 5
print(*mydict.items())
vector1 = (1, 2, 3)
vector2 = (2, 3, 4)
dotp = np.dot(vector1, vector2)
print("The dot product is", dotp)'''
x = np.linspace(-2, 2, 25)
y1 = x
y2 = x ** 2
plt.plot(x, y1, 'g', linewidth = 3)
plt.plot(x, y2, 'k', marker = 'o', markerfacecolor = 'b')
plt.axis([-2, 2, -2, 4])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plots for 2 polynomials')
plt.legend(['straight', 'curved'], loc = 'lower right')
plt.show()
print(x)