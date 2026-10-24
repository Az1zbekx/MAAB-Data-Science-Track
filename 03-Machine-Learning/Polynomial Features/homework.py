import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = load_diabetes()

df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

print(df.head())
print(df.shape)
print(data.feature_names)
print(df.describe())

X = df.drop("target", axis=1)
y = df["target"]

poly_features = ["bmi", "bp", "s5"]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "poly",
            PolynomialFeatures(degree=2, include_bias=False),
            poly_features
        )
    ],
    remainder="passthrough"
)

poly_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

linear_model = LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

linear_model.fit(X_train, y_train)

poly_pipeline.fit(X_train, y_train)

poly = PolynomialFeatures(degree=2, include_bias=False)

poly.fit(X[poly_features])

poly_feature_names = poly.get_feature_names_out(poly_features)

all_feature_names = list(poly_feature_names)

remaining_features = [col for col in X.columns if col not in poly_features]

all_feature_names.extend(remaining_features)

print("Number of polynomial features:", len(poly_feature_names))
print("Expanded feature names:")
print(all_feature_names)

linear_preds = linear_model.predict(X_test)

poly_preds = poly_pipeline.predict(X_test)

linear_mae = mean_absolute_error(y_test, linear_preds)
linear_rmse = np.sqrt(mean_squared_error(y_test, linear_preds))
linear_r2 = r2_score(y_test, linear_preds)

poly_mae = mean_absolute_error(y_test, poly_preds)
poly_rmse = np.sqrt(mean_squared_error(y_test, poly_preds))
poly_r2 = r2_score(y_test, poly_preds)

print("\nBaseline Linear Regression Metrics")
print("MAE:", linear_mae)
print("RMSE:", linear_rmse)
print("R2:", linear_r2)

print("\nPolynomial Regression Metrics")
print("MAE:", poly_mae)
print("RMSE:", poly_rmse)
print("R2:", poly_r2)

coefficients = poly_pipeline.named_steps["model"].coef_

coef_df = pd.DataFrame({
    "Feature": all_feature_names,
    "Coefficient": coefficients
})

coef_df["AbsCoefficient"] = np.abs(coef_df["Coefficient"])

top_10 = coef_df.sort_values(
    by="AbsCoefficient",
    ascending=False
).head(10)

print("\nTop 10 Largest Coefficients")
print(top_10[["Feature", "Coefficient"]])

print("\nCoefficient Explanations:")
print("1. bmi coefficient shows body mass index strongly affects diabetes progression.")
print("2. s5 coefficient relates to serum measurements associated with disease severity.")
print("3. bmi^2 or interaction terms indicate non-linear relationships between health indicators.")

plt.figure(figsize=(8, 6))
plt.scatter(y_test, linear_preds, alpha=0.7, label="Linear")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Linear Regression: Predictions vs Actual")
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(y_test, poly_preds, alpha=0.7, label="Polynomial")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Polynomial Regression: Predictions vs Actual")
plt.legend()
plt.show()

metrics = ["MAE", "RMSE"]

baseline_scores = [linear_mae, linear_rmse]
poly_scores = [poly_mae, poly_rmse]

x = np.arange(len(metrics))
width = 0.35

plt.figure(figsize=(8, 6))

plt.bar(x - width/2, baseline_scores, width, label="Baseline")
plt.bar(x + width/2, poly_scores, width, label="Polynomial")

plt.xticks(x, metrics)
plt.ylabel("Error")
plt.title("Error Comparison")
plt.legend()

plt.show()

X_bmi = df[["bmi"]]
y_bmi = df["target"]

poly_single = PolynomialFeatures(degree=2, include_bias=False)

X_bmi_poly = poly_single.fit_transform(X_bmi)

single_model = LinearRegression()

single_model.fit(X_bmi_poly, y_bmi)

x_sorted = np.sort(X_bmi.values.flatten())

x_sorted_df = pd.DataFrame({"bmi": x_sorted})

x_sorted_poly = poly_single.transform(x_sorted_df)

y_curve = single_model.predict(x_sorted_poly)

plt.figure(figsize=(8, 6))

plt.scatter(X_bmi, y_bmi, alpha=0.5)

plt.plot(x_sorted, y_curve, linewidth=2)

plt.xlabel("BMI")
plt.ylabel("Target")
plt.title("Polynomial Curve Fit for BMI")

plt.show()

sample_input = pd.DataFrame({
    "age": [0.05],
    "sex": [0.02],
    "bmi": [0.04],
    "bp": [0.03],
    "s1": [-0.02],
    "s2": [-0.01],
    "s3": [0.00],
    "s4": [0.02],
    "s5": [0.03],
    "s6": [0.01]
})

linear_prediction = linear_model.predict(sample_input)

poly_prediction = poly_pipeline.predict(sample_input)

print("\nSample Predictions")
print("Linear Regression Prediction:", linear_prediction[0])
print("Polynomial Regression Prediction:", poly_prediction[0])

print("\nModel Comparison")
if poly_r2 > linear_r2:
    print("Polynomial features improved the model.")
else:
    print("Polynomial features did not significantly improve the model.")

print("Polynomial regression can capture non-linear relationships.")
print("However, the diabetes dataset is relatively small,")
print("so additional polynomial terms may lead to overfitting.")