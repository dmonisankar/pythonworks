# example of box plot


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



df = pd.read_csv('iris.csv')
# df1= df.loc[df['species'] =='versicolor']
# versicolor_petal_length = df1['petal_length']

_= sns.boxplot(x='species', y='petal_length', data=df)

_ = plt.xlabel('species')

_ = plt.ylabel('petal length')

plt.show()