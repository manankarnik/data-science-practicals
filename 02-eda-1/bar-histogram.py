import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")
df = df.dropna()
# Map string to int
df["VOTES"] = df["VOTES"].str.replace(",", "").astype(int)

plt.hist(df["VOTES"], bins=10, edgecolor="black")
plt.xlabel("Votes")
plt.ylabel("Frequency")
plt.title("Histogram of Votes")
plt.show()

# Reduce data to 10 records for better plot
df = df[:10]
plt.bar(df["MOVIES"], df["VOTES"], edgecolor="black")
plt.xlabel("Movies")
plt.ylabel("Votes")
plt.title("Bar Plot of Votes")
plt.show()
