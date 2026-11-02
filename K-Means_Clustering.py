from sklearn.cluster import KMeans

X = [
    [1000, 200],
    [1200, 300],
    [5000, 2000],
    [5500, 2500],
    [10000, 7000],
    [11000, 7500]
]

model = KMeans(n_clusters=3, random_state=42, n_init=10)

model.fit(X)

print(model.labels_)