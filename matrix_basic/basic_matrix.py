import numpy as np
#matrix addition same as array
#matrix multiplication
a = np.arange(1,5).reshape(2,2)
b= np.arange(1,5).reshape(2,2)
c = np.dot(a,b)
print(c)
print(a.dot(b))#same

#transpose same as array