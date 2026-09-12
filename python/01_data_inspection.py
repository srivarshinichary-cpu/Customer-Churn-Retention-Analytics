import pandas as pd

# Load dataset
file_path = "../data/Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)

# Basic information
print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

print("\n--- Churn Distribution ---")
print(df["Churn"].value_counts())

print("\n--- Churn Percentage ---")
print(df["Churn"].value_counts(normalize=True) * 100)