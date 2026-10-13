#concatenate a array

import numpy as np

array1 = np.array([10, 20, 30])
array2 = np.array([40, 50, 60])

combined_array = np.concatenate((array1, array2))
print(f"Array 1: {array1}")
print(f"Array 2: {array2}")
print(f"Combined Array: {combined_array}")
