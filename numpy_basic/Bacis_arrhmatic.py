import numpy as np 
arr = np.array([[1,2,3],[4,5,6]])

#basic single digit operstions

print(arr+5)

#Array to array operation
#array must be of same shape
arr2= np.array([[10,11,12],[10,11,12]])

print(arr+arr2)

#or you can use

a = np.add(arr,10)
print(a)

#np.add(a,b)
#np.subtract(a,b)
#np.divide(a,b)
#np.multiply(a,b)
#np.mod(a,b)
#etc.(1 or 2)