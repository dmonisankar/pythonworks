import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


df = pd.read_csv('pima-input.csv')
print(df.head())



# Create arrays for the features and the target variable
y = df['I'].values
X = df.drop('I', axis=1).values



logreg = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)

logreg.fit(X_train,y_train)

y_pred = logreg.predict(X_test)

score = logreg.score(X_test,y_test)

print(score)


# Generate the confusion matrix and classification report
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))


