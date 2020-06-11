# Import necessary modules
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


boston = datasets.load_boston()


# Create feature and target arrays
X = boston.data
y = boston.target
X_rooms = X[:,5]

y=y.reshape(-1,1)
X_rooms = X_rooms.reshape(-1,1)


sns.set()
plt.scatter(X_rooms,y)
plt.ylabel('value of house/ 1000 ($)')
plt.xlabel('Number of rooms')


reg = linear_model.LinearRegression()

reg.fit(X_rooms,y)

prediction_space = np.linspace(min(X_rooms),max(X_rooms)).reshape(-1,1)

plt.plot(prediction_space,reg.predict(prediction_space),color='black', linewidth=3)
plt.show()