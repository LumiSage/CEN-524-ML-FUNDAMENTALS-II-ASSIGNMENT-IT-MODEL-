
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# Load the synthetic dataset
df = pd.read_csv("devops_synthetic_data.csv")

# Extract features and target
X = df[["Deployment_Frequency", "CI_CD_Failures"]].values
y = df["System_Reliability_Score"].values.reshape(-1, 1)

# Normalize the design matrix
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Add intercept (bias) term to X matrix
X_design = np.hstack([np.ones((X_normalized.shape[0], 1)), X_normalized])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_design, y, test_size=0.2, random_state=42)

# Cost function
def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

# Gradient descent
def gradient_descent(X, y, theta, learning_rate=0.01, iterations=1000):
    m = len(y)
    cost_history = []

    for _ in range(iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = (1 / m) * X.T.dot(errors)
        theta -= learning_rate * gradient
        cost_history.append(compute_cost(X, y, theta))

    return theta, cost_history

# Initialize theta (weights)
theta = np.zeros((X_design.shape[1], 1))

# Train model using gradient descent
theta_final, cost_history = gradient_descent(X_train, y_train, theta)

# Test the model
predictions = X_test.dot(theta_final)
mse = mean_squared_error(y_test, predictions)

print("MSE on Test Set:", mse)
