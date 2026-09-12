import pandas as pd

# Load segmented dataset
file_path = "../data/customer_churn_segmented.csv"
df = pd.read_csv(file_path)

print("========== RETENTION & REVENUE ANALYSIS ==========\n")

# ---------------------------------------------------
# 1. Revenue by Churn Status
# ---------------------------------------------------

print("--- Revenue by Churn Status ---")

revenue_by_churn = df.groupby("Churn")["MonthlyCharges"].agg(
    ["count", "sum", "mean"]
)

revenue_by_churn.columns = [
    "Customers",
    "Monthly_Revenue",
    "Average_Monthly_Charge"
]

print(revenue_by_churn.round(2))


# ---------------------------------------------------
# 2. Revenue by Risk Segment
# ---------------------------------------------------

print("\n--- Revenue by Risk Segment ---")

revenue_by_risk = df.groupby("RiskSegment").agg(
    Customers=("customerID", "count"),
    Monthly_Revenue=("MonthlyCharges", "sum"),
    Average_Monthly_Charge=("MonthlyCharges", "mean")
)

print(revenue_by_risk.round(2))


# ---------------------------------------------------
# 3. High-Risk Customer Revenue
# ---------------------------------------------------

high_risk = df[df["RiskSegment"] == "High Risk"]

high_risk_customers = len(high_risk)
high_risk_revenue = high_risk["MonthlyCharges"].sum()

print("\n--- High-Risk Customer Exposure ---")
print("High-Risk Customers:", high_risk_customers)
print(f"High-Risk Monthly Revenue: ${high_risk_revenue:,.2f}")


# ---------------------------------------------------
# 4. Churned Customer Revenue
# ---------------------------------------------------

churned = df[df["Churn"] == "Yes"]

churned_customers = len(churned)
churned_monthly_revenue = churned["MonthlyCharges"].sum()

print("\n--- Churned Customer Revenue ---")
print("Churned Customers:", churned_customers)
print(f"Monthly Revenue from Churned Customers: ${churned_monthly_revenue:,.2f}")


# ---------------------------------------------------
# 5. Potential Annual Revenue Exposure
# ---------------------------------------------------

annual_revenue_exposure = churned_monthly_revenue * 12

print("\n--- Potential Annual Revenue Exposure ---")
print(f"Annualized Revenue Exposure: ${annual_revenue_exposure:,.2f}")


# ---------------------------------------------------
# 6. High-Risk Customers Who Have Already Churned
# ---------------------------------------------------

high_risk_churn = high_risk[high_risk["Churn"] == "Yes"]

print("\n--- High-Risk Churned Customers ---")
print("High-Risk Churned Customers:", len(high_risk_churn))

print(
    f"High-Risk Churned Monthly Revenue: "
    f"${high_risk_churn['MonthlyCharges'].sum():,.2f}"
)


# ---------------------------------------------------
# 7. Retention Opportunity
# ---------------------------------------------------

retention_opportunity = high_risk[high_risk["Churn"] == "No"]

print("\n--- Retention Opportunity ---")
print("High-Risk Customers Still Active:", len(retention_opportunity))

print(
    f"Monthly Revenue from High-Risk Active Customers: "
    f"${retention_opportunity['MonthlyCharges'].sum():,.2f}"
)


# ---------------------------------------------------
# 8. Save Retention Analysis Dataset
# ---------------------------------------------------

output_path = "../data/customer_retention_analysis.csv"

df.to_csv(output_path, index=False)

print("\nRetention analysis dataset saved successfully!")
print(output_path)