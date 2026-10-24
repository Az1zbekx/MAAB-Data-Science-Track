import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("data/california_housing.csv")

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

df = df.dropna()

plt.figure(figsize=(10, 8))

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.show()

X = df.drop("MedHouseVal", axis=1)

y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

linear_model = LinearRegression()

linear_model.fit(X_train_scaled, y_train)

linear_predictions = linear_model.predict(X_test_scaled)

linear_mse = mean_squared_error(y_test, linear_predictions)

linear_r2 = r2_score(y_test, linear_predictions)

print("\nLinear Regression")

print("MSE:", linear_mse)

print("R2:", linear_r2)

ridge_params = {
    "alpha": np.logspace(-3, 3, 50)
}

ridge = Ridge()

ridge_grid = GridSearchCV(
    ridge,
    ridge_params,
    cv=5,
    scoring="r2"
)

ridge_grid.fit(X_train_scaled, y_train)

best_ridge = ridge_grid.best_estimator_

ridge_predictions = best_ridge.predict(X_test_scaled)

ridge_mse = mean_squared_error(y_test, ridge_predictions)

ridge_r2 = r2_score(y_test, ridge_predictions)

print("\nRidge Regression")

print("Best Alpha:", ridge_grid.best_params_["alpha"])

print("MSE:", ridge_mse)

print("R2:", ridge_r2)

lasso_params = {
    "alpha": np.logspace(-3, 1, 50)
}

lasso = Lasso(max_iter=10000)

lasso_grid = GridSearchCV(
    lasso,
    lasso_params,
    cv=5,
    scoring="r2"
)

lasso_grid.fit(X_train_scaled, y_train)

best_lasso = lasso_grid.best_estimator_

lasso_predictions = best_lasso.predict(X_test_scaled)

lasso_mse = mean_squared_error(y_test, lasso_predictions)

lasso_r2 = r2_score(y_test, lasso_predictions)

print("\nLasso Regression")

print("Best Alpha:", lasso_grid.best_params_["alpha"])

print("MSE:", lasso_mse)

print("R2:", lasso_r2)

alphas = np.logspace(-3, 3, 100)

ridge_coefficients = []

for alpha in alphas:
    ridge_model = Ridge(alpha=alpha)

    ridge_model.fit(X_train_scaled, y_train)

    ridge_coefficients.append(ridge_model.coef_)

ridge_coefficients = np.array(ridge_coefficients)

plt.figure(figsize=(10, 6))

for i in range(X.shape[1]):
    plt.plot(
        alphas,
        ridge_coefficients[:, i],
        label=X.columns[i]
    )

plt.xscale("log")

plt.xlabel("Alpha")

plt.ylabel("Coefficient Value")

plt.title("Ridge Coefficients vs Alpha")

plt.legend()

plt.show()

lasso_coefficients = []

for alpha in alphas:
    lasso_model = Lasso(alpha=alpha, max_iter=10000)

    lasso_model.fit(X_train_scaled, y_train)

    lasso_coefficients.append(lasso_model.coef_)

lasso_coefficients = np.array(lasso_coefficients)

plt.figure(figsize=(10, 6))

for i in range(X.shape[1]):
    plt.plot(
        alphas,
        lasso_coefficients[:, i],
        label=X.columns[i]
    )

plt.xscale("log")

plt.xlabel("Alpha")

plt.ylabel("Coefficient Value")

plt.title("Lasso Coefficients vs Alpha")

plt.legend()

plt.show()

lasso_non_zero = np.sum(best_lasso.coef_ != 0)

ridge_non_zero = np.sum(best_ridge.coef_ != 0)

linear_non_zero = np.sum(linear_model.coef_ != 0)

comparison_df = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Ridge Regression",
        "Lasso Regression"
    ],
    "MSE": [
        linear_mse,
        ridge_mse,
        lasso_mse
    ],
    "R2": [
        linear_r2,
        ridge_r2,
        lasso_r2
    ],
    "Non-Zero Coefficients": [
        linear_non_zero,
        ridge_non_zero,
        lasso_non_zero
    ]
})

print("\nModel Comparison")

print(comparison_df)

lasso_feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": best_lasso.coef_
})

lasso_feature_importance["AbsCoefficient"] = np.abs(
    lasso_feature_importance["Coefficient"]
)

lasso_feature_importance = lasso_feature_importance.sort_values(
    by="AbsCoefficient",
    ascending=False
)

print("\nLasso Feature Importance")

print(lasso_feature_importance)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=lasso_feature_importance,
    x="AbsCoefficient",
    y="Feature"
)

plt.title("Lasso Feature Importance")

plt.xlabel("Absolute Coefficient")

plt.ylabel("Feature")

plt.show()

elastic_params = {
    "alpha": np.logspace(-3, 1, 20),
    "l1_ratio": [0.1, 0.3, 0.5, 0.7, 0.9]
}

elastic_model = ElasticNet(max_iter=10000)

elastic_grid = GridSearchCV(
    elastic_model,
    elastic_params,
    cv=5,
    scoring="r2"
)

elastic_grid.fit(X_train_scaled, y_train)

best_elastic = elastic_grid.best_estimator_

elastic_predictions = best_elastic.predict(X_test_scaled)

elastic_mse = mean_squared_error(y_test, elastic_predictions)

elastic_r2 = r2_score(y_test, elastic_predictions)

print("\nElasticNet Regression")

print("Best Parameters:", elastic_grid.best_params_)

print("MSE:", elastic_mse)

print("R2:", elastic_r2)

print("\nInsights")

print("1. Regularization helps reduce overfitting by penalizing large coefficients.")

print("2. Ridge regression shrinks coefficients but keeps all features.")

print("3. Lasso regression can reduce some coefficients to zero, performing feature selection.")

print("4. Lasso improves interpretability by identifying the most important features.")

print("5. Higher alpha values increase regularization strength and shrink coefficients more aggressively.")

print("6. Features with the highest absolute Lasso coefficients are the most important predictors of house prices.")