import pandas as pd

df = pd.read_csv("F:\PythonL\Data\crisis_data.csv.csv")


print("Missing values in each column:")
print(df.isnull().sum())


if df.isnull().values.any():
    print("The dataset contains missing values.")
else:
    print("The dataset has no missing values.")