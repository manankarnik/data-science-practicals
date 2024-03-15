import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv("movies.csv")

contingency_table = pd.crosstab(df["RATING"], df["VOTES"])
chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

print(f"Chi-squared value: {chi2_stat}")
print(f"P-value: {p_value}")

alpha = 0.5

if p_value < alpha:
    print("Null Hypothesis: Rejected (both values are dependent)")
else:
    print("Null Hypothesis: Accepted (both values are independent)")

