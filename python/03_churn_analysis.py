import pandas as pd

# Load cleaned dataset
file_path = "../data/telco_churn_cleaned.csv"
df = pd.read_csv(file_path)

print("========== CUSTOMER CHURN ANALYSIS ==========\n")

# 1. Overall customer statistics
total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
retained_customers = (df["Churn"] == "No").sum()
churn_rate = (churned_customers / total_customers) * 100

print("--- Overall Customer Metrics ---")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
print(f"Churn Rate: {churn_rate:.2f}%")

# 2. Churn by Contract
print("\n--- Churn by Contract ---")

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print(contract_churn.round(2))

# 3. Churn by Internet Service
print("\n--- Churn by Internet Service ---")

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"],
    normalize="index"
) * 100

print(internet_churn.round(2))

# 4. Churn by Payment Method
print("\n--- Churn by Payment Method ---")

payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
) * 100

print(payment_churn.round(2))

# 5. Churn by Senior Citizen
print("\n--- Churn by Senior Citizen ---")

senior_churn = pd.crosstab(
    df["SeniorCitizen"],
    df["Churn"],
    normalize="index"
) * 100

print(senior_churn.round(2))

# 6. Average monthly charges
print("\n--- Average Monthly Charges ---")

monthly_charges = df.groupby("Churn")["MonthlyCharges"].mean()

print(monthly_charges.round(2))

# 7. Average tenure
print("\n--- Average Tenure ---")

average_tenure = df.groupby("Churn")["tenure"].mean()

print(average_tenure.round(2))