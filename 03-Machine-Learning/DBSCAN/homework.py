import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

iris = load_iris()

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)

print(df.head())

print(df.shape)

print(df.describe())

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_visual = X_scaled[:, :2]

eps_values = [0.2, 0.3, 0.5, 0.7]

min_samples_values = [3, 5, 8]

results = []

for eps in eps_values:
    for min_samples in min_samples_values:

        dbscan = DBSCAN(
            eps=eps,
            min_samples=min_samples
        )

        dbscan.fit(X_scaled)

        labels = dbscan.labels_

        n_clusters = len(
            set(labels)
        ) - (1 if -1 in labels else 0)

        noise_points = np.sum(labels == -1)

        print("\n=========================")
        print(f"eps = {eps}")
        print(f"min_samples = {min_samples}")

        print("Labels:")
        print(labels)

        print("Number of clusters:")
        print(n_clusters)

        print("Noise points:")
        print(noise_points)

        if n_clusters > 1:
            score = silhouette_score(
                X_scaled,
                labels
            )
        else:
            score = -1

        results.append({
            "eps": eps,
            "min_samples": min_samples,
            "clusters": n_clusters,
            "noise_points": noise_points,
            "silhouette_score": score
        })

results_df = pd.DataFrame(results)

print("\nDBSCAN Results Summary")

print(results_df)

best_result = results_df.sort_values(
    by="silhouette_score",
    ascending=False
).iloc[0]

print("\nBest Configuration")

print(best_result)

best_dbscan = DBSCAN(
    eps=best_result["eps"],
    min_samples=int(best_result["min_samples"])
)

best_dbscan.fit(X_scaled)

best_labels = best_dbscan.labels_

unique_labels = np.unique(best_labels)

plt.figure(figsize=(10, 7))

for label in unique_labels:

    if label == -1:
        color = "black"
        label_name = "Noise"
    else:
        color = None
        label_name = f"Cluster {label}"

    plt.scatter(
        X_visual[best_labels == label, 0],
        X_visual[best_labels == label, 1],
        c=color,
        label=label_name
    )

plt.xlabel("Feature 1")

plt.ylabel("Feature 2")

plt.title("DBSCAN Clustering")

plt.legend()

plt.show()

kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

kmeans.fit(X_scaled)

kmeans_labels = kmeans.labels_

plt.figure(figsize=(10, 7))

plt.scatter(
    X_visual[:, 0],
    X_visual[:, 1],
    c=kmeans_labels
)

plt.xlabel("Feature 1")

plt.ylabel("Feature 2")

plt.title("KMeans Clustering")

plt.show()

kmeans_score = silhouette_score(
    X_scaled,
    kmeans_labels
)

print("\nKMeans Silhouette Score")

print(kmeans_score)

print("\nAnalysis")

print(
    "1. Smaller eps values create tighter clusters and increase noise points."
)

print(
    "2. Larger eps values merge nearby clusters and reduce noise."
)

print(
    "3. Higher min_samples values make DBSCAN stricter and increase noise detection."
)

print(
    "4. Lower min_samples values create more clusters with fewer noise points."
)

print(
    "5. DBSCAN can detect irregular cluster shapes and identify outliers."
)

print(
    "6. KMeans assumes spherical clusters and cannot detect noise points."
)

print(
    "7. DBSCAN performed better when clusters had varying density and non-linear structure."
)

print(
    "8. KMeans produced fixed cluster assignments even for potential outliers."
)