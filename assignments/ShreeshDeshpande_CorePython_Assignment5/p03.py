#print data types in numpy

import numpy as np
x=[12,33,53,64,74,45]
y=[12.43,35.45,54.3,18.1]
x=np.array(x)
y=np.array(y)
print(f"integer array: {x.dtype}")
print(f"decimal array :{y.dtype}")