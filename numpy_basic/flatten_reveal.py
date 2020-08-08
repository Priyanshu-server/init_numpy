import numpy as np
a = np.array([[1,2],[3,4]])
b = a.flatten()
print(b)
a = a.flatten(order ="F")
print(a)

#ravel
arr = np.array([[10,20],[30,40]])
arr0 = np.ravel(arr,order="C")
print(arr0)
#or
arr1 = arr.ravel()
print(arr1)

#to expand dima
a = np.arange(1,3)
n = a.copy()
np.expand_dims(a,0)
n = np.expand_dims(n,1)
print("",a,n,sep='\n\n')