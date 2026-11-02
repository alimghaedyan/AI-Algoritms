from sklearn.tree import DecisionTreeClassifier

X = [
    [5000, 2000],
    [3000, 3500],
    [8000, 3000],
    [2000, 4000]
]

y = [1, 0, 1, 0]

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[6000, 2500]]))