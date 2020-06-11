# machine learning classifier to distinguish between apple and orange.
# features : weight in gm, skin texture ( bumpy(0),smooth(1)) 
# 0 for apple and 1 for orange 


from sklearn import tree

features=[[140,1],[130,1],[150,0],[170,0]]
labels=[0,0,1,1]
clf=tree.DecisionTreeClassifier()
clf1=clf.fit(features, labels)
print(clf1.predict([[160,0]]))