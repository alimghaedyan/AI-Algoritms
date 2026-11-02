from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)

model.fit(X, y)

print(model.predict([[6000, 2500]]))