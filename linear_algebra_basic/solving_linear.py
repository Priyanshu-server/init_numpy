# solving matrix
import numpy as np
'''
3x + y = 9
x + 2y = 8
so the matrix will be
a = [ [3 , 1]
      [1 , 2]  ]
b = [[9,8]]
by solving it will return value of x and y

x = 2 and y = 3

a = np.linalg.solve(a,b)
'''
a = np.array([[3,1],[1,2]])
b = np.array([9,8])
c = np.linalg.solve(a,b)
print(c)