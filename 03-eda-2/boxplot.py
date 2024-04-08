import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.boxplot(data.dropna()["BMI"])
plt.title("BMI")
plt.show()

#Boxplot of Skin Thickness
pregnant_and_not_diabetic = data.query("Outcome == 0 & Pregnancies >= 1")
plt.boxplot(pregnant_and_not_diabetic["SkinThickness"])
plt.title("Skin Thickness")
plt.show()