import numpy as np

#Change data type

a = np.array(([1,2]),dtype=np.int8)
print(a.dtype)

#delcaring a variable to np dataType

x = np.float32(1)
print(x)

y = np.array([1,2,3],'f')
print(y.ndim)

#changing dataType of array
y = y.astype(int)
print(y)

y = np.float32(y)
print(y)