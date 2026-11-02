from sklearn.linear_model import LogisticRegression

X = [
    [1], [2], [3], [7], [8], [9]
]

y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[8]]))