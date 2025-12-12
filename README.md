# Superstore Sales & Customer Profitability Analysis (SQLite)

A complete end-to-end SQL analytics project using the Superstore dataset.  
This project demonstrates practical skills in data cleaning, KPI analysis, customer segmentation, discount impact evaluation, and profitability insights.

---

# 📑 Table of Contents

1. [Project Overview](#project-overview)  
2. [Objectives](#objectives)  
3. [Data Preparation](#data-preparation)  
4. [Overall KPIs](#overall-kpis)  
5. [Yearly Performance](#yearly-performance)  
6. [Category Performance](#category-performance)  
7. [Monthly Sales & Profit Trend](#monthly-sales--profit-trend)  
8. [Regional Sales & Profit Analysis](#regional-sales--profit-analysis)  
9. [Top 10 Most Profitable Customers](#top-10-most-profitable-customers)  
10. [Unprofitable Customers Analysis](#unprofitable-customers-analysis)  
11. [Final Notes](#final-notes)

---

# 📘 Project Overview

This SQL project performs a complete analysis of the Superstore dataset using **SQLite**.  
It evaluates sales trends, category profitability, customer behavior, discount effects, and regional performance.

The project highlights real-world Data Analyst capabilities including:

- SQL-based data cleaning  
- KPI development  
- Trend & segmentation analysis  
- Insight generation for business decisions  

---

# 🎯 Objectives

- Analyze **sales trends** over time  
- Identify **profitable vs. low-profit categories**  
- Segment customers based on **profitability**  
- Measure the **impact of discounts**  
- Compare **regional performance**  
---
# 🛠 Data Preparation

### **1. Convert date columns into ISO format (`YYYY-MM-DD`)**

The dataset originally contained dates in inconsistent formats (e.g., `11/8/2016`).  
They were transformed into ISO format so SQLite could process them correctly.

### **2. Create a clean view for analysis**

### Sample Cleaned Data (compact preview)
### Full Data Preview (All Columns)

> Scroll horizontally to view all columns →

| # | Order ID | Order Date | Ship Date | Ship Mode | Customer ID | Customer Name | Segment | Country | City | State | Postal Code | Region | Product ID | Category | Sub-Category | Product Name | Sales | Quantity | Discount | Profit | ISO Order Date | Year | Month |
|---|----------|------------|-----------|-----------|-------------|----------------|---------|---------|------|--------|-------------|--------|------------|-----------|---------------|--------------|--------|----------|-----------|---------|----------------|------|-------|
| 1 | CA-2016-152156 | 11/8/2016 | 11/11/2016 | Second Class | CG-12520 | Claire Gute | Consumer | United States | Henderson | Kentucky | 42420 | South | FUR-BO-10001798 | Furniture | Bookcases | Bush Somerset Collection Bookcase | 261.96 | 2 | 0 | 41.9136 | 2016-11-08 | 2016 | 11 |
| 2 | CA-2016-152156 | 11/8/2016 | 11/11/2016 | Second Class | CG-12520 | Claire Gute | Consumer | United States | Henderson | Kentucky | 42420 | South | FUR-CH-10000454 | Furniture | Chairs | Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back | 731.94 | 3 | 0 | 219.582 | 2016-11-08 | 2016 | 11 |
| 3 | CA-2016-138688 | 6/12/2016 | 6/16/2016 | Second Class | DV-13045 | Darrin Van Huff | Corporate | United States | Los Angeles | California | 90036 | West | OFF-LA-10000240 | Office Supplies | Labels | Self-Adhesive Address Labels for Typewriters by Universal | 14.62 | 2 | 0 | 6.8714 | 2016-06-12 | 2016 | 06 |





---

# 📊 Overall KPIs

* **5,009 unique orders**
* **Total sales:** $2.30M
* **Total profit:** $286K
* **Overall profit margin:** ~12–13%

---

# 📈 Yearly Performance

| Year | Sales (USD) | Profit (USD) |
| ---- | ----------- | ------------ |
| 2014 | 484,247.50  | 49,543.97    |
| 2015 | 470,532.51  | 61,618.60    |
| 2016 | 609,205.60  | 81,795.17    |
| 2017 | 733,215.26  | 93,439.27    |

### **Insights**

* Revenue dipped slightly in 2015 vs. 2014, but profit rose.
* Sales and profit grew sharply in 2016 and 2017, showing positive momentum.

---

# 🛒 Category Performance

| Category        | Sales (USD) | Profit (USD) |
| --------------- | ----------: | -----------: |
| Technology      |  836,154.03 |   145,454.95 |
| Furniture       |  741,999.80 |    18,451.27 |
| Office Supplies |  719,047.03 |   122,490.80 |

### **Insights**

* Technology is the strongest category by a wide margin.
* Office Supplies also shows high profitability.
* Furniture generates high sales but minimal profit due to low margins.

---

# 📅 Monthly Sales & Profit Trend

```sql
SELECT
    order_year,
    order_month,
    order_year || '-' || order_month AS year_month,
    ROUND(SUM(sales), 2)  AS monthly_sales,
    ROUND(SUM(profit), 2) AS monthly_profit
FROM orders_clean
GROUP BY order_year, order_month
ORDER BY order_year, order_month;
```

### **Insights**

* **Q4 consistently delivers the highest revenue**, especially November and December.
* Profit does not always rise with sales due to discounting (especially in Q4).
* **Q1 is the weakest period**, reflecting post-holiday slowdown.
* Some months (e.g., **March, October**) show unusually high margins.
* Negative-profit months (e.g., **July 2014**, **Jan 2015**) highlight unprofitable discounting.
* **2017** is the strongest year overall.

---

# 🌎 Regional Sales & Profit Analysis

```sql
SELECT
    region,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales), 2)     AS total_sales,
    ROUND(SUM(profit), 2)    AS total_profit,
    ROUND(AVG(discount), 4)  AS avg_discount,
    ROUND((SUM(profit) * 100.0 / SUM(sales)), 2) AS profit_margin_pct
FROM orders_clean
GROUP BY region
ORDER BY total_sales DESC;
```

### **Insights**

* **West** leads all regions in revenue ($725K) and profit ($108K) with the highest margin (14.9%).
* **East** performs strongly but with slightly lower margins.
* **Central** suffers from high discounting (avg 24%) and the lowest margin (7.9%).
* **South** has the lowest revenue but healthier margins than Central.
* Strong negative correlation: **higher discount = lower margin**.
* **West + East = 60% of total revenue**.

---

# 🏆 Top 10 Most Profitable Customers

```sql
SELECT
    customer_id,
    customer_name,
    ROUND(SUM(sales), 2)  AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS order_count
FROM orders_clean
GROUP BY customer_id, customer_name
ORDER BY total_profit DESC
LIMIT 10;
```

### **Insights**

* **Tamara Chand** is the most profitable customer ($8,981 profit from 5 orders).
* Raymond Buch and Sanjit Chand also contribute strongly.
* Some frequent buyers (e.g., **Keith Dawkins**) generate low profit due to product mix or discounts.
* Profitability is not equal to revenue — discounts and category margins matter.
* Top 10 customers contribute **~17% of total company profit**.
* Valuable for CRM, loyalty programs, and pricing optimization.

---

# 🚨 Unprofitable Customers Analysis

```sql
SELECT
    customer_id,
    customer_name,
    ROUND(SUM(sales), 2)  AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS order_count
FROM orders_clean
GROUP BY customer_id, customer_name
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;
```

### **Insights**

* **Cindy Stewart** is the most unprofitable customer (–$6,626 loss).
* Several others (e.g., **Grant Thornton**, **Luke Foster**) produce significant losses.
* High-frequency customers with negative profit (e.g., **Henry Goldwyn**, **Zuschuss Carroll**) are structurally unprofitable.
* Some customers generate high sales but negative profit → discount-heavy transactions.
* Negative-profit customers collectively account for **over –$70K in loss**.
* Indicates need for improved discount strategy and targeted segmentation.

```





