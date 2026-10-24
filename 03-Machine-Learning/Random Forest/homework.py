# Random Forest Regression - Wine Quality Prediction

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Load dataset
# Download winequality-red.csv from:
# https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/

df = pd.read_csv("winequality-red.csv", sep=";")

# Display first rows
print(df.head())

# Dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Statistical summary
print(df.describe())

# Histograms
df.hist(figsize=(14, 10))
plt.tight_layout()
plt.show()

# Correlation matrix
plt.figure(figsize=(12, 8))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.show()

# Features and target
X = df.drop("quality", axis=1)
y = df["quality"]

# Feature scaling
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest Regressor
rf_model = RandomForestRegressor(
    random_state=42
)

# Train model
rf_model.fit(X_train, y_train)

# Predictions
y_pred = rf_model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Random Forest Regression Results")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

# Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

# Plot feature importance
plt.figure(figsize=(10, 6))

sns.barplot(
    x="Importance",
    y="Feature",
    data=importance
)

plt.title("Feature Importance")
plt.show()

# Hyperparameter tuning
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2],
    "max_features": ["sqrt", "log2"]
}

grid_search = GridSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1
)

# Train GridSearchCV
grid_search.fit(X_train, y_train)

# Best parameters
print("Best Parameters:")
print(grid_search.best_params_)

# Best model
best_model = grid_search.best_estimator_

# Predictions with tuned model
best_pred = best_model.predict(X_test)

# Evaluation
best_mae = mean_absolute_error(y_test, best_pred)
best_mse = mean_squared_error(y_test, best_pred)
best_r2 = r2_score(y_test, best_pred)

print("Tuned Random Forest Results")
print("MAE:", best_mae)
print("MSE:", best_mse)
print("R2 Score:", best_r2)

# Compare with Linear Regression
lr_model = LinearRegression()

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

lr_mae = mean_absolute_error(y_test, lr_pred)
lr_mse = mean_squared_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)

print("Linear Regression Results")
print("MAE:", lr_mae)
print("MSE:", lr_mse)
print("R2 Score:", lr_r2)

# ------------------------------------------
# BONUS: Classification Task
# ------------------------------------------

# Convert quality into categories
# Low: <=5
# Medium: 6
# High: >=7

df["quality_class"] = df["quality"].apply(
    lambda x: "Low" if x <= 5 else (
        "Medium" if x == 6 else "High"
    )
)

# Features and target
X_class = df.drop(
    ["quality", "quality_class"],
    axis=1
)

y_class = df["quality_class"]

# Scale features
X_class_scaled = scaler.fit_transform(X_class)

# Train-test split
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    X_class_scaled,
    y_class,
    test_size=0.2,
    random_state=42
)

# Random Forest Classifier
rf_classifier = RandomForestClassifier(
    random_state=42
)

# Train classifier
rf_classifier.fit(Xc_train, yc_train)

# Predictions
yc_pred = rf_classifier.predict(Xc_test)

# Classification metrics
accuracy = accuracy_score(yc_test, yc_pred)

print("Random Forest Classification Accuracy:")
print(accuracy)

print("Classification Report:")
print(classification_report(yc_test, yc_pred))

print("Confusion Matrix:")
print(confusion_matrix(yc_test, yc_pred))

# Logistic Regression comparison
log_model = LogisticRegression(max_iter=1000)

log_model.fit(Xc_train, yc_train)

log_pred = log_model.predict(Xc_test)

log_accuracy = accuracy_score(yc_test, log_pred)

print("Logistic Regression Accuracy:")
print(log_accuracy)

# Partial Dependence Plot
from sklearn.inspection import PartialDependenceDisplay

features = [0, 10]

PartialDependenceDisplay.from_estimator(
    best_model,
    X_train,
    features,
    feature_names=X.columns
)

plt.show()

# Final insights
print("\nInsights:")
print("1. Alcohol and sulphates are usually strong predictors of wine quality.")
print("2. Random Forest performs better than Linear Regression.")
print("3. Hyperparameter tuning improves prediction performance.")
print("4. Wine quality prediction is difficult because quality ratings are subjective.")
print("5. Random Forest reduces overfitting by averaging many decision trees.")