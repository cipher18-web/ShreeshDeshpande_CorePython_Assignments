# acessing elements from an 2d array

import numpy as np
data=[
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]
mat=np.array(data)
print(f"""
{mat[0,1]}
{mat[1,2]}
{mat[2,0]}""")