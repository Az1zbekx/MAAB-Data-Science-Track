import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/car_price.csv")

print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

df = df.dropna()

categorical_cols = df.select_dtypes(include=["object"]).columns

df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

target_column = "price"

X = df.drop(target_column, axis=1)
y = df[target_column]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

X_train = np.c_[np.ones(X_train.shape[0]), X_train]
X_test = np.c_[np.ones(X_test.shape[0]), X_test]

theta = np.zeros(X_train.shape[1])

def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    cost_history = []

    for i in range(iterations):
        predictions = X.dot(theta)

        gradients = (1 / m) * X.T.dot(predictions - y)

        theta = theta - learning_rate * gradients

        cost = compute_cost(X, y, theta)

        cost_history.append(cost)

    return theta, cost_history

learning_rates = [0.001, 0.01, 0.1]

iterations = 1000

results = {}

for lr in learning_rates:
    theta_temp = np.zeros(X_train.shape[1])

    theta_final, cost_history = gradient_descent(
        X_train,
        y_train.values,
        theta_temp,
        lr,
        iterations
    )

    results[lr] = {
        "theta": theta_final,
        "cost_history": cost_history
    }

best_lr = 0.01

best_theta = results[best_lr]["theta"]

train_predictions = X_train.dot(best_theta)
test_predictions = X_test.dot(best_theta)

train_mse = mean_squared_error(y_train, train_predictions)
test_mse = mean_squared_error(y_test, test_predictions)

train_r2 = r2_score(y_train, train_predictions)
test_r2 = r2_score(y_test, test_predictions)

print("\nGradient Descent Results")
print("Train MSE:", train_mse)
print("Test MSE:", test_mse)

print("Train R2:", train_r2)
print("Test R2:", test_r2)

plt.figure(figsize=(10, 6))

for lr in learning_rates:
    plt.plot(
        results[lr]["cost_history"],
        label=f"Learning Rate = {lr}"
    )

plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Cost Function Convergence")
plt.legend()

plt.show()

if "horsepower" in X.columns:
    horsepower_index = list(X.columns).index("horsepower")

    horsepower_values = X_test[:, horsepower_index + 1]

    plt.figure(figsize=(10, 6))

    plt.scatter(horsepower_values, y_test, alpha=0.6, label="Actual")

    plt.scatter(
        horsepower_values,
        test_predictions,
        alpha=0.6,
        label="Predicted"
    )

    plt.xlabel("Horsepower")
    plt.ylabel("Price")
    plt.title("Horsepower vs Car Price")
    plt.legend()

    plt.show()

def mini_batch_gradient_descent(
    X,
    y,
    theta,
    learning_rate,
    iterations,
    batch_size
):
    m = len(y)

    cost_history = []

    for iteration in range(iterations):
        indices = np.random.permutation(m)

        X_shuffled = X[indices]
        y_shuffled = y[indices]

        for i in range(0, m, batch_size):
            X_batch = X_shuffled[i:i + batch_size]
            y_batch = y_shuffled[i:i + batch_size]

            predictions = X_batch.dot(theta)

            gradients = (
                1 / len(y_batch)
            ) * X_batch.T.dot(predictions - y_batch)

            theta = theta - learning_rate * gradients

        cost = compute_cost(X, y, theta)

        cost_history.append(cost)

    return theta, cost_history

mini_theta = np.zeros(X_train.shape[1])

mini_theta, mini_cost_history = mini_batch_gradient_descent(
    X_train,
    y_train.values,
    mini_theta,
    learning_rate=0.01,
    iterations=500,
    batch_size=32
)

mini_predictions = X_test.dot(mini_theta)

mini_mse = mean_squared_error(y_test, mini_predictions)

mini_r2 = r2_score(y_test, mini_predictions)

print("\nMini-Batch Gradient Descent")
print("MSE:", mini_mse)
print("R2:", mini_r2)

def stochastic_gradient_descent(
    X,
    y,
    theta,
    learning_rate,
    iterations
):
    m = len(y)

    cost_history = []

    for iteration in range(iterations):
        for i in range(m):
            random_index = np.random.randint(m)

            X_i = X[random_index:random_index + 1]
            y_i = y[random_index:random_index + 1]

            prediction = X_i.dot(theta)

            gradients = X_i.T.dot(prediction - y_i)

            theta = theta - learning_rate * gradients.flatten()

        cost = compute_cost(X, y, theta)

        cost_history.append(cost)

    return theta, cost_history

sgd_theta = np.zeros(X_train.shape[1])

sgd_theta, sgd_cost_history = stochastic_gradient_descent(
    X_train,
    y_train.values,
    sgd_theta,
    learning_rate=0.001,
    iterations=500
)

sgd_predictions = X_test.dot(sgd_theta)

sgd_mse = mean_squared_error(y_test, sgd_predictions)

sgd_r2 = r2_score(y_test, sgd_predictions)

print("\nStochastic Gradient Descent")
print("MSE:", sgd_mse)
print("R2:", sgd_r2)

sklearn_model = LinearRegression()

sklearn_model.fit(X_train[:, 1:], y_train)

sklearn_predictions = sklearn_model.predict(X_test[:, 1:])

sklearn_mse = mean_squared_error(y_test, sklearn_predictions)

sklearn_r2 = r2_score(y_test, sklearn_predictions)

print("\nScikit-Learn Linear Regression")
print("MSE:", sklearn_mse)
print("R2:", sklearn_r2)

if "horsepower" in X.columns:
    hp_index = list(X.columns).index("horsepower")

    horsepower_feature = X.iloc[:, hp_index].values.reshape(-1, 1)

    poly = PolynomialFeatures(degree=2, include_bias=False)

    horsepower_poly = poly.fit_transform(horsepower_feature)

    hp_train, hp_test, y_hp_train, y_hp_test = train_test_split(
        horsepower_poly,
        y,
        test_size=0.2,
        random_state=42
    )

    poly_model = LinearRegression()

    poly_model.fit(hp_train, y_hp_train)

    poly_predictions = poly_model.predict(hp_test)

    poly_mse = mean_squared_error(y_hp_test, poly_predictions)

    poly_r2 = r2_score(y_hp_test, poly_predictions)

    print("\nPolynomial Regression")
    print("MSE:", poly_mse)
    print("R2:", poly_r2)

print("\nReport")
print("1. Small learning rates converge slowly but are stable.")
print("2. Large learning rates converge faster but may overshoot.")
print("3. Gradient Descent and Mini-Batch methods produce similar results.")
print("4. SGD converges faster but has noisier updates.")
print("5. Polynomial features may improve performance if relationships are non-linear.")