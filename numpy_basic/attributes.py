import numpy as np


#Dimentions
a = np.array(([6,7],[1,2],[1,2]))

print(a.ndim)

#Shape
print(a.shape)

a = np.zeros((2,3,4))

print("Dimention = ",a.ndim,"\nShape =",a.shape)

#Size ( no. of elements in the array)
# or multiplications of shape digits

print(a.size)

#Dtype

print(a.dtype)

#itemSize (give the bytes of the elements)
#float64 = 64/8 = 8 and int32 = 32/8 = 4

print(a.itemsize)
