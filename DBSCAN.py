from sklearn.cluster import DBSCAN

model = DBSCAN(eps=2, min_samples=2)

labels = model.fit_predict(X)

print(labels)