import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



df = pd.read_csv('iris.csv')
df1= df.loc[df['species'] =='versicolor']
versicolor_petal_length = df1['petal_length']
versicolor_petal_width = df1['petal_width']

# Make a scatter plot
plt.plot(versicolor_petal_length,versicolor_petal_width,marker='.',linestyle='none')


# Set margins
plt.margins(0.02)

# Label the axes
_ = plt.xlabel('versicolor_petal_length')

_ = plt.ylabel('versicolor_petal_width')


# Show the result
plt.show()

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0,1]

# Print the length/width covariance
print(petal_cov)

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length,versicolor_petal_width)
# Print the result
print("The correlation Coefficient is {}". format(r))

