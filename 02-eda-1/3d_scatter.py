import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("movies.csv")
df = df.dropna(subset=["VOTES", "Gross"])
# Convert Votes column from string to int
df["VOTES"] = df["VOTES"].str.replace(",", "").astype(int)
# Convert Gross column from string to float
df["Gross"] = (df["Gross"].str.replace("$", "")).str.replace("M", "").astype(float)

ax = plt.axes(projection ="3d")
ax.scatter3D(df["Gross"], df["RunTime"], df["VOTES"])
plt.title("3D Scatter Plot")
plt.legend("upper right")
plt.show()
