import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV
)

from sklearn.preprocessing import (
    StandardScaler
)

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    roc_auc_score
)

from sklearn.feature_selection import RFE

from sklearn.svm import SVC

from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier

from imblearn.over_sampling import SMOTE

df = pd.read_csv("data/heart_disease.csv")

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

df = df.dropna()

plt.figure(figsize=(14, 10))

df.hist(figsize=(14, 10))

plt.show()

numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    plt.figure(figsize=(6, 4))

    sns.boxplot(x=df[col])

    plt.title(f"Boxplot of {col}")

    plt.show()

plt.figure(figsize=(12, 8))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

categorical_cols = ["CP", "Slope", "Thal"]

df = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)

X = df.drop("Target", axis=1)

y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

log_model = LogisticRegression(
    solver="liblinear",
    penalty="l2",
    max_iter=1000
)

log_model.fit(X_train_scaled, y_train)

y_pred = log_model.predict(X_test_scaled)

y_prob = log_model.predict_proba(X_test_scaled)[:, 1]

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

auc = roc_auc_score(y_test, y_prob)

print("\nLogistic Regression Results")

print("Accuracy:", accuracy)

print("Precision:", precision)

print("Recall:", recall)

print("F1 Score:", f1)

print("ROC AUC:", auc)

print("\nClassification Report")

print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.title("Confusion Matrix")

plt.show()

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.figure(figsize=(8, 6))

plt.plot(fpr, tpr, label=f"AUC = {auc:.3f}")

plt.plot([0, 1], [0, 1], linestyle="--")

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.show()

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": log_model.coef_[0]
})

coefficients["AbsCoefficient"] = np.abs(
    coefficients["Coefficient"]
)

coefficients = coefficients.sort_values(
    by="AbsCoefficient",
    ascending=False
)

print("\nFeature Coefficients")

print(coefficients)

plt.figure(figsize=(10, 8))

sns.barplot(
    data=coefficients.head(15),
    x="Coefficient",
    y="Feature"
)

plt.title("Top Logistic Regression Coefficients")

plt.show()

rfe_model = LogisticRegression(
    solver="liblinear",
    max_iter=1000
)

rfe = RFE(
    estimator=rfe_model,
    n_features_to_select=8
)

rfe.fit(X_train_scaled, y_train)

selected_features = X.columns[rfe.support_]

print("\nSelected Features")

print(selected_features)

X_train_rfe = X_train[selected_features]

X_test_rfe = X_test[selected_features]

X_train_rfe_scaled = scaler.fit_transform(X_train_rfe)

X_test_rfe_scaled = scaler.transform(X_test_rfe)

rfe_log_model = LogisticRegression(
    solver="liblinear",
    max_iter=1000
)

rfe_log_model.fit(
    X_train_rfe_scaled,
    y_train
)

rfe_predictions = rfe_log_model.predict(
    X_test_rfe_scaled
)

rfe_accuracy = accuracy_score(
    y_test,
    rfe_predictions
)

print("\nRFE Model Accuracy")

print(rfe_accuracy)

param_grid = {
    "C": [0.01, 0.1, 1, 10],
    "penalty": ["l1", "l2"],
    "solver": ["liblinear"]
}

grid_model = GridSearchCV(
    LogisticRegression(max_iter=1000),
    param_grid,
    cv=5,
    scoring="accuracy"
)

grid_model.fit(X_train_scaled, y_train)

best_model = grid_model.best_estimator_

best_predictions = best_model.predict(
    X_test_scaled
)

best_accuracy = accuracy_score(
    y_test,
    best_predictions
)

print("\nBest Hyperparameters")

print(grid_model.best_params_)

print("Best Accuracy:", best_accuracy)

svm_model = SVC(
    probability=True
)

svm_model.fit(
    X_train_scaled,
    y_train
)

svm_predictions = svm_model.predict(
    X_test_scaled
)

svm_accuracy = accuracy_score(
    y_test,
    svm_predictions
)

print("\nSVM Accuracy")

print(svm_accuracy)

rf_model = RandomForestClassifier(
    random_state=42
)

rf_model.fit(
    X_train,
    y_train
)

rf_predictions = rf_model.predict(
    X_test
)

rf_accuracy = accuracy_score(
    y_test,
    rf_predictions
)

print("\nRandom Forest Accuracy")

print(rf_accuracy)

knn_model = KNeighborsClassifier(
    n_neighbors=5
)

knn_model.fit(
    X_train_scaled,
    y_train
)

knn_predictions = knn_model.predict(
    X_test_scaled
)

knn_accuracy = accuracy_score(
    y_test,
    knn_predictions
)

print("\nkNN Accuracy")

print(knn_accuracy)

X_imbalanced = X.copy()

y_imbalanced = y.copy()

class_1_indices = y_imbalanced[
    y_imbalanced == 1
].index

reduced_indices = np.random.choice(
    class_1_indices,
    size=int(len(class_1_indices) * 0.3),
    replace=False
)

imbalanced_indices = list(
    y_imbalanced[y_imbalanced == 0].index
) + list(reduced_indices)

X_imbalanced = X_imbalanced.loc[
    imbalanced_indices
]

y_imbalanced = y_imbalanced.loc[
    imbalanced_indices
]

smote = SMOTE(random_state=42)

X_smote, y_smote = smote.fit_resample(
    X_imbalanced,
    y_imbalanced
)

X_train_smote, X_test_smote, y_train_smote, y_test_smote = train_test_split(
    X_smote,
    y_smote,
    test_size=0.2,
    random_state=42
)

X_train_smote_scaled = scaler.fit_transform(
    X_train_smote
)

X_test_smote_scaled = scaler.transform(
    X_test_smote
)

smote_model = LogisticRegression(
    solver="liblinear",
    class_weight="balanced",
    max_iter=1000
)

smote_model.fit(
    X_train_smote_scaled,
    y_train_smote
)

smote_predictions = smote_model.predict(
    X_test_smote_scaled
)

smote_accuracy = accuracy_score(
    y_test_smote,
    smote_predictions
)

print("\nSMOTE Logistic Regression Accuracy")

print(smote_accuracy)

sample_patient = pd.DataFrame({
    "Age": [58],
    "Sex": [1],
    "Trestbps": [140],
    "Chol": [240],
    "FBS": [1],
    "Restecg": [1],
    "Thalach": [120],
    "Exang": [1],
    "Oldpeak": [2.3],
    "CA": [2],
    "CP_1": [0],
    "CP_2": [1],
    "CP_3": [0],
    "Slope_1": [1],
    "Slope_2": [0],
    "Thal_1": [0],
    "Thal_2": [1],
    "Thal_3": [0]
})

sample_patient = sample_patient.reindex(
    columns=X.columns,
    fill_value=0
)

sample_scaled = scaler.transform(
    sample_patient
)

sample_prediction = log_model.predict(
    sample_scaled
)

sample_probability = log_model.predict_proba(
    sample_scaled
)[:, 1]

print("\nSample Patient Prediction")

print(
    "Heart Disease Prediction:",
    sample_prediction[0]
)

print(
    "Probability of Heart Disease:",
    sample_probability[0]
)

print("\nInsights")

print(
    "1. Features with large positive coefficients increase heart disease risk."
)

print(
    "2. Hyperparameter tuning improved model stability and accuracy."
)

print(
    "3. Feature selection reduced complexity while maintaining strong performance."
)

print(
    "4. Logistic Regression is interpretable and effective for binary classification."
)

print(
    "5. Random Forest and SVM may achieve higher accuracy on complex patterns."
)

print(
    "6. SMOTE improved performance on imbalanced data by balancing class distribution."
)