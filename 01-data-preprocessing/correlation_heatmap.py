import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movies.csv")
df = df.dropna(subset=["VOTES", "Gross"])
df["VOTES"] = df["VOTES"].str.replace(",", "").astype(int)
df["Gross"] = (df["Gross"].str.replace("$", "")).str.replace("M", "").astype(float)

numeric_df = df.select_dtypes(include=["float", "int"])
corr_matrix = numeric_df.corr()

sns.heatmap(corr_matrix, annot=True, fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
