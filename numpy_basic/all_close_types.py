import numpy as np

#isclose
#it return a boolen array for each element
a = np.array([[3,4],[1,2.]])
b = np.array([[1,5],[1,2]])
print(np.isclose(a,b))

#allclose
#it return for all elements
print(np.allclose(a,b))

#any

a = np.arange(1,5).reshape(2,2)
b = np.arange(1,5).reshape(2,2).astype('f')
print(np.allclose(a,b))
# if aaxis is not defines then any will give true if any of the axis element matched
result = a==b
print(np.any(result))
#all give true if the given axis or any axis's all element matched
print(np.all(result))

#np.array_equal return true if all element and shape equal
print("\n\n",np.array_equal(a,b))