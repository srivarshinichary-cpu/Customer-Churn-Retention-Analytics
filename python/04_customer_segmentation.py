import pandas as pd

# Load cleaned dataset
file_path = "../data/telco_churn_cleaned.csv"
df = pd.read_csv(file_path)

print("========== CUSTOMER RISK SEGMENTATION ==========\n")

# Calculate median monthly charges
monthly_charge_median = df["MonthlyCharges"].median()

print(f"Monthly Charges Median: {monthly_charge_median:.2f}")

# Create risk score
df["RiskScore"] = 0

# Contract risk
df.loc[df["Contract"] == "Month-to-month", "RiskScore"] += 2

# Tenure risk
df.loc[df["tenure"] < 12, "RiskScore"] += 2

# Monthly charges risk
df.loc[df["MonthlyCharges"] > monthly_charge_median, "RiskScore"] += 1

# Payment method risk
df.loc[df["PaymentMethod"] == "Electronic check", "RiskScore"] += 2


# Create risk segments
def classify_risk(score):
    if score <= 2:
        return "Low Risk"
    elif score <= 4:
        return "Medium Risk"
    else:
        return "High Risk"


df["RiskSegment"] = df["RiskScore"].apply(classify_risk)


# Risk segment distribution
print("\n--- Customer Risk Segments ---")
print(df["RiskSegment"].value_counts())

# Risk segment percentages
print("\n--- Risk Segment Percentages ---")
risk_percentage = (
    df["RiskSegment"]
    .value_counts(normalize=True) * 100
)

print(risk_percentage.round(2))


# Churn rate by risk segment
print("\n--- Churn Rate by Risk Segment ---")

risk_churn = pd.crosstab(
    df["RiskSegment"],
    df["Churn"],
    normalize="index"
) * 100

print(risk_churn.round(2))


# Average monthly charges by risk segment
print("\n--- Average Monthly Charges by Risk Segment ---")

avg_charges = df.groupby("RiskSegment")["MonthlyCharges"].mean()

print(avg_charges.round(2))


# Average tenure by risk segment
print("\n--- Average Tenure by Risk Segment ---")

avg_tenure = df.groupby("RiskSegment")["tenure"].mean()

print(avg_tenure.round(2))


# Save segmented dataset
output_path = "../data/customer_churn_segmented.csv"
df.to_csv(output_path, index=False)

print("\nSegmented dataset saved successfully!")
print(output_path)