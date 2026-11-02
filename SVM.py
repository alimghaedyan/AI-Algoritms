from sklearn.svm import SVC

model = SVC(kernel="linear")

model.fit(X, y)

print(model.predict([[7]]))