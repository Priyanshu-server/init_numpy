#Broadcasting

import numpy as np
arr0 = np.array([[1,2],[3,4],[5,6]])
arr1 = np.array([5,10])

'''
as arrp having shape(3,2) and arr1 having (2,) so left side of it srreched out as (1,2) now 
(3,2)
(1,2)
so if dimention did'nt match then there should be at least 1 in anyside
so 1 is there in (1,2) so we can add them-->
'''
print(arr0+arr1)

'''
or you can add (1,3) to (3,1) because both having 1
'''
arr4 = np.array([[1],[2],[3]])
arr5 = np.array([1,2,3])
print(arr4.shape,arr5.shape)
print(arr4+arr5)