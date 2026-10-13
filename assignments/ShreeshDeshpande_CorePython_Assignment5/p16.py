#converting a array into a matrix

import numpy as np

array = np.arange(1, 13)

rarray = array.reshape(3, 4)

print(f"Original:{array}")
print(f"""Reshaped:
{rarray}""")
