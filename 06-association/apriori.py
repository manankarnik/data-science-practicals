from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import seaborn as sns
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

# Run Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# Print the association rules
print(rules)

# Plot
plt.xticks(rotation=90)
sns.barplot(x="itemsets", y="support", data=frequent_itemsets.nlargest(n=15,
columns="support"), palette="mako")
plt.show()
