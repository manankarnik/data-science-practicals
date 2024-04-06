from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import csv

dataset = []
with open("groceries.csv", mode="r") as file:
  file = csv.reader(file)
  # Skip first row
  next(file)
  for line in file:
    dataset.append(line[2].split(" "))

# Convert dataset to one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Run FP-Growth
frequent_itemsets = fpgrowth(df, min_support=0.01, use_colnames=True)

# Print the frequent itemsets
print(frequent_itemsets)

