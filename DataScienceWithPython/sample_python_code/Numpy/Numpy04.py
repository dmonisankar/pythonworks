import numpy as np
x = np.array([6, 5, 4, 6, 7, 5, 6, 4])
y = np.array([6, 9, 9, 4, 0, 9, 9, 6])

print(np.corrcoef(x, y))