#add

import numpy as np

array1 = np.array(input("Enter Array 1 (10 numbers): ").split(), dtype=int)
array2 = np.array(input("Enter Array 2 (10 numbers): ").split(), dtype=int)
print("Result:", array1 + array2)