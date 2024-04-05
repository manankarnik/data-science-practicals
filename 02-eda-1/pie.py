import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")
df = df.dropna()
# Reduce data to 10 records for better plot
df = df[:10]
print(df)
# Map string to int
df["VOTES"] = df["VOTES"].str.replace(",", "").astype(int)

plt.pie(df["VOTES"], labels=df["MOVIES"], autopct="%1.1f%%")
plt.title("Votes")
plt.axis("equal")
plt.show()

