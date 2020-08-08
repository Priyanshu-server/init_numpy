import numpy as np

#no.allclose(array1,array2) true boolean value for equal array

#array

arr = np.array([1, 3, 3],dtype="complex",ndmin=3)
print(arr)
print("\n\n")

#arange (kind of range function)

aran = np.arange(0, 10, dtype="int")
print(aran)
print("\n\n")

#zeros

zero = np.zeros((2,4),dtype ="int")
print(zero)
print("\n\n")

#ones

one = np.ones((2,4),dtype="int")
print(one)
print("\n\n")

#linspace

lin = np.linspace(1, 10, num=10, endpoint=False, dtype="int", retstep="True",axis=0)
print(lin)
print("\n\n")


#eye (adds 1 in a Kth diagonal & all elemnts will be 0)

eye = np.eye(3, 5, k=1, dtype = "int")
print(eye)
print("\n\n")

#identity matrix using eye method

identity_eye = np.eye(3)
print(identity_eye)
print("\n\n")

#identity matrix using identity method

identity = np.identity(3, dtype ="int")
print(identity)
print("\n\n")

#Random function

#Rand --> [0,1)

rand = np.random.rand(3, 3)
print(rand)
print("\n\n")

#Randn --> Standard normal distribution

randn = np.random.randn(3,3)
print(randn)
print("\n\n")

#Ranf --> [0.0,1.0)

ranf = np.random.ranf(size=(5,5))
print(ranf)
print("\n\n")

#Randint --> (input by users)

randint  = np.random.randint(0, 10, size = (2,4))
print(randint)
print("\n\n")

#choice

arr = np.random.choice(range(20),(2,2),replace = False)
print(arr)

#for locking the data
np.random.seed(0)
#you need to call it everytime
'''
np.random.seed(0)
a = np.random.rand(3)
print(a)
np.random.seed(0)
print(np.random.rand(3))
'''