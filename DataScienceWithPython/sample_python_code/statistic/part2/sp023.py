import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('beak_finch.csv')

print(df.head())

sns.set()

# Create bee swarm plot
_= sns.swarmplot(x='year', y='beak_depth', data=df)

# Label the axes
_ = plt.xlabel('year')
_ = plt.ylabel('beak depth (mm)')

# Show the plot
plt.show()