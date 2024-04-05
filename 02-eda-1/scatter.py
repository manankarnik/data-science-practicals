import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")
df = df.dropna(subset=["VOTES", "Gross"])
# Convert Votes column from string to int
df["VOTES"] = df["VOTES"].str.replace(",", "").astype(int)
# Convert Gross column from string to float
df["Gross"] = (df["Gross"].str.replace("$", "")).str.replace("M", "").astype(float)

plt.scatter(df["VOTES"], df["Gross"])
plt.xlabel('Votes')
plt.ylabel('Gross (Millions)')
plt.title('Scatter Plot of Votes vs Gross')
plt.grid(True)
plt.show()
