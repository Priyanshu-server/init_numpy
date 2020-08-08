import numpy as np
#determinant

a = np.arange(1,5).reshape(2,2)
b = np.linalg.det(a)
print(b,round(b),sep= "\n")
