# iris data

# Import numpy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('IRIS.csv')

print(df.head())


# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x='species', y='petal_length', data=df)



# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm')

# Show the plot
plt.show()
