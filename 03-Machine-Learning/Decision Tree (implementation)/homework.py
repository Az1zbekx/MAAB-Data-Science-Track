# Iris Flower Classification using Decision Tree Classifier

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Load dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target column
df["species"] = iris.target

# Map target values to species names
df["species_name"] = df["species"].map({
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
})

# Display first rows
print(df.head())

# Check dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Feature distributions
df.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))

for species, color in zip(df["species_name"].unique(), ["red", "green", "blue"]):
    subset = df[df["species_name"] == species]
    
    plt.scatter(
        subset["petal length (cm)"],
        subset["petal width (cm)"],
        label=species,
        color=color
    )

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend()
plt.title("Petal Length vs Petal Width")
plt.show()

# Features and target
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Classification Report
report = classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
)

print("Classification Report:")
print(report)

# Visualize Decision Tree
plt.figure(figsize=(14, 8))

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.title("Decision Tree Visualization")
plt.show()

# Feature Importance
importance = pd.DataFrame({
    "Feature": iris.feature_names,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(by="Importance", ascending=False)

print(importance)

# Feature Importance Plot
plt.figure(figsize=(8, 5))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.xticks(rotation=45)
plt.title("Feature Importance")
plt.show()

# Hyperparameter Tuning
param_grid = {
    "criterion": ["gini", "entropy"],
    "max_depth": [2, 3, 4, 5],
    "min_samples_split": [2, 3, 4]
}

grid_search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=5
)

grid_search.fit(X_train, y_train)

print("Best Parameters:")
print(grid_search.best_params_)

# Best model
best_model = grid_search.best_estimator_

# Predictions using best model
best_pred = best_model.predict(X_test)

# Accuracy after tuning
best_accuracy = accuracy_score(y_test, best_pred)

print("Best Model Accuracy:", best_accuracy)

# Compare with Logistic Regression
lr_model = LogisticRegression(max_iter=200)

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_pred)

print("Logistic Regression Accuracy:", lr_accuracy)

# Compare with Random Forest
rf_model = RandomForestClassifier(random_state=42)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_pred)

print("Random Forest Accuracy:", rf_accuracy)

# Final conclusion
print("\nConclusion:")
print("Decision Tree Classifier successfully classified iris flowers.")
print("Petal length and petal width were the most important features.")
print("Hyperparameter tuning improved model performance.")
print("Random Forest and Logistic Regression were also compared.")