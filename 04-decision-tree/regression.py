import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Generate random data
X_1 = 2 * np.random.rand(768, 8)
y1 = 4 + 3 * X_1 + np.random.randn(768, 8)
y2 = 2 + 2 * X_1 + np.random.randn(768, 8)
y = np.hstack((y1, y2))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_1, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print predicted values
print(y_pred)

# Calculate Mean Squared Error and R-squared
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Set threshold for binary classification
threshold = 0.5

# Convert predictions to binary based on threshold
y_pred_binary = (y_pred > threshold).astype(int)

# Plot scatter plot of predicted vs actual values
plt.scatter(y_pred, y_test)
plt.xlabel("Predicted Values")
plt.ylabel("Actual Values")
plt.title("Scatter Plot of Predicted vs Actual Values")
plt.show()

