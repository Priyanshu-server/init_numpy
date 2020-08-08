import numpy as np
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#Indexing

print(arr[0][0][0])
print(arr[-1][0][0])

#Slicing
#array[start:end:step,start:end:step,.....]
print(arr[0][0][0:])
print(arr[0][0:])
print(arr[:1,:,1:])

#advance indexing
arr = np.arange(1,11)
print(arr)
index = np.array([2,4,6])
print(arr[index])
#or
print(arr[[2,4,6]])
#2-D
arr4 = np.array([[1,2],[3,4]])
print("\n\n",arr4)
# array[[rows],[cols]]
print(arr4[[0,1],[0,1]])


#Boolean indexing

arr5= np.array([[0,1],[0,2]])
print(arr5[arr5<2])
