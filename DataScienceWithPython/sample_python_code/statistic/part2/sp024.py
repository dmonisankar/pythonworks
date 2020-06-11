
# While bee swarm plots are useful, we found that ECDFs are often even better when doing EDA. Plot the ECDFs for the 1975 and 2012 beak depth measurements on the same plot.
# For your convenience, the beak depths for the respective years has been stored in the NumPy arrays bd_1975 and bd_2012.


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y
	
df = pd.read_csv('beak_finch.csv', header=0)

print(df.head())

sns.set()

bd_1975 = df['beak_depth'][(df['year']==1975)].tolist()
bd_2012 = df['beak_depth'][(df['year']==2012)].tolist()


# Compute ECDFs
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

# Plot the ECDFs
_ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
_ = plt.plot(x_2012, y_2012, marker='.', linestyle='none')

# Set margins
plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('beak depth (mm)')
_ = plt.ylabel('ECDF')
_ = plt.legend(('1975', '2012'), loc='lower right')

# Show the plot
plt.show()


# The differences are much clearer in the ECDF. The mean is larger in the 2012 data, and the variance does appear larger as well.