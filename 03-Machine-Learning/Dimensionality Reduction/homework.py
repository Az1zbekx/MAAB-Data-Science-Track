import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import accuracy_score

data = load_breast_cancer()

X = data.data
y = data.target

print("Dataset shape:", X.shape)
print("Number of features:", X.shape[1])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

start = time.time()

model = LogisticRegression(max_iter=10000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

end = time.time()

print("\nWithout Scaling")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Training Time:", end - start)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

start = time.time()

scaled_model = LogisticRegression(max_iter=10000)

scaled_model.fit(X_train_scaled, y_train)

y_pred_scaled = scaled_model.predict(X_test_scaled)

end = time.time()

print("\nWith StandardScaler")
print("Accuracy:", accuracy_score(y_test, y_pred_scaled))
print("Training Time:", end - start)

print("\nPCA requires standardized features because features with larger scales dominate variance calculations.")

pca_2 = PCA(n_components=2)

X_pca = pca_2.fit_transform(X_train_scaled)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(
    X_train_scaled[:, 0],
    X_train_scaled[:, 1],
    c=y_train,
    cmap="viridis"
)
plt.title("Original Features")

plt.subplot(1, 2, 2)
plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y_train,
    cmap="viridis"
)
plt.title("PCA Components")

plt.show()

X_centered = X_train_scaled - np.mean(X_train_scaled, axis=0)

cov_matrix = np.cov(X_centered.T)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

sorted_index = np.argsort(eigenvalues)[::-1]

sorted_vectors = eigenvectors[:, sorted_index]

manual_pca = np.dot(X_centered, sorted_vectors[:, :2])

plt.figure(figsize=(6, 5))

plt.scatter(
    manual_pca[:, 0],
    manual_pca[:, 1],
    c=y_train,
    cmap="viridis"
)

plt.title("Manual PCA")
plt.show()

pca_full = PCA(n_components=None)

pca_full.fit(X_train_scaled)

explained_variance = pca_full.explained_variance_ratio_

cumulative_variance = np.cumsum(explained_variance)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(explained_variance, marker="o")
plt.title("Explained Variance Ratio")

plt.subplot(1, 2, 2)
plt.plot(cumulative_variance, marker="o")
plt.axhline(y=0.90, color="r", linestyle="--")
plt.title("Cumulative Explained Variance")

plt.show()

n_components_90 = np.argmax(cumulative_variance >= 0.90) + 1

print("\nComponents for 90% variance:", n_components_90)

print("\nExplained variance helps select the smallest number of components while preserving most information.")

pca_90 = PCA(n_components=n_components_90)

X_train_pca = pca_90.fit_transform(X_train_scaled)
X_test_pca = pca_90.transform(X_test_scaled)

start = time.time()

pca_model = LogisticRegression(max_iter=10000)

pca_model.fit(X_train_pca, y_train)

y_pred_pca = pca_model.predict(X_test_pca)

end = time.time()

print("\nPCA Model")
print("Accuracy:", accuracy_score(y_test, y_pred_pca))
print("Training Time:", end - start)

print("\nDimensionality reduction improves efficiency and reduces complexity but may slightly reduce accuracy.")

tsne = TSNE(
    n_components=2,
    random_state=42,
    perplexity=30
)

X_tsne = tsne.fit_transform(X_train_scaled)

plt.figure(figsize=(6, 5))

plt.scatter(
    X_tsne[:, 0],
    X_tsne[:, 1],
    c=y_train,
    cmap="viridis"
)

plt.title("t-SNE Visualization")
plt.show()

print("\nt-SNE captures non-linear structures better than PCA, while PCA preserves global variance structure.")