import numpy as np

a = np.array([1,2])

np.set_printoptions(legacy= '1.13')
print(a)
b = np.array([1.38282828,2.8282829])
np.set_printoptions(precision= 2)
print(b)

y=np.array([1.5e-10,1.5,1500])
print(y)
# [  1.500e-10   1.500e+00   1.500e+03]
np.set_printoptions(suppress=True)
print(y)
# [    0.      1.5  1500. ]

x = np.random.random(10)
with np.printoptions(precision=3, suppress=True):
    print(x)
    
    
    
#or you can use array_str
help(np.array_str)
a = np.random.rand(10)
print(a)
a = np.array_str(a,precision = 2)
print(a)