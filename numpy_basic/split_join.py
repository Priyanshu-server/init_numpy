import numpy as np
a = np.arange(1,6)
b = np.arange(6,11)
c = np.zeros((10))
#out we can use for send the output to another array
np.concatenate((a,b),out=c)
print(c)

#2-d(dim should be same)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

c = np.concatenate((a,b),axis = 0)
print(c)
b = b.T
c = np.concatenate((a,b),axis = 1)
print("\n\n",c)
'''   for axis =0
     a = (2,2)
     b = (1,2)
     we dont need to watch for the axis at whixh we are concatenating we need to see another axis
     
     for axis = 1
     a = (2,2)
     b= (2,1)
'''
# np.vstack((a,b))  it is for axis 0
#for 1-d array it convert it in 2d
a = np.arange(1,6)
b = np.arange(1,6)

c = np.vstack((a,b))
print(c)

# np.hstack((a,b))  for axis 1
#it is same as concatenate 

#split

arr = np.arange(1,11)
arr = np.split(arr,2)
print(arr)

arr0 = np.array([[1,2,3,4],[5,6,7,8]])
arr1=np.split(arr0,2,axis = 1)
print(arr1)
arr2= np.split(arr0,2,axis=0)
print(arr2)
#np.hsplit(array,section)
#np.vsplit(array,section)