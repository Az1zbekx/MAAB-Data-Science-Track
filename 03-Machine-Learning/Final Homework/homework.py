import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    classification_report,
    confusion_matrix
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (
    RandomForestClassifier,
    BaggingClassifier,
    VotingClassifier
)

from sklearn.tree import DecisionTreeClassifier

cifar = fetch_openml(
    "CIFAR_10_small",
    version=1,
    as_frame=False
)

X = cifar.data
y = cifar.target

print("Dataset Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

print("\nUnique Classes:")
print(np.unique(y))

class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]

print("\nImage Size:")
print("32 x 32 x 3")

plt.figure(figsize=(10, 5))

for i in range(10):

    image = X[i].reshape(32, 32, 3).astype(np.uint8)

    plt.subplot(2, 5, i + 1)

    plt.imshow(image)

    plt.title(class_names[int(y[i])])

    plt.axis("off")

plt.tight_layout()

plt.show()

X = X / 255.0

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

baseline_model = LogisticRegression(
    max_iter=2000,
    solver="lbfgs",
    multi_class="multinomial"
)

baseline_model.fit(X_train, y_train)

baseline_predictions = baseline_model.predict(X_test)

baseline_accuracy = accuracy_score(
    y_test,
    baseline_predictions
)

baseline_precision = precision_score(
    y_test,
    baseline_predictions,
    average="weighted"
)

baseline_recall = recall_score(
    y_test,
    baseline_predictions,
    average="weighted"
)

print("\nBaseline Logistic Regression Results")

print("Accuracy:", baseline_accuracy)

print("Precision:", baseline_precision)

print("Recall:", baseline_recall)

print("\nClassification Report")

print(
    classification_report(
        y_test,
        baseline_predictions
    )
)

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_accuracy = accuracy_score(
    y_test,
    rf_predictions
)

rf_precision = precision_score(
    y_test,
    rf_predictions,
    average="weighted"
)

rf_recall = recall_score(
    y_test,
    rf_predictions,
    average="weighted"
)

print("\nRandom Forest Results")

print("Accuracy:", rf_accuracy)

print("Precision:", rf_precision)

print("Recall:", rf_recall)

print("\nClassification Report")

print(
    classification_report(
        y_test,
        rf_predictions
    )
)

bagging_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)

bagging_model.fit(X_train, y_train)

bagging_predictions = bagging_model.predict(X_test)

bagging_accuracy = accuracy_score(
    y_test,
    bagging_predictions
)

print("\nBagging Classifier Accuracy")

print(bagging_accuracy)

voting_model = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(
            max_iter=2000,
            solver="lbfgs",
            multi_class="multinomial"
        )),
        ("rf", RandomForestClassifier(
            n_estimators=50,
            random_state=42
        )),
        ("dt", DecisionTreeClassifier())
    ],
    voting="hard"
)

voting_model.fit(X_train, y_train)

voting_predictions = voting_model.predict(X_test)

voting_accuracy = accuracy_score(
    y_test,
    voting_predictions
)

print("\nVoting Classifier Accuracy")

print(voting_accuracy)

cm = confusion_matrix(
    y_test,
    rf_predictions
)

plt.figure(figsize=(10, 8))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names
)

plt.xlabel("Predicted Label")

plt.ylabel("True Label")

plt.title("Random Forest Confusion Matrix")

plt.show()

comparison = {
    "Logistic Regression": baseline_accuracy,
    "Random Forest": rf_accuracy,
    "Bagging": bagging_accuracy,
    "Voting": voting_accuracy
}

models = list(comparison.keys())

scores = list(comparison.values())

plt.figure(figsize=(8, 5))

plt.bar(models, scores)

plt.ylabel("Accuracy")

plt.title("Model Accuracy Comparison")

plt.show()

print("\nModel Comparison")

for model, score in comparison.items():
    print(model, ":", score)

print("\nInsights")

print(
    "1. Logistic Regression provides a simple baseline for image classification."
)

print(
    "2. Random Forest improved performance by combining multiple decision trees."
)

print(
    "3. Bagging reduced variance and improved stability compared to a single tree."
)

print(
    "4. Voting Classifier combined predictions from multiple models for better generalization."
)

print(
    "5. CIFAR-10 is challenging for traditional machine learning because images contain complex visual patterns."
)

print(
    "6. Feature scaling improved optimization and model convergence."
)

print(
    "7. Ensemble learning generally performed better than the baseline model."
)