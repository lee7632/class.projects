# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 21:13:39 2018

@author: jlee
"""

import numpy as np
import matplotlib.pyplot as plt


# Import data:

with open('meshtal') as f:
    content = f.readlines()

print content[18]
# ++ coordinate
x = []
y = []

for i in range(0, 100):
    x.append(float(content[18].split()[i]))
    y.append(float(content[18].split()[i]))
#print x, len(x)
#print y, len(y)


z = []

for l in range(19, 119):
    temp = []
    
    for k in range(0, 101):
        temp.append(float(content[l].split()[k]))
    temp.remove(temp[0]) 
    
    for i in range(0, 100):
        z.append(temp[i])


for i in range(0, 10000):
    z[i] = float(z[i])*2.43/200/1.6/(10**(-13))*(10**6)*5
#print z, len(z)


# -+ coordinate

x1 = []
y1 = []

for i in range(0, 100):
    y1.append(y[i])
    if x[i] >= 0:
        x1.append(-x[i])
    
#print x1
#print y1

# -- coordinate 

x2 = []
y2= []

for i in range(0, 100):
    if x[i] >= 0:
        x2.append(-x[i])
    if y[i] >= 0:
        y2.append(-y[i])
        
# +- coordinate 

x3 = []
y3 = []

for i in range(0, 100):
    x3.append(y[i])
    if y[i] >= 0:
        y3.append(-y[i])
    



# color plot python
X, Y = np.meshgrid(x,y)
z = np.array(z)
grid = z.reshape((100, 100))
#print grid

X1, Y1 = np.meshgrid(x1, y1)
X2, Y2 = np.meshgrid(x2, y2)
X3, Y3 = np.meshgrid(x3, y3)


plt.figure(figsize=(6,5))
plt.pcolormesh(X,Y, grid)
plt.pcolormesh(X1, Y1, grid)
plt.pcolormesh(X2, Y2, grid)
plt.pcolormesh(X3, Y3, grid)
plt.colorbar()



plt.show()


