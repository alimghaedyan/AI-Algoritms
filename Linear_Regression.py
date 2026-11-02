import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([100, 200, 300, 400, 500])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)