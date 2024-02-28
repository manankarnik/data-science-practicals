import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movies.csv")
df = df.dropna()
df["VOTES"] = df["VOTES"].str.replace(",", "").astype(int)

correlation = df["RATING"].corr(df["VOTES"])
print(f"Pearson Correlation: {correlation:.2f}")

sns.regplot(x="RATING", y="VOTES", data=df, scatter_kws={"alpha": 0.5})
plt.title("Scatter plot of Rating vs Votes")
plt.xlabel("Rating")
plt.ylabel("Votes")
plt.text(df["RATING"].min(), df["VOTES"].max(), f"Pearson Correlation: {correlation:.2f}", horizontalalignment="left")
plt.show()

