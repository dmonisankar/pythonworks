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
	
df = pd.read_csv('iris.csv')
df1= df.loc[df['species'] =='versicolor']
versicolor_petal_length = df1['petal_length']

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_=plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# Make the margins nice

plt.margins(0.02)
# Label the axes
_ = plt.xlabel('veriscolor petal length')
_= plt.ylabel('ECDF')


# Display the plot
plt.show()
