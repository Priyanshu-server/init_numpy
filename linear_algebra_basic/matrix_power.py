import numpy as np

#power of matrix 
#np.linalg.power_matrix(array,power)
a = np.arange(1,5).reshape(2,2)
b = np.linalg.matrix_power(a,2)
print(b)
# here b is simple a^2 means a.a
# so a.dot(a) should be equal to b

print(np.array_equal(a.dot(a),b))

#if power is 0 then it will give identity array

c = np.linalg.matrix_power(a,0)
print(c)

#if power is -ve then it will first inverse it and then find the result

d = np.linalg.matrix_power(a,-2)
print("\n\n",d)

print(np.allclose(d,np.dot(np.linalg.inv(a),np.linalg.inv(a))))

#inverse of array can be find by np.linalg.inv(array)
print(np.allclose(np.linalg.matrix_power(a,-1),np.linalg.inv(a)))