#reshape
#you can use -1 in reshape to enter remoaing automatically
import numpy as np
a= np.arange(10)
print(a)
#default order is c
b = np.reshape(a,(5,2))
print(b,"\n\n",b.shape,"\n\n")

#now , we will take elements column wise
c= np.reshape(a,(5,2),order="F")
print(c,"\n\n",c.shape)

#or
d = a.reshape((5,2),order="F")
print(d,"\n\n")

#Resize
#we don't want to count the elements and reshaoe them accordingly
#we can take any no. of elemnts or shape they automatically adjusted

#array is repated
arr = np.array([1,2,3,4,5])
b = np.resize(arr,(3,2))
print(b)
#or 0 is repeated
arr.resize((3,3))
print(arr)