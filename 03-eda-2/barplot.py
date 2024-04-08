import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
counts = data["Outcome"].value_counts()
plt.bar(counts.index, counts)
plt.title('Count of Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.show()

#Barplot of Pregnancies
counts = data["Pregnancies"].value_counts()
plt.bar(counts.index, counts)
plt.title('Count of Pregnancies')
plt.xlabel('Pregnancies')
plt.ylabel('Count')
plt.show()