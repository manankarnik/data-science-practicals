import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")
df = df.dropna(subset=["Gross", "RunTime"])
# Convert Gross column from string to float
df["Gross"] = (df["Gross"].str.replace("$", "")).str.replace("M", "").astype(float)

df[["Gross", "RunTime"]].plot(kind="box", title="boxplot")
plt.show()
