from sklearn.decomposition import PCA

model = PCA(n_components=2)

X_reduced = model.fit_transform(X)

print(X_reduced)