import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

Q1 = data["BMI"].quantile(0.25)
Q3 = data["BMI"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outlier_indices = (data["BMI"] < lower_bound) | (data["BMI"] > upper_bound)
print("Outlier Indices:")
print(outlier_indices.index[outlier_indices].tolist())
print("Rows with Outliers:")
print(data[outlier_indices])


#removing oultiers
data_without_outliers = data.query(f"BMI >= {lower_bound} & BMI <= {upper_bound}")
plt.boxplot(data_without_outliers["BMI"])
plt.title("BMI")
plt.show()

#Mean, Median, Min, Max
print("Mean BMI:", data_without_outliers["BMI"].mean())
print("Median BMI:", data_without_outliers["BMI"].median())
print("Min BMI:", data_without_outliers["BMI"].min())
print("Max BMI:", data_without_outliers["BMI"].max())

