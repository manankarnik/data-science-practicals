import pandas as pd

def min_max_scaling(column, new_min, new_max):
    return (column - column.min()) / (column.max() - column.min()) * (new_max - new_min) + new_min

df = pd.read_csv("movies.csv")
df = df.dropna()

df["SCALED_RATING"] = min_max_scaling(df["RATING"], 1, 10)
print(df.head())
