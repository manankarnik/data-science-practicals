import pandas as pd 

#Summary:
print("Summary:")
data = pd.read_csv("data.csv")
print(data)
print(data.describe())

#Diabetic:
diabetic = data.query("Outcome == 1")
print("\nDiabetic:")
print(diabetic)

#Pregnant and not Diabetic:
print("\nPregnant and not Diabetic:")
pregnant_and_not_diabetic = data.query("Outcome == 0 & Pregnancies >= 1")
print(pregnant_and_not_diabetic)

#Pregnant or not Diabetic:
print("\nPregnant or not Diabetic:")
pregnant_or_not_diabetic = data.query("Outcome == 0 | Pregnancies >= 1")
print(pregnant_or_not_diabetic)

#Ascending BMI:
print("\nAscending BMI:")
ascending_bmi = data.sort_values("BMI")
print(ascending_bmi[["Pregnancies", "Glucose", "Age", "BMI", "Outcome"]])

#Decending BMI:
print("\nDescending BMI:")
descending_bmi = data.sort_values("BMI", ascending=False)
print(descending_bmi[["Pregnancies", "Glucose", "Age", "BMI", "Outcome"]])

#Aggregate Data and Names:
print("\nAggregate Data and Names:")
aggregate_data = data.groupby('Outcome')['BMI'].mean().reset_index()
print(aggregate_data)
print(data.columns.tolist())

#No. of Null Entries:
print("\nNo. of Null Entries:")
print(data.isna().sum().sum())