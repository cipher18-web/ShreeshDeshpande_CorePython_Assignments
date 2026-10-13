# find min and max

import numpy as np

array = np.array(input("Enter 10 numbers separated by spaces: ").split(), dtype=int)

print(f"Array:   {array}")
print(f"Maximum: {np.max(array)}")
print(f"Minimum: {np.min(array)}")
