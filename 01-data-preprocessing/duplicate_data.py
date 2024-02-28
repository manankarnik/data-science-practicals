import pandas as pd

df = pd.read_csv("movies.csv")
print("Records:", len(df))
df.drop_duplicates(inplace=True)
print("Records after dropping duplicates:", len(df))

