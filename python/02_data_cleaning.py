import pandas as pd

# Load raw dataset
file_path = "../data/Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)

print("--- Before Cleaning ---")
print("Shape:", df.shape)
print("\nTotalCharges data type:", df["TotalCharges"].dtype)

# Check blank values in TotalCharges
blank_total_charges = (df["TotalCharges"].astype(str).str.strip() == "").sum()

print("Blank TotalCharges:", blank_total_charges)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Check missing values created after conversion
print("\nMissing TotalCharges after conversion:")
print(df["TotalCharges"].isnull().sum())

# Remove rows with missing TotalCharges
df = df.dropna(subset=["TotalCharges"])

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
output_path = "../data/telco_churn_cleaned.csv"
df.to_csv(output_path, index=False)

print("\n--- After Cleaning ---")
print("Shape:", df.shape)
print("TotalCharges data type:", df["TotalCharges"].dtype)
print("Duplicate rows:", df.duplicated().sum())

print("\nCleaned dataset saved successfully!")
print(output_path)