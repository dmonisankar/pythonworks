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

df_set= df.loc[df['species'] =='setosa']
setosa_petal_length = df_set['petal_length']

df_vers= df.loc[df['species'] =='versicolor']
versicolor_petal_length = df_vers['petal_length']

df_virg= df.loc[df['species'] =='virginica']
virginica_petal_length = df_virg['petal_length']


# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)


# Generate plot
# Plot all ECDFs on the same plot
_=plt.plot(x_set, y_set, marker='.', linestyle='none')
_=plt.plot(x_vers, y_vers, marker='.', linestyle='none')
_=plt.plot(x_virg, y_virg, marker='.', linestyle='none')

# Make nice margins
plt.margins(0.02)

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()