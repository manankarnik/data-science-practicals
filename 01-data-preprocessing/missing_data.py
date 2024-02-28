import pandas as pd

df = pd.read_csv("movies.csv")
print(df.head())

if df["RunTime"].isnull().values.any():
    print("Column with missing values")
    print(df["RunTime"].head())
    df["RunTime"] = df["RunTime"].fillna(df["RunTime"].mean())
    print("\nMissing values filled with mean")
    print(df["RunTime"].head())
else:
    print("No missing values in column")
