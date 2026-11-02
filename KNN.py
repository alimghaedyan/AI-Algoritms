from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [3], [8], [9], [10]]
y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print(model.predict([[7]]))