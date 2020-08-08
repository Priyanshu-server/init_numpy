import numpy as np
#matrix class
a = np.matrix("1 2;3 4")
print(a)
#or
a = np.matrix([[1,2],[3,4]])
#matrix never be of 1- dimention
b = np.matrix("1 2")

# here * will multiply matrix no need to use dot()

a = np.matrix([[1,2],[3,4]])
b = np.matrix("10 20;30 40")
print("\n\n",a*b,"\n\n")
print(a.dot(b))

#if one is matrix and one is array then mulriplication act as matrix
#Ans result is also matrix
c = np.array([[10,20],[30,40]])
d = a*c
print(d)
d= d.flatten()
print(d)