-- ============================================================
-- Customer Churn & Retention Analytics
-- SQL Analysis | MySQL
-- ============================================================

USE customer_churn;

-- ============================================================
-- 1. OVERALL CHURN ANALYSIS
-- ============================================================

SELECT
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS retained_customers,
ROUND(
100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate
FROM customer_churn_data;

-- ============================================================
-- 2. CHURN RATE BY CONTRACT TYPE
-- ============================================================

SELECT
Contract,
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate
FROM customer_churn_data
GROUP BY Contract
ORDER BY churn_rate DESC;

-- ============================================================
-- 3. CHURN RATE BY INTERNET SERVICE
-- ============================================================

SELECT
InternetService,
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate
FROM customer_churn_data
GROUP BY InternetService
ORDER BY churn_rate DESC;

-- ============================================================
-- 4. CHURN RATE BY PAYMENT METHOD
-- ============================================================

SELECT
PaymentMethod,
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate
FROM customer_churn_data
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;

-- ============================================================
-- 5. CHURN RATE BY TENURE GROUP
-- ============================================================

SELECT
CASE
WHEN tenure < 12 THEN '0-11 Months'
WHEN tenure < 24 THEN '12-23 Months'
WHEN tenure < 48 THEN '24-47 Months'
ELSE '48+ Months'
END AS tenure_group,
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate
FROM customer_churn_data
GROUP BY tenure_group
ORDER BY churn_rate DESC;

-- ============================================================
-- 6. CHURN RATE BY SENIOR CITIZEN STATUS
-- ============================================================

SELECT
CASE
WHEN SeniorCitizen = 1 THEN 'Senior Citizen'
ELSE 'Non-Senior'
END AS customer_group,
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate
FROM customer_churn_data
GROUP BY SeniorCitizen
ORDER BY churn_rate DESC;

-- ============================================================
-- 7. MONTHLY REVENUE BY CHURN STATUS
-- ============================================================

SELECT
Churn,
COUNT(*) AS customers,
ROUND(SUM(MonthlyCharges), 2) AS monthly_revenue,
ROUND(AVG(MonthlyCharges), 2) AS average_monthly_charge
FROM customer_churn_data
GROUP BY Churn
ORDER BY Churn;

-- ============================================================
-- 8. REVENUE AND CHURN BY RISK SEGMENT
-- ============================================================

SELECT
RiskSegment,
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate,
ROUND(SUM(MonthlyCharges), 2) AS monthly_revenue
FROM customer_churn_data
GROUP BY RiskSegment
ORDER BY churn_rate DESC;

-- ============================================================
-- 9. HIGH-RISK ACTIVE CUSTOMER OPPORTUNITY
-- ============================================================

SELECT
COUNT(*) AS high_risk_active_customers,
ROUND(SUM(MonthlyCharges), 2) AS monthly_revenue_opportunity,
ROUND(SUM(MonthlyCharges) * 12, 2) AS annualized_revenue_opportunity
FROM customer_churn_data
WHERE RiskSegment = 'High Risk'
AND Churn = 'No';

-- ============================================================
-- 10. HIGH-RISK CHURN ANALYSIS
-- ============================================================

SELECT
RiskSegment,
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate
FROM customer_churn_data
WHERE RiskSegment = 'High Risk'
GROUP BY RiskSegment;

-- ============================================================
-- 11. CONTRACT + PAYMENT METHOD ANALYSIS
-- ============================================================

WITH contract_payment AS (
SELECT
Contract,
PaymentMethod,
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM customer_churn_data
GROUP BY Contract, PaymentMethod
)
SELECT
Contract,
PaymentMethod,
total_customers,
churned_customers,
ROUND(
100.0 * churned_customers / total_customers,
2
) AS churn_rate
FROM contract_payment
ORDER BY churn_rate DESC;

-- ============================================================
-- 12. RANK CUSTOMER GROUPS BY CHURN RATE
-- ============================================================

WITH churn_summary AS (
SELECT
Contract,
PaymentMethod,
COUNT(*) AS total_customers,
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM customer_churn_data
GROUP BY Contract, PaymentMethod
),
ranked_groups AS (
SELECT
Contract,
PaymentMethod,
total_customers,
churned_customers,
ROUND(
100.0 * churned_customers / total_customers,
2
) AS churn_rate
FROM churn_summary
)
SELECT
Contract,
PaymentMethod,
total_customers,
churned_customers,
churn_rate,
RANK() OVER (ORDER BY churn_rate DESC) AS churn_rank
FROM ranked_groups
ORDER BY churn_rank;

-- ============================================================
-- 13. CHURNED REVENUE EXPOSURE
-- ============================================================

SELECT
COUNT(*) AS churned_customers,
ROUND(SUM(MonthlyCharges), 2) AS monthly_revenue_exposure,
ROUND(SUM(MonthlyCharges) * 12, 2) AS annualized_revenue_exposure
FROM customer_churn_data
WHERE Churn = 'Yes';

-- ============================================================
-- END OF ANALYSIS
-- ============================================================
