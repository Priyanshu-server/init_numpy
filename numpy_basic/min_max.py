import numpy as np
a = np.random.choice(range(20),10,replace= False)
#min and max value
print(a.min(),a.max())

#min and max index
print(a.argmin(),a.argmax())