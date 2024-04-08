import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.hist(data["BMI"], edgecolor='black')
plt.title("BMI vs Frequency")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.show()