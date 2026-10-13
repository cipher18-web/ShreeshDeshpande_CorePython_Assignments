#mini calulator

import numpy as np

get_array = lambda msg: np.array(input(msg).split(), dtype=int)

array1 = get_array("Enter Array 1: ")
array2 = get_array("Enter Array 2: ")

print(f"addition:{np.add(array1, array2)}")
print(f"subtraction:{np.subtract(array1, array2)}")
print(f"multiplication:{np.multiply(array1, array2)}")
print(f"division:{np.divide(array1, array2)}")
