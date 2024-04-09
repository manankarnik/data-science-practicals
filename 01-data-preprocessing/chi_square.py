import pandas as pd
from scipy.stats import chi2, chi2_contingency

df = pd.read_csv("movies.csv")

contingency_table = pd.crosstab(df["RATING"], df["VOTES"])
chi2_stat, p_value, dof, ef = chi2_contingency(contingency_table)

print(f"Chi-squared value: {chi2_stat}")
print(f"P-value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequency: {ef}")

alpha = 0.5
critical_value = chi2.ppf(1 - alpha, dof)
print(f"Critical Value: {critical_value}")

if chi2_stat > critical_value:
    print("Reject null hypothesis. There is a significant association between VOTES and RATING.")
else:
    print("Fail to reject null hypothesis based on critical value.")

if p_value < alpha:
    print("Null Hypothesis: Rejected (both values are dependent)")
else:
    print("Null Hypothesis: Accepted (both values are independent)")
