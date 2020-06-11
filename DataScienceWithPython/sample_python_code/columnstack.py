import numpy as np
store = np.array([4, 5, 5, 3, 2, 5])
cost  = np.array([60, 67, 89, 68, 80, 80])
np_cols = np.column_stack((store, cost))

print(np_cols)