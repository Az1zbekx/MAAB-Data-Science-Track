# Boosting and Stacking - Binary Classification

# Import libraries
import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import StackingClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report

# Load Breast Cancer dataset
data = load_breast_cancer()

# Features and target
X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Feature scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =========================================================
# AdaBoost
# =========================================================

print("\n================ AdaBoost =================")

# Create model
ada_model = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=0.1,
    random_state=42
)

# Train model
ada_model.fit(X_train_scaled, y_train)

# Predictions
ada_train_pred = ada_model.predict(X_train_scaled)
ada_test_pred = ada_model.predict(X_test_scaled)

# Metrics
ada_train_acc = accuracy_score(y_train, ada_train_pred)
ada_test_acc = accuracy_score(y_test, ada_test_pred)

ada_train_f1 = f1_score(y_train, ada_train_pred)
ada_test_f1 = f1_score(y_test, ada_test_pred)

# Results
print("Train Accuracy:", ada_train_acc)
print("Test Accuracy:", ada_test_acc)

print("Train F1-score:", ada_train_f1)
print("Test F1-score:", ada_test_f1)

print("\nClassification Report:")
print(classification_report(y_test, ada_test_pred))

# =========================================================
# Gradient Boosting
# =========================================================

print("\n================ Gradient Boosting =================")

# Different experiments
experiments = [
    {
        "n_estimators": 50,
        "learning_rate": 0.1
    },
    {
        "n_estimators": 100,
        "learning_rate": 0.05
    },
    {
        "n_estimators": 200,
        "learning_rate": 0.01
    }
]

# Store results
results = []

# Run experiments
for exp in experiments:

    gb_model = GradientBoostingClassifier(
        n_estimators=exp["n_estimators"],
        learning_rate=exp["learning_rate"],
        random_state=42
    )

    # Train
    gb_model.fit(X_train_scaled, y_train)

    # Predict
    gb_pred = gb_model.predict(X_test_scaled)

    # Metrics
    acc = accuracy_score(y_test, gb_pred)
    f1 = f1_score(y_test, gb_pred)

    # Save results
    results.append({
        "n_estimators": exp["n_estimators"],
        "learning_rate": exp["learning_rate"],
        "accuracy": acc,
        "f1_score": f1
    })

# Convert results to DataFrame
results_df = pd.DataFrame(results)

print("\nGradient Boosting Results:")
print(results_df)

# =========================================================
# Stacking Classifier
# =========================================================

print("\n================ Stacking Classifier =================")

# Base models
base_models = [
    (
        "lr",
        LogisticRegression(max_iter=1000)
    ),
    (
        "dt",
        DecisionTreeClassifier(max_depth=5)
    ),
    (
        "knn",
        KNeighborsClassifier(n_neighbors=5)
    )
]

# Meta learner
meta_model = LogisticRegression(max_iter=1000)

# Stacking model
stack_model = StackingClassifier(
    estimators=base_models,
    final_estimator=meta_model
)

# Train model
stack_model.fit(X_train_scaled, y_train)

# Predictions
stack_pred = stack_model.predict(X_test_scaled)

# Probabilities for ROC-AUC
stack_prob = stack_model.predict_proba(X_test_scaled)[:, 1]

# Metrics
stack_acc = accuracy_score(y_test, stack_pred)

stack_auc = roc_auc_score(y_test, stack_prob)

# Results
print("Stacking Accuracy:", stack_acc)

print("Stacking ROC-AUC:", stack_auc)

print("\nClassification Report:")
print(classification_report(y_test, stack_pred))

# =========================================================
# Final Comparison
# =========================================================

print("\n================ Final Comparison =================")

comparison = pd.DataFrame({
    "Model": [
        "AdaBoost",
        "GradientBoosting",
        "Stacking"
    ],
    "Accuracy": [
        ada_test_acc,
        results_df["accuracy"].max(),
        stack_acc
    ]
})

print(comparison)

# =========================================================
# Conclusion
# =========================================================

print("\nConclusion:")
print("1. AdaBoost improves weak learners sequentially.")
print("2. Gradient Boosting achieved strong performance with tuned parameters.")
print("3. Stacking combines multiple models to improve generalization.")
print("4. ROC-AUC helps evaluate classification quality beyond accuracy.")
print("5. Ensemble methods generally outperform single models.")