import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.scatter(data.index, data["BMI"])
plt.title("Index vs BMI")
plt.xlabel("Index")
plt.ylabel("BMI")
plt.show()