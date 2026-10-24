import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

class KMeans:
    def __init__(self, n_clusters, max_iter=300, tol=1e-4, random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state

    def fit(self, X):
        np.random.seed(self.random_state)

        random_idx = np.random.choice(X.shape[0], self.n_clusters, replace=False)
        centroids = X[random_idx]

        for i in range(self.max_iter):
            distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
            labels = np.argmin(distances, axis=1)

            new_centroids = np.array([
                X[labels == k].mean(axis=0)
                for k in range(self.n_clusters)
            ])

            shift = np.linalg.norm(new_centroids - centroids)

            centroids = new_centroids

            if shift < self.tol:
                break

        self.cluster_centers_ = centroids
        self.labels_ = labels
        self.inertia_ = np.sum(
            (X - centroids[labels]) ** 2
        )
        self.n_iter_ = i + 1

        return self

    def predict(self, X):
        distances = np.linalg.norm(
            X[:, np.newaxis] - self.cluster_centers_,
            axis=2
        )
        return np.argmin(distances, axis=1)

    def fit_predict(self, X):
        self.fit(X)
        return self.labels_

data = load_iris()
X = data.data[:, :2]

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

print(kmeans.cluster_centers_)
print(kmeans.inertia_)
print(kmeans.n_iter_)

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=kmeans.labels_,
    cmap='viridis'
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=300,
    c='red',
    marker='X'
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("KMeans Clustering")
plt.show()