import numpy as np
a = np.array([[1,2],[3,4]])
b= np.transpose(a)
print(b)
c = a.transpose()
print(c)
#transpose will rearrange the dimention in the reverse order

arr = np.arange(1,25).reshape(2,3,4)
print(arr.transpose().shape)#4,3,2
#using axis
arr = np.arange(1,25).reshape(2,3,4)
'''
here, 0 axis :: 2
      1 axis :: 3
      2 axis :: 4
      by using axis we generally transpose it in our fav. direction
'''
arr0 = np.transpose(arr,axes=(1,0,2))
print(arr.shape)

#Swapaxes

swap = np.arange(1,5).reshape(2,2)
print(swap)
#swapping axes
swap0 = np.swapaxes(swap,0,1)
print(swap0)
#or 
#ndarray.swapaxes(axes1,axes2)
#3-d

swap = np.arange(1,25).reshape(2,3,4)
print("\n\n",swap)
swap1 = np.swapaxes(swap,1,2)
print(swap1)