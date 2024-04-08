import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
#Correlation
correlation = data.dropna().corr().round(2)
print(correlation)