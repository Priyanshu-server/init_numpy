import numpy as np
a = np.arange(1,5).reshape(2,2)
print(" Array a is :: \n",a)
b = np.linalg.inv(a)
print("\nInverse of a is :: \n",b)

#numpy.linalg.inv(array)
c = np.dot(a,b)
print("\n\na * b is :: \n", c)

#np.allclose give boolen value for equality
print(np.allclose(a,np.linalg.inv(b)))
#check the dot of matrix is euqal to identity
print("\n\n",np.allclose(c,np.identity(2)))
'''
NOTE - if u give 3d array to inv then it will treat it like a 2 2-D array and calculate for both
'''