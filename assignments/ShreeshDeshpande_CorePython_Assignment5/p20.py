#numpy functions

import numpy as np

marks = np.array([78, 65, 89, 92, 56, 74, 81, 69, 95, 72])

print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Total Marks:", np.sum(marks))
print("Students Above 75:", np.sum(marks > 75))
