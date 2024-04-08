import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
counts = data["Pregnancies"].value_counts()

plt.pie(counts, labels=counts.index)
plt.title('Count of Pregnancies')
plt.show()