# updating an array (used fancy indexing)

import numpy as np
arr=np.arange(10,51,10)
print(f"Original Array: {arr}")
arr[[1,-1]]=25,55
print(f"Updated Array: {arr}")