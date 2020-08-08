import numpy as np
a = np.arange(1,11).reshape(2,5)
print(a)
#numpy.insert(array,index,element,axis)
#it will flatten the array
b = np.insert(a,2,12)
print(b)
#inserting without flatting
c = np.insert(a,2,12,axis=0)
print(c)
# you can use append
# np.append(array,value,axis)
d = np.append(a,[[10,20,30,40,50]],axis=0)
'''
NOTE -if appending then you need to enter the value in shape but in inserting don't worry about it'''

#Delete

a = np.array([[1,2],[3,4]])
a = np.delete(a,1,axis=0) #delete the 1st index
#without axis it flatten the array
print(a)