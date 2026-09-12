# Customer Churn & Retention Analytics

**Python | SQL | Power BI**

An end-to-end data analytics project that analyzes customer churn, identifies high-risk customer segments, evaluates revenue exposure, and presents actionable retention insights through an interactive Power BI dashboard.

## Project Overview

Customer churn directly impacts recurring revenue and customer lifetime value. This project analyzes telecom customer data to understand **why customers churn, which customer groups are most at risk, and where retention efforts can have the greatest business impact**.

The analysis follows a complete analytics workflow:

**Data Inspection → Data Cleaning → Exploratory Analysis → Customer Risk Segmentation → SQL Analysis → Power BI Dashboard → Business Recommendations**

## Dataset

* **Source:** Telco Customer Churn dataset
* **Original records:** 7,043
* **Records after cleaning:** 7,032
* **Features:** 21 customer and service attributes
* **Target variable:** Churn

## Tools & Technologies

* **Python:** Pandas, NumPy
* **SQL:** MySQL
* **Visualization:** Power BI
* **Data Analysis:** Excel concepts, descriptive statistics, segmentation
* **Version Control:** Git & GitHub

## Project Structure

```text
Customer-Churn-Retention-Analytics/
│
├── data/
│   ├── Telco-Customer-Churn.csv
│   ├── telco_churn_cleaned.csv
│   ├── customer_churn_segmented.csv
│   └── customer_retention_analysis.csv
│
├── python/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   ├── 03_churn_analysis.py
│   ├── 04_customer_segmentation.py
│   └── 05_retention_analysis.py
│
├── sql/
│   └── churn_analysis.sql
│
├── powerbi/
│   └── Customer_Churn_Retention_Analytics.pbix
│
├── screenshots/
│
└── README.md
```

## Python Analysis

Python was used to inspect, clean, analyze, and segment the customer data.

### Data Cleaning

* Identified `TotalCharges` as an object-type field.
* Converted `TotalCharges` to numeric format.
* Identified 11 records with missing `TotalCharges`.
* Removed the 11 incomplete records.
* Final analytical dataset contains **7,032 customers**.

### Churn Analysis

Key findings:

* **Total customers:** 7,032
* **Churned customers:** 1,869
* **Retained customers:** 5,163
* **Overall churn rate:** 26.58%
* **Average tenure of churned customers:** 17.98 months
* **Average tenure of retained customers:** 37.65 months
* **Average monthly charge of churned customers:** $74.44
* **Average monthly charge of retained customers:** $61.31

## Customer Risk Segmentation

An **explainable rule-based risk score** was developed to identify customers with higher churn risk.

Risk factors included:

* Month-to-month contract
* Tenure below 12 months
* Higher-than-median monthly charges
* Electronic check payment method

Customers were grouped into:

* **Low Risk:** Score 0–2
* **Medium Risk:** Score 3–4
* **High Risk:** Score 5–7

### Risk Results

| Risk Segment | Customers | Churn Rate |
| ------------ | --------: | ---------: |
| Low Risk     |     3,251 |      6.71% |
| Medium Risk  |     1,911 |     28.89% |
| High Risk    |     1,870 |     58.77% |

The high-risk segment shows a substantially higher churn rate than the low-risk segment, making it a strong focus area for retention initiatives.

> **Note:** This is an explainable analytical segmentation approach, not a machine-learning prediction model.

## SQL Analysis

MySQL was used to validate and extend the Python analysis.

SQL techniques included:

* `GROUP BY`
* Aggregate functions
* `CASE`
* Filtering
* Subqueries
* **CTEs**
* **Window functions**
* `RANK()`

Example analyses:

* Overall churn rate
* Churn by contract type
* Churn by internet service
* Churn by payment method
* Churn by tenure group
* Churn by senior-citizen status
* Monthly revenue by churn status
* Revenue by risk segment
* High-risk active customer opportunity
* Contract + payment-method churn analysis
* Ranking customer groups by churn rate

## Power BI Dashboard

The Power BI report contains **two interactive pages**.

### Page 1 — Executive Overview

Includes:

* Total Customers
* Churned Customers
* Churn Rate
* Monthly Revenue
* Churn Rate by Contract
* Churn Rate by Tenure
* Contract slicer
* Payment Method slicer
* Internet Service slicer

### Page 2 — Customer Risk & Churn

Includes:

* Churn Rate by Payment Method
* Customer Risk Segmentation
* Churn Rate by Internet Service
* High-Risk Churn Rate
* High-Risk Active Customers
* High-Risk Monthly Revenue

## Key Business Insights

### 1. Month-to-month customers show the highest churn

Month-to-month customers have a churn rate of approximately **42.7%**, considerably higher than customers on longer-term contracts.

### 2. Early-tenure customers are more likely to churn

Customers with less than 12 months of tenure have a churn rate of approximately **48.5%**, indicating that the early customer lifecycle is a critical retention period.

### 3. High-risk customers require targeted retention

The rule-based high-risk segment contains **1,870 customers** with a **58.77% churn rate**.

### 4. High-risk active customers represent a retention opportunity

There are **771 active high-risk customers**, representing approximately **$60.36K in monthly recurring charges**.

### 5. Churned customers have higher average monthly charges

Churned customers have an average monthly charge of approximately **$74.44**, compared with **$61.31** among retained customers.

## Business Recommendations

Based on the analysis:

1. **Prioritize early-tenure customers** with proactive onboarding and engagement.
2. **Target month-to-month customers** with incentives for longer-term contracts.
3. **Focus retention campaigns on high-risk customers** rather than using a one-size-fits-all approach.
4. **Review payment experience**, particularly for customers using electronic checks.
5. **Monitor higher-value customers at risk of churn** because their monthly charges are relatively higher.
6. Use Power BI monitoring to track churn trends and evaluate retention strategies over time.

## Project Outcome

This project demonstrates an end-to-end data analytics workflow combining:

**Python for data preparation and analysis → SQL for analytical querying → Power BI for interactive business reporting.**

It focuses on translating customer-level data into **measurable churn insights, customer risk segments, revenue opportunities, and actionable retention recommendations**.
