import pandas as pd

df = pd.read_csv("movies.csv")
df = df.dropna()

mean = df["RATING"].mean()
std_dev = df["RATING"].std()
df["SCALED_RATING"] = (df["RATING"] - mean) / std_dev

print(df.head())
