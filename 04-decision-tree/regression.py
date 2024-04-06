import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

np.random.seed(42)

X_1 = 2 * np.random.rand(768, 8)
y1 = 4 + 3 * X_1 + np.random.randn(768, 8)
y2 = 2 + 2 * X_1 + np.random.randn(768, 8)
y = np.hstack((y1, y2))

X_train, X_test, y_train, y_test = train_test_split(X_1, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

threshold = 0.5
y_pred_binary = (y_pred > threshold).astype(int)
plt.scatter(y_pred, y_test)
plt.xlabel("Predicted Values")
plt.ylabel("Actual Values")
plt.title("Scatter Plot of Predicted vs Actual Values")
plt.show()
